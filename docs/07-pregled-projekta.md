# 07 - Pregled projekta

Projekt KockiTsa sem prevzel od kolega. Najprej sem ga zagnal pri sebi po navodilih iz README-ja, napolnil katalog s seed skripto in nato aplikacijo preizkusil kot kupec, prodajalec in administrator. Vmes sem prebral še dokumentacijo, ADR-je in kodo, da sem dobil občutek, kako je vse skupaj sestavljeno.

## Kaj je narejeno

Za MVP je bilo predvidenih 7 funkcionalnosti in narejene so vse:

1. Registracija in prijava z vlogo
2. Oddaja oglasa v pregled
3. Pregled oglasov pred objavo (odobritev ali zavrnitev z razlogom)
4. Rezervacija oglasa
5. Potrditev prodaje ali sprostitev rezervacije
6. Zamenjava vloge na profilu
7. Iskanje kompleta z ujemanjem oglasov

Celoten potek oglasa sem preizkusil od začetka do konca: oddal sem oglas, ga kot administrator odobril, kot kupec rezerviral, potem sprostil, ponovno rezerviral in na koncu potrdil prodajo. Vse je delovalo brez težav.

## Uporabniške zgodbe

Podrobneje sem pogledal pet zgodb, po eno iz vsakega večjega dela aplikacije:

- **US-03 - Oddaja oglasa:** zadošča. Komplet je mogoče izbrati samo iz kataloga, cena se preverja, nov oglas pa najprej čaka na pregled in še ni javno viden.
- **US-06 - Zavrnitev oglasa z razlogom:** zadošča. Brez vpisanega razloga oglasa ni mogoče zavrniti, prodajalec pa razlog vidi pri svojem oglasu.
- **US-07 - Rezervacija oglasa:** zadošča. Rezervira lahko samo kupec, svojega oglasa ne more, če pa oglas medtem rezervira nekdo drug, dobi sporočilo "Oglas ni več na voljo".
- **US-09 - Potrditev prodaje:** zadošča. Prodajo lahko potrdi samo prodajalec, ki je oglas objavil, in ko je oglas enkrat prodan, se ga ne da več spremeniti.
- **US-14 - Ujemajoči oglasi:** zadošča. Pri iskanju se prikažejo oglasi, ki ustrezajo ceni in stanju, v meniju pa je število iskanj, ki imajo zadetke.

## Zaključek

Projekt je narejen dobro in pokriva vse, kar je bilo načrtovano za MVP. Edino, kar bi izboljšal, je README, ki ima navodila za zagon samo za Windows, ne pa tudi za macOS.