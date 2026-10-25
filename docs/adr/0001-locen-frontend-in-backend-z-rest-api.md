# Ločen frontend in backend, povezana prek REST API

## Kontekst in problem

KockiTsa ima uporabniški vmesnik v brskalniku in strežniški del, ki preverja pravila delovnih procesov (prehodi med statusi oglasa, ujemanje oglasov z iskanji) in dostopa do podatkovne baze. Odločiti se je treba, kako sta ta dva dela povezana: ali strežnik sam sestavlja strani HTML ali pa brskalnik podatke pridobi prek API in jih prikaže sam.

## Obravnavane možnosti

* Ločen frontend (HTML in JavaScript) in backend z REST API (JSON)
* Strani HTML, ki jih sestavi strežnik s predlogami (na primer Jinja2), brez ločenega API
* Aplikacija z enim ogrodjem za oba dela (na primer Django s predlogami)

## Odločitev

Izbrana možnost: »Ločen frontend in backend z REST API«, ker je meja med prikazom in poslovnimi pravili jasna: vsa pravila so v končnih točkah API, frontend pa samo prikazuje podatke in pošilja vnose. Backend datoteke frontenda tudi streže, zato sta oba dela na istem naslovu.

### Posledice

* Dobro, ker je mogoče frontend kasneje zamenjati ali dodati drugega odjemalca (na primer mobilno aplikacijo), ne da bi spreminjali backend.
* Dobro, ker je API mogoče preizkusiti neodvisno od frontenda (na primer prek samodejne dokumentacije, glej ADR-0003).
* Dobro, ker frontend in backend tečeta na istem naslovu, zato nastavitve CORS niso potrebne.
* Slabo, ker mora frontend sam pridobiti podatke in sestaviti stran, kar pomeni več kode JavaScript kot pri strežniških predlogah.
* Slabo, ker je treba za vsako dejanje določiti in vzdrževati končno točko API in obliko podatkov JSON.
