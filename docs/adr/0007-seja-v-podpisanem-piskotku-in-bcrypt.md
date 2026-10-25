# Prijava z e-pošto in geslom, gesla z bcrypt, seja v podpisanem piškotku

## Kontekst in problem

Rešitev potrebuje registracijo, prijavo in odjavo ter preverjanje vloge pri vsakem zahtevku. Gesla ne smejo biti shranjena v berljivi obliki. Odločiti se je treba, kako backend ve, kateri uporabnik pošilja zahtevek, in kako hrani gesla.

## Obravnavane možnosti

* Seja v podpisanem piškotku (SessionMiddleware iz ogrodja Starlette) in gesla, zgoščena z bcrypt
* Žeton JWT, ki ga frontend hrani v brskalniku in pošilja v glavi zahtevka
* Zunanji ponudnik prijave (na primer Google ali Auth0)

## Odločitev

Izbrana možnost: »Seja v podpisanem piškotku in bcrypt«, ker rešitev ne potrebuje zunanje storitve, brskalnik piškotek pošlje z vsakim zahtevkom sam in, ker backend streže tudi frontend (ADR-0001), piškotek deluje brez dodatnih nastavitev. Bcrypt je namenjen zgoščevanju gesel: je namenoma počasen in vsakemu geslu doda naključno sol.

### Posledice

* Dobro, ker frontendu ni treba hraniti žetona in ga dodajati k zahtevkom.
* Dobro, ker uporabnik vsebine piškotka (oznaka uporabnika in vloga) ne more spremeniti, ne da bi backend to zaznal, saj je piškotek podpisan s skrivnim ključem.
* Dobro, ker iz ukradene baze ni mogoče neposredno prebrati gesel.
* Slabo, ker je piškotek samo podpisan, ne šifriran, zato vanj ne smemo zapisati zaupnih podatkov.
* Slabo, ker seja ni shranjena na strežniku in je ni mogoče preklicati drugače kot z odjavo ali menjavo skrivnega ključa.
* Slabo, ker mora backend ob zamenjavi vloge posodobiti tudi vlogo v seji, ne samo v bazi.
