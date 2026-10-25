# 01 – Zasnova rešitve

## Ime rešitve

**KockiTsa**

## Namen rešitve in problem, ki ga naslavlja

KockiTsa je spletna tržnica, na kateri posamezniki prodajajo in kupujejo nove in rabljene LEGO komplete.

Rešitev naslavlja štiri težave, ki nastanejo pri prodaji kompletov prek splošnih spletnih oglasnikov:

- **Oglasov pred objavo nihče ne pregleda.** Oglas je lahko nepopoln ali zavajajoč.
- **Iz oglasa ni razvidno, ali je komplet še na voljo.** Oglas lahko ostane objavljen tudi po tem, ko je komplet že prodan.
- **Oglas ni vezan na točno določen komplet.** Prodajalec naslov in opis vpiše po svoje, zato kupec težko najde vse ponudbe za isti komplet in primerja njihove cene.
- **Kupec mora oglase preverjati sam.** Če kompleta, ki ga išče, trenutno nihče ne prodaja, mora seznam oglasov pregledovati znova in znova.

KockiTsa te težave odpravi tako:

- vsak oglas pred objavo pregleda administrator, ki ga odobri ali zavrne;
- vsak oglas ima status, iz katerega je razvidno, ali je komplet na voljo, rezerviran ali prodan;
- vsak oglas je vezan na komplet iz kataloga (številka kompleta, ime, tema, število kock, leto izdaje);
- kupec shrani iskanje kompleta z najvišjo ceno in sprejemljivimi stanji, rešitev pa mu sama pokaže oglas, ki iskanju ustreza, ko je objavljen.

## Ciljni uporabniki

- **Prodajalci** – posamezniki, ki imajo doma LEGO komplete, ki jih ne potrebujejo več, na primer starši ali zbiratelji, ki prodajajo del zbirke.
- **Kupci** – ljubitelji in zbiratelji LEGO kock ter starši, ki iščejo točno določen komplet ali cenejši rabljen komplet.

## Kratek opis delovanja

1. Uporabnik se registrira kot kupec ali prodajalec in se prijavi. Vlogo lahko kasneje zamenja na svojem profilu.
2. Prodajalec izbere komplet iz kataloga, vpiše stanje kompleta, ceno in opis ter odda oglas. Oglas še ni javno viden.
3. Administrator oglas pregleda in ga odobri ali zavrne. Odobren oglas postane javno viden.
4. Kupec, ki želenega kompleta ne najde, shrani iskanje z najvišjo ceno in sprejemljivimi stanji. Ko administrator odobri oglas, ki iskanju ustreza, ga rešitev pokaže pri kupčevem iskanju.
5. Kupec med objavljenimi oglasi ali pri svojem iskanju izbere oglas in ga rezervira. Rezerviranega oglasa drugi kupci ne morejo več rezervirati. Kupec in prodajalec vidita e-poštni naslov drug drugega in se dogovorita za prevzem.
6. Po prevzemu prodajalec potrdi prodajo; kupčevo iskanje za ta komplet se s tem zaključi. Če do prodaje ne pride, prodajalec rezervacijo sprosti in oglas je znova na voljo.

Plačilo in predaja kompleta potekata neposredno med kupcem in prodajalcem, zunaj rešitve.

## Primer uporabe

Prodajalec ima doma sestavljen komplet iz teme Star Wars, ki ga ne potrebuje več. V katalogu poišče komplet po številki, izbere stanje »rabljen«, vpiše ceno 60 € in kratek opis ter odda oglas. Administrator oglas pregleda in ga odobri. Kupec, ki išče prav ta komplet, oglas najde med objavljenimi oglasi in ga rezervira. S prodajalcem se po e-pošti dogovorita za prevzem. Po prevzemu prodajalec v rešitvi potrdi prodajo in oglas dobi status »prodan«.
