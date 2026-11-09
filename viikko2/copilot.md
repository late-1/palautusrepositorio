### Copilot raportti 

1. Kuinka hyödyllisiksi koit koodin täydennyksen ehdotukset?

    Koodin täydennykset ja tekoälyn apu olivat hyödyllisiä, erityisesti pylint konfiguraation säätämisessä, luokkien refaktoroinnissa ja GHA -putken määrittelyssä. 

2. Pitikö Copilotin selitys Pylint-varoituksesta paikkansa?
    
    Pitkälti kyllä. Agentti osasi selittää miksi koodi kaatui pylint-tarkastuksessa ja osasi korjata suurimman osan virheistä itse. 

3. Tekikö agentti toimivan ratkaisun, ja testit? 

    Ratkaisu toimi, mutta testejä piti hieman muokata sekä lisätä vielä ´pytest.ini´ tiedosto jossa määritellään ´pythonpath = src´


4. Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?

    Agentti generoi testit käyttäen Pythonin sisäänrakennettua ´unittest´ -kirjastoa joka eroaa viime viikosta. Stubin käyttö eristämään verkkopyyntöjä oli kuitenkin sama kun edellisen viikon testeissä. 

5. Löysikö Pylint agentin koodista virheitä?

    Kyllä. Pylint löysi agentin aiemmin tuottamasta koodista ylimääräisiä tyhjiä lyöntejä (trailing whitespace), tiedostojen lopusta puuttuvia tyhjiä rivejä, importtien järjestysvirheitä, liian pitkän main-funtion (Too many statements) sekä dict-varatun sanan käytön parametrinä ja API-pyynnön puuttuvan timeoutin.

6. Mitä muuta opit

    Opin agenttien käytöstä ja muutosten tarkastelun tärkeydestä. 