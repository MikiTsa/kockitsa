# Pravila delovnih procesov preverja backend

## Kontekst in problem

Oglas prehaja med statusi (`pending`, `approved`, `rejected`, `reserved`, `sold`), iskanje pa se zaključi, ko prodajalec potrdi prodajo kompleta kupcu, ki je iskanje shranil. Vsak prehod lahko izvede samo določena vloga in samo iz določenega statusa. Odločiti se je treba, kje se ta pravila preverjajo.

## Obravnavane možnosti

* Pravila preverja backend v končnih točkah API
* Pravila preverja frontend (gumbi se prikažejo samo, ko je dejanje dovoljeno)
* Pravila preverja podatkovna baza s prožilci (triggers)

## Odločitev

Izbrana možnost: »Pravila preverja backend«, ker je zahtevke mogoče poslati tudi mimo frontenda (na primer prek dokumentacije API ali orodja za zahtevke HTTP), zato preverjanje samo v frontendu ne zadošča. Backend ob vsakem prehodu preveri vlogo, lastništvo in trenutni status, frontend pa gumbe le skrije, kadar dejanje ni dovoljeno.

### Posledice

* Dobro, ker so vsa pravila na enem mestu, v kodi Python, ki jo je mogoče preizkusiti s testi.
* Dobro, ker rezervacija uspe samo, če ima oglas v trenutku zahtevka še status `approved`, zato dva kupca istega oglasa ne moreta rezervirati.
* Dobro, ker se ujemanje oglasov z iskanji izračuna ob vsakem prikazu iz tabele `listings`, zato ni podvojenih podatkov, ki bi jih bilo treba usklajevati.
* Slabo, ker mora frontend pravila delno ponoviti (kdaj prikazati gumb), zato je treba ob spremembi pravila popraviti oba dela.
* Slabo, ker baza sama ne prepreči napačnega prehoda statusa, če bi backend vseboval napako; omejitve v bazi (ADR-0005) preverijo samo veljavne vrednosti statusa.
