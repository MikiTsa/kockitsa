# Ena aktivna vloga na uporabniški račun

## Kontekst in problem

Rešitev ima tri vloge: kupca, prodajalca in administratorja. Isti človek pogosto kupuje in prodaja. Vsaka končna točka API mora vedeti, katera dejanja so uporabniku dovoljena. Odločiti se je treba, koliko vlog ima lahko en račun in kako se preverjajo.

## Obravnavane možnosti

* Ena aktivna vloga na račun, kupec in prodajalec jo zamenjata na profilu
* Več hkratnih vlog na račun (dodatna tabela vlog uporabnika)
* Ločen račun za vsako vlogo

## Odločitev

Izbrana možnost: »Ena aktivna vloga na račun«, ker je preverjanje pravic preprosto (končna točka primerja vlogo iz seje z zahtevano vlogo), uporabnik, ki želi kupovati in prodajati, pa vseeno potrebuje samo en račun. Vloga je shranjena v polju `users.role`; oglasi, rezervacije in iskanja so vezani na uporabnika, ne na vlogo, zato se ob zamenjavi ohranijo.

### Posledice

* Dobro, ker uporabnik vidi samo meni in možnosti trenutne vloge, kar zmanjša zmedo v uporabniškem vmesniku.
* Dobro, ker podatkovni model ne potrebuje dodatne tabele vlog.
* Slabo, ker mora uporabnik, ki kupuje in prodaja, za vsako dejanje najprej zamenjati vlogo.
* Slabo, ker mora backend posebej preprečiti, da bi kupec rezerviral oglas, ki ga je sam oddal kot prodajalec.
* Slabo, ker bi poznejša podpora več hkratnim vlogam zahtevala spremembo modela in preverjanja pravic.
