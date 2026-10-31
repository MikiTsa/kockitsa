# Katalog kompletov iz Brickset API

## Kontekst in problem

Vsak oglas in vsako iskanje je vezano na komplet iz kataloga (tabela `sets`: številka, ime, tema, število kock, leto izdaje). Upravljanje kataloga (funkcionalnost 12) ni del MVP, zato katalog napolni skripta za začetne podatke. Odločiti se je treba, od kod skripta dobi podatke o kompletih.

## Obravnavane možnosti

* Skripta prenese komplete iz Brickset API
* Skripta vsebuje ročno vpisan seznam kompletov
* Skripta uvozi datoteko CSV s kompleti, preneseno s spletne strani Rebrickable

## Odločitev

Izbrana možnost: »Skripta prenese komplete iz Brickset API«, ker vrne resnične komplete z vsemi polji, ki jih potrebuje tabela `sets`, brez ročnega vnosa in brez datoteke v repozitoriju. Skripta izbere 100 kompletov, izdanih od leta 2020 naprej, ki imajo podano število kock in maloprodajno ceno.

### Posledice

* Dobro, ker katalog vsebuje resnične komplete, zato je rešitev med preizkušanjem podobna pravi tržnici.
* Dobro, ker je skripta kratka in podatkov ni treba vzdrževati ročno.
* Slabo, ker sta za lokalni zagon potrebna brezplačen ključ za Brickset API in internetna povezava.
* Slabo, ker skripta komplete izbere naključno, zato se katalog na različnih računalnikih razlikuje.
