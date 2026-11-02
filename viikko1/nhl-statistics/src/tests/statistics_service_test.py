import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_olemassa_olevan_pelaajan(self):
            pelaaja = self.stats.search("Kurri")
        
            self.assertEqual(pelaaja.name, "Kurri")
            self.assertEqual(pelaaja.team, "EDM")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        pelaaja = self.stats.search("Laine")
        
        self.assertIsNone(pelaaja)

    def test_team_palauttaa_oikean_maaran_pelaajia(self):
        edm_pelaajat = self.stats.team("EDM")
        
        self.assertEqual(len(edm_pelaajat), 3)
        self.assertEqual(edm_pelaajat[0].name, "Semenko")
        self.assertEqual(edm_pelaajat[1].name, "Kurri")
        self.assertEqual(edm_pelaajat[2].name, "Gretzky")

    def test_top_palauttaa_oikeat_pelaajat_pistejarjestyksessa(self):
        parhaat = self.stats.top(2)
        
        self.assertEqual(len(parhaat), 3)
        self.assertEqual(parhaat[0].name, "Gretzky") # 124 pistettä
        self.assertEqual(parhaat[1].name, "Lemieux") # 99 pistettä
        self.assertEqual(parhaat[2].name, "Yzerman") # 98 pistettä

    def test_top_palauttaa_oikeat_pelaajat_maalien_perusteella(self):
        parhaat = self.stats.top(2, SortBy.GOALS)
        
        self.assertEqual(len(parhaat), 3)
        self.assertEqual(parhaat[0].name, "Lemieux")
        self.assertEqual(parhaat[1].name, "Yzerman")
        self.assertEqual(parhaat[2].name, "Kurri")

    def test_top_palauttaa_oikeat_pelaajat_syottojen_perusteella(self):
        parhaat = self.stats.top(2, SortBy.ASSISTS)
        
        self.assertEqual(len(parhaat), 3)
        self.assertEqual(parhaat[0].name, "Gretzky")
        self.assertEqual(parhaat[1].name, "Yzerman")
        self.assertEqual(parhaat[2].name, "Lemieux")