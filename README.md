# KockiTsa

KockiTsa je spletna tržnica, na kateri posamezniki prodajajo in kupujejo nove in rabljene LEGO komplete. Vsak oglas je vezan na komplet iz kataloga in ga pred objavo pregleda administrator. Kupec objavljen oglas rezervira, prodajalec po prevzemu potrdi prodajo. Kupec lahko shrani iskanje kompleta z najvišjo ceno in sprejemljivimi stanji, rešitev pa mu pokaže oglase, ki iskanju ustrezajo.

Vloge: kupec, prodajalec, administrator.

## Tehnologije

| Del | Tehnologije |
|---|---|
| Frontend | HTML, CSS, JavaScript (brez ogrodja) |
| Backend | Python, FastAPI, Uvicorn, psycopg3 |
| Podatkovna baza | PostgreSQL (Docker, Docker Compose) |
| Avtentikacija | e-pošta in geslo, bcrypt, seja v podpisanem piškotku |

## Struktura repozitorija

- `frontend/` – strani HTML in JavaScript
- `backend/` – aplikacija FastAPI
- `docs/` – projektna dokumentacija

## Dokumentacija

1. [Zasnova rešitve](docs/01-zasnova-resitve.md)
2. [Funkcionalnosti in obseg](docs/02-funkcionalnosti-in-obseg.md)
3. [Podatkovni model](docs/03-podatkovni-model.md)
4. [Arhitektura in tehnološki sklad](docs/04-arhitektura-in-tehnoloski-sklad.md)
5. [Uporabniške zgodbe](docs/05-uporabniske-zgodbe.md)
6. [Wireframes](docs/06-wireframes.md)
7. [Arhitekturne odločitve (ADR)](docs/adr/)
