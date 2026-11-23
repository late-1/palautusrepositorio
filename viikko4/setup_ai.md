### Reflektointi

Agentti poisti järkevästi toiston erityttämällä ostotapahtuman uuteen apumetodiin. Lisäksi se siivosi käyttämättömät importit. Testikoodi on nyt tiiviimpää ja helpommin luettavaa.

Agentti ei muuttanut testien toiminnallisuutta tai poistanut tarkistuksia. Ensimmäisessä testissä säilyi alkuperäinen assert_called() -tarkistus, ja muissa säilyivät assert_called_with(...) tarkistukset. 

Ainut tarve omalle toiminnalle oli testien ajaminen, agentti ei saanut niitä itse ajettua virtuaaliympäristön takia jostain syystä. 