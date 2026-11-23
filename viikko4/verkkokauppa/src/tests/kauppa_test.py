import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            if tuote_id == 3:
                return Tuote(3, "kahvi", 7)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def maksa_ostokset(self, *tuote_idt):
        self.kauppa.aloita_asiointi()
        for tuote_id in tuote_idt:
            self.kauppa.lisaa_koriin(tuote_id)
        self.kauppa.tilimaksu("pekka", "12345")

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.maksa_ostokset(1)

        self.pankki_mock.tilisiirto.assert_called()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.maksa_ostokset(1)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kaksi_eri_tuotetta_ja_tilisiirto_oikeilla_parametreilla(self):
        self.maksa_ostokset(1, 2)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8
        )

    def test_kaksi_samaa_tuotetta_ja_tilisiirto_oikeilla_parametreilla(self):
        self.maksa_ostokset(1, 1)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_varastossa_oleva_ja_loppu_oleva_tuote_ja_tilisiirto_oikeilla_parametreilla(self):
        self.maksa_ostokset(1, 3)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.maksa_ostokset(1)
        self.maksa_ostokset(2)

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 3
        )

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [10, 20, 30]

        self.maksa_ostokset(1)
        self.maksa_ostokset(2)
        self.maksa_ostokset(1, 2)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[0][0],
            ("pekka", 10, "12345", "33333-44455", 5)
        )
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[1][0],
            ("pekka", 20, "12345", "33333-44455", 3)
        )
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list[2][0],
            ("pekka", 30, "12345", "33333-44455", 8)
        )

    def test_poista_korista_poistaa_tuotteen_ja_palauttaa_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 3
        )
        self.varasto_mock.palauta_varastoon.assert_called_once()
