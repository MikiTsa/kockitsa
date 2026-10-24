# Backend v ogrodju FastAPI

## Kontekst in problem

Backend ponuja REST API (ADR-0001), preverja prijavo in vlogo uporabnika ter pravila delovnih procesov in dostopa do podatkovne baze. Odločiti se je treba, v katerem ogrodju bo napisan.

## Obravnavane možnosti

* FastAPI (Python)
* Flask (Python)
* Django z Django REST Framework (Python)
* Express (Node.js)

## Odločitev

Izbrana možnost: »FastAPI«, ker je za REST API potrebne malo kode, vhodne podatke samodejno preveri po opisanih modelih in na naslovu `/docs` samodejno ponudi dokumentacijo API, s katero je mogoče končne točke preizkusiti brez frontenda.

### Posledice

* Dobro, ker FastAPI napačne vhodne podatke (na primer manjkajočo ceno) zavrne sam, še preden se izvede koda končne točke.
* Dobro, ker se dokumentacija API ustvari iz kode in je zato vedno usklajena s končnimi točkami.
* Dobro, ker ogrodje ne vsiljuje ORM ali strukture projekta, zato ostane backend majhen (glej ADR-0004).
* Slabo, ker za razliko od ogrodja Django nima vgrajenega upravljanja uporabnikov, administratorskega vmesnika in migracij; prijavo je treba napisati sami (ADR-0007).
* Slabo, ker je treba za podpisan piškotek seje uporabiti vmesno programsko opremo iz ogrodja Starlette, na katerem FastAPI temelji.
