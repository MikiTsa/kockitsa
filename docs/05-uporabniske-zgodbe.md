# 05 – Uporabniške zgodbe

## Pregled

| Zgodba | Povezana funkcionalnost | Uporabniška vloga |
|---|---|---|
| US-01 | 1 – Registracija in prijava z vlogo | obiskovalec |
| US-02 | 1 – Registracija in prijava z vlogo | kupec, prodajalec, administrator |
| US-03 | 2 – Oddaja oglasa v pregled | prodajalec |
| US-04 | 2 – Oddaja oglasa v pregled | prodajalec |
| US-05 | 3 – Pregled oglasov pred objavo | administrator |
| US-06 | 3 – Pregled oglasov pred objavo | administrator |
| US-07 | 4 – Rezervacija oglasa | kupec |
| US-08 | 4 – Rezervacija oglasa | kupec |
| US-09 | 5 – Potrditev prodaje ali sprostitev rezervacije | prodajalec |
| US-10 | 5 – Potrditev prodaje ali sprostitev rezervacije | prodajalec |
| US-11 | 6 – Zamenjava vloge na profilu | kupec, prodajalec |
| US-12 | 6 – Zamenjava vloge na profilu | kupec, prodajalec |
| US-13 | 7 – Iskanje kompleta z ujemanjem oglasov | kupec |
| US-14 | 7 – Iskanje kompleta z ujemanjem oglasov | kupec |
| US-15 | 7 – Iskanje kompleta z ujemanjem oglasov | kupec |

## US-01 – Registracija

> **Kot** obiskovalec **želim** ustvariti račun z imenom, e-pošto in geslom ter izbrati vlogo kupca ali prodajalca, **da** lahko na tržnici kupujem ali prodajam komplete.

- **Povezana funkcionalnost:** 1 – Registracija in prijava z vlogo
- **Uporabniška vloga:** obiskovalec (neprijavljen uporabnik)

Acceptance criteria:

1. Obrazec za registracijo ima polja ime, e-pošta in geslo ter izbiro vloge »kupec« ali »prodajalec«; vloge »administrator« ni mogoče izbrati.
2. Če katero od polj ni izpolnjeno ali vloga ni izbrana, se račun ne ustvari in ob manjkajočem podatku se prikaže sporočilo o napaki.
3. Če račun z vpisano e-pošto že obstaja, se nov račun ne ustvari in prikaže se sporočilo »Račun s tem e-poštnim naslovom že obstaja«.
4. Geslo je v podatkovni bazi shranjeno samo kot zgoščena vrednost (bcrypt), nikoli v berljivi obliki.
5. Po uspešni registraciji je uporabnik preusmerjen na stran za prijavo.

## US-02 – Prijava in odjava

> **Kot** registriran uporabnik **se želim** prijaviti z e-pošto in geslom, **da** lahko uporabljam možnosti svoje vloge.

- **Povezana funkcionalnost:** 1 – Registracija in prijava z vlogo
- **Uporabniška vloga:** kupec, prodajalec, administrator

Acceptance criteria:

1. Ob pravilni e-pošti in geslu je uporabnik prijavljen; v glavi strani sta prikazana njegovo ime in trenutna vloga.
2. Ob napačni e-pošti ali geslu uporabnik ni prijavljen in prikaže se sporočilo »Napačna e-pošta ali geslo«, ki ne pove, kateri od podatkov je napačen.
3. Meni po prijavi vsebuje samo možnosti trenutne vloge: kupec vidi »Oglasi«, »Moja iskanja« in »Profil«, prodajalec »Oglasi«, »Oddaj oglas«, »Moji oglasi« in »Profil«, administrator »Oglasi v pregledu«.
4. Neprijavljen uporabnik, ki odpre stran, za katero je potrebna prijava, je preusmerjen na stran za prijavo.
5. Po kliku na »Odjava« je seja izbrisana in strani, za katere je potrebna prijava, niso več dostopne.

## US-03 – Oddaja oglasa

> **Kot** prodajalec **želim** oddati oglas za komplet iz kataloga, **da** ga po odobritvi lahko ponudim kupcem.

- **Povezana funkcionalnost:** 2 – Oddaja oglasa v pregled
- **Uporabniška vloga:** prodajalec

Acceptance criteria:

1. Prodajalec komplet poišče po številki ali imenu in ga izbere iz kataloga; oglasa za komplet, ki ga v katalogu ni, ni mogoče oddati.
2. Stanje (zapečaten, nov ali rabljen) in cena sta obvezna, opis ni obvezen.
3. Cena mora biti število, večje od 0, z največ dvema decimalnima mestoma; sicer se oglas ne odda in ob polju se prikaže sporočilo o napaki.
4. Oddani oglas ima status »v pregledu« in ni prikazan na seznamu objavljenih oglasov.
5. Oglas lahko odda samo uporabnik v vlogi prodajalca; zahtevek kupca ali administratorja backend zavrne.

## US-04 – Pregled lastnih oglasov

> **Kot** prodajalec **želim** na enem mestu videti vse svoje oglase z njihovim statusom, **da** vem, kateri čakajo na pregled in kateri so objavljeni, rezervirani, prodani ali zavrnjeni.

- **Povezana funkcionalnost:** 2 – Oddaja oglasa v pregled
- **Uporabniška vloga:** prodajalec

Acceptance criteria:

1. Seznam »Moji oglasi« vsebuje vse oglase, ki jih je oddal prijavljeni prodajalec, ne glede na status, in nobenega oglasa drugih prodajalcev.
2. Pri vsakem oglasu so prikazani številka in ime kompleta, stanje, cena, status in čas oddaje.
3. Oglasi so razvrščeni po času oddaje, najnovejši je prvi.
4. Če prodajalec še nima oglasov, se prikaže sporočilo »Nimate še oglasov« s povezavo na oddajo oglasa.

## US-05 – Odobritev oglasa

> **Kot** administrator **želim** pregledati oglase, ki čakajo na pregled, in ustrezne odobriti, **da** so javno objavljeni samo popolni in nezavajajoči oglasi.

- **Povezana funkcionalnost:** 3 – Pregled oglasov pred objavo
- **Uporabniška vloga:** administrator

Acceptance criteria:

1. Seznam »Oglasi v pregledu« vsebuje vse oglase s statusom »v pregledu« in nobenega drugega; razvrščeni so po času oddaje, najstarejši je prvi.
2. Pri vsakem oglasu so prikazani številka in ime kompleta, stanje, cena, opis, ime prodajalca in čas oddaje.
3. Po kliku na »Odobri« dobi oglas status »objavljen«, izgine s seznama »Oglasi v pregledu« in je prikazan na seznamu objavljenih oglasov.
4. Administrator cene in opisa oglasa ne more spremeniti.
5. Uporabnik, ki ni administrator, seznama ne vidi; njegov zahtevek za odobritev backend zavrne.

## US-06 – Zavrnitev oglasa z razlogom

> **Kot** administrator **želim** neustrezen oglas zavrniti in vpisati razlog, **da** oglas ni objavljen in prodajalec ve, kaj mora v novem oglasu popraviti.

- **Povezana funkcionalnost:** 3 – Pregled oglasov pred objavo
- **Uporabniška vloga:** administrator

Acceptance criteria:

1. Po kliku na »Zavrni« se prikaže polje za razlog zavrnitve; če je polje prazno, zavrnitve ni mogoče potrditi.
2. Po potrditvi dobi oglas status »zavrnjen« in izgine s seznama »Oglasi v pregledu«; na seznamu objavljenih oglasov ni nikoli prikazan.
3. Prodajalec na seznamu »Moji oglasi« pri tem oglasu vidi status »zavrnjen« in vpisani razlog.
4. Zavrnjenega oglasa ni mogoče odobriti ali rezervirati; tak zahtevek backend zavrne.

## US-07 – Rezervacija oglasa

> **Kot** kupec **želim** rezervirati objavljen oglas, **da** kompleta pred prevzemom ne more rezervirati drug kupec.

- **Povezana funkcionalnost:** 4 – Rezervacija oglasa
- **Uporabniška vloga:** kupec

Acceptance criteria:

1. Gumb »Rezerviraj« je prikazan samo prijavljenemu kupcu, in sicer pri oglasih s statusom »objavljen« na seznamu objavljenih oglasov in pri ujemajočih oglasih njegovih iskanj.
2. Po rezervaciji dobi oglas status »rezerviran« in ni več prikazan ne na seznamu objavljenih oglasov ne med ujemajočimi oglasi iskanj.
3. Če oglas v trenutku zahtevka nima več statusa »objavljen« (ker ga je medtem rezerviral drug kupec), rezervacija ne uspe in prikaže se sporočilo »Oglas ni več na voljo«.
4. Kupec ne more rezervirati oglasa, ki ga je sam oddal kot prodajalec; tak zahtevek backend zavrne.

## US-08 – Kontakt po rezervaciji

> **Kot** kupec **želim** takoj po rezervaciji dobiti e-poštni naslov prodajalca, **da** se z njim dogovorim za prevzem kompleta.

- **Povezana funkcionalnost:** 4 – Rezervacija oglasa
- **Uporabniška vloga:** kupec

Acceptance criteria:

1. Po uspešni rezervaciji se kupcu prikaže potrditev s podatki oglasa (komplet, stanje, cena) ter z imenom in e-poštnim naslovom prodajalca.
2. Prodajalec na seznamu »Moji oglasi« pri rezerviranem ali prodanem oglasu vidi ime in e-poštni naslov kupca.
3. Pri oglasih s statusom »objavljen« e-poštni naslov prodajalca ni prikazan nikomur.
4. E-poštni naslov kupca je prikazan samo prodajalcu oglasa, ki ga je kupec rezerviral ali kupil.

## US-09 – Potrditev prodaje

> **Kot** prodajalec **želim** po prevzemu kompleta potrditi prodajo, **da** je oglas označen kot prodan in ga nihče več ne more rezervirati.

- **Povezana funkcionalnost:** 5 – Potrditev prodaje ali sprostitev rezervacije
- **Uporabniška vloga:** prodajalec

Acceptance criteria:

1. Gumb »Potrdi prodajo« je na seznamu »Moji oglasi« prikazan samo pri oglasih s statusom »rezerviran«.
2. Po potrditvi dobi oglas status »prodan«.
3. Pri prodanem oglasu ni prikazan noben gumb za dejanje; statusa »prodan« ni mogoče več spremeniti.
4. Prodajo lahko potrdi samo prodajalec, ki je oglas oddal; zahtevek drugega uporabnika, tudi administratorja, backend zavrne.

## US-10 – Sprostitev rezervacije

> **Kot** prodajalec **želim** sprostiti rezervacijo, kadar do prodaje ne pride, **da** lahko komplet rezervira drug kupec.

- **Povezana funkcionalnost:** 5 – Potrditev prodaje ali sprostitev rezervacije
- **Uporabniška vloga:** prodajalec

Acceptance criteria:

1. Gumb »Sprosti rezervacijo« je na seznamu »Moji oglasi« prikazan samo pri oglasih s statusom »rezerviran«.
2. Po sprostitvi dobi oglas status »objavljen« in je znova prikazan na seznamu objavljenih oglasov ter pri iskanjih, ki jim ustreza.
3. Po sprostitvi oglas nima več kupca, zato prodajalec pri njem ne vidi več imena in e-poštnega naslova kupca.
4. Rezervacijo lahko sprosti samo prodajalec, ki je oglas oddal; zahtevek drugega uporabnika backend zavrne.

## US-11 – Zamenjava vloge

> **Kot** kupec ali prodajalec **želim** na svojem profilu zamenjati vlogo, **da** lahko z istim računom kupujem in prodajam.

- **Povezana funkcionalnost:** 6 – Zamenjava vloge na profilu
- **Uporabniška vloga:** kupec, prodajalec

Acceptance criteria:

1. Stran »Profil« prikazuje trenutno vlogo in gumb za zamenjavo v drugo vlogo (iz kupca v prodajalca ali obratno).
2. Po zamenjavi meni takoj prikazuje možnosti nove vloge, brez ponovne prijave.
3. Nova vloga je shranjena v podatkovni bazi, zato velja tudi po odjavi in ponovni prijavi.
4. Vloge ni mogoče zamenjati v »administrator«; tak zahtevek backend zavrne.
5. Administratorju gumb za zamenjavo vloge ni prikazan.

## US-12 – Ohranitev podatkov ob zamenjavi vloge

> **Kot** uporabnik, ki kupuje in prodaja, **želim**, da se ob zamenjavi vloge moji oglasi, rezervacije in iskanja ohranijo, **da** z njimi nadaljujem, ko se vrnem v ustrezno vlogo.

- **Povezana funkcionalnost:** 6 – Zamenjava vloge na profilu
- **Uporabniška vloga:** kupec, prodajalec

Acceptance criteria:

1. Zamenjava vloge ne spremeni statusa nobenega uporabnikovega oglasa, rezervacije ali iskanja.
2. Objavljeni oglasi uporabnika ostanejo na seznamu objavljenih oglasov tudi, ko je ta v vlogi kupca.
3. V vlogi kupca uporabnik strani »Moji oglasi« ne vidi.
4. V vlogi prodajalca uporabnik strani »Moja iskanja« ne vidi.
5. Po vrnitvi v prejšnjo vlogo uporabnik vidi vse svoje oglase oziroma iskanja z nespremenjenimi podatki.

## US-13 – Shranjevanje iskanja

> **Kot** kupec **želim** za komplet, ki ga ne najdem med objavljenimi oglasi, shraniti iskanje z najvišjo ceno in sprejemljivimi stanji, **da** mi rešitev pokaže ustrezen oglas, ko bo objavljen, in mi oglasov ni treba preverjati vsak dan.

- **Povezana funkcionalnost:** 7 – Iskanje kompleta z ujemanjem oglasov
- **Uporabniška vloga:** kupec

Acceptance criteria:

1. Na strani »Moja iskanja« kupec komplet poišče po številki ali imenu in ga izbere iz kataloga; iskanja za komplet, ki ga v katalogu ni, ni mogoče shraniti.
2. Obvezna sta najvišja cena in vsaj eno sprejemljivo stanje (zapečaten, nov, rabljen); sicer se iskanje ne shrani in prikaže se sporočilo o napaki.
3. Če ima kupec za izbrani komplet že aktivno iskanje, se novo ne shrani in prikaže se sporočilo »Za ta komplet že imate aktivno iskanje«.
4. Shranjeno iskanje ima status »aktivno« in je prikazano med aktivnimi iskanji na strani »Moja iskanja«.
5. Iskanje lahko shrani samo uporabnik v vlogi kupca; zahtevek prodajalca ali administratorja backend zavrne.

## US-14 – Ujemajoči oglasi in opozorilo v meniju

> **Kot** kupec **želim** pri vsakem aktivnem iskanju videti oglase, ki mu ustrezajo, in biti nanje opozorjen v meniju, **da** ustrezen komplet rezerviram, preden ga rezervira kdo drug.

- **Povezana funkcionalnost:** 7 – Iskanje kompleta z ujemanjem oglasov
- **Uporabniška vloga:** kupec

Acceptance criteria:

1. Pri vsakem aktivnem iskanju so prikazani vsi ujemajoči oglasi, razvrščeni po ceni od najnižje do najvišje, s stanjem, ceno, imenom prodajalca in gumbom »Rezerviraj«.
2. Oglas se med ujemajočimi prikaže takoj, ko ga administrator odobri ali ko je njegova rezervacija sproščena, in izgine, ko je rezerviran ali umaknjen.
3. Oglas za isti komplet, ki je dražji od najvišje cene, ima stanje, ki ni med sprejemljivimi, ali ga je oddal kupec sam, ni prikazan.
4. V meniju je ob »Moja iskanja« prikazano število aktivnih iskanj, ki imajo vsaj en ujemajoč oglas; če takega iskanja ni, število ni prikazano.
5. Če iskanje nima ujemajočih oglasov, je pri njem prikazano sporočilo »Ni ujemajočih oglasov«.

## US-15 – Pregled in zaključek iskanj

> **Kot** kupec **želim** imeti pregled nad svojimi iskanji in da se iskanje po nakupu samo zaključi, **da** med aktivnimi iskanji vidim samo komplete, ki jih še iščem.

- **Povezana funkcionalnost:** 7 – Iskanje kompleta z ujemanjem oglasov
- **Uporabniška vloga:** kupec

Acceptance criteria:

1. Stran »Moja iskanja« ločeno prikazuje aktivna in izpolnjena iskanja prijavljenega kupca; iskanj drugih kupcev ne prikazuje.
2. Pri vsakem iskanju so prikazani številka in ime kompleta, najvišja cena, sprejemljiva stanja in status.
3. Ko prodajalec potrdi prodajo oglasa za isti komplet temu kupcu, dobi kupčevo aktivno iskanje za ta komplet status »izpolnjeno«, ujemajoči oglasi pa pri njem niso več prikazani.
4. Kupec lahko aktivno iskanje izbriše z gumbom »Izbriši iskanje«; izbrisano iskanje ni več prikazano.
5. Najvišje cene in sprejemljivih stanj iskanja ne vidi nihče razen kupca, ki je iskanje shranil.
