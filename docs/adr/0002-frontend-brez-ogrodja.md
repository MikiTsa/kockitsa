# Frontend v HTML in JavaScriptu brez ogrodja

## Kontekst in problem

Frontend ima malo strani (objavljeni oglasi, oddaja oglasa, moji oglasi, oglasi v pregledu, moja iskanja, profil, prijava in registracija). Vsaka stran podatke pridobi iz REST API (ADR-0001) in jih prikaže. Odločiti se je treba, ali za frontend uporabiti ogrodje.

## Obravnavane možnosti

* HTML, CSS in JavaScript brez ogrodja (vgrajena funkcija `fetch`)
* React
* Vue.js

## Odločitev

Izbrana možnost: »HTML, CSS in JavaScript brez ogrodja«, ker rešitev nima zahtevnega uporabniškega vmesnika, ki bi upravičil ogrodje. Brez ogrodja ni koraka gradnje in ni orodij Node.js, backend pa datoteke frontenda streže neposredno.

### Posledice

* Dobro, ker frontend ne potrebuje namestitve paketov in koraka gradnje; za lokalni zagon zadošča backend.
* Dobro, ker je koda lažje razumljiva razvijalcu, ki ogrodja ne pozna.
* Slabo, ker je treba posodabljanje strani (DOM) pisati ročno.
* Slabo, ker ni komponent, zato se deli strani, kot je meni, ponavljajo ali pa jih je treba vstaviti z lastno funkcijo.
* Slabo, ker bi ob večji rasti uporabniškega vmesnika prehod na ogrodje pomenil ponovno pisanje frontenda.
