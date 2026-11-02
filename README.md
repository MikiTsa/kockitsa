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
- `db/` – shema podatkovne baze
- `seed/` – skripta za začetne podatke (katalog kompletov iz Brickset API, administratorski račun)
- `docs/` – projektna dokumentacija

## Lokalni zagon

Potrebni so Docker Desktop, Python 3.13 in brezplačen ključ za [Brickset API](https://brickset.com/tools/webservices/requestkey). Ukazi so za PowerShell in se izvedejo v korenu repozitorija.

1. Kopirajte `.env.example` v `.env` in izpolnite vrednosti:
   ```
   copy .env.example .env
   ```
   - `POSTGRES_PASSWORD` – poljubno geslo podatkovne baze; isto geslo vpišite namesto `<geslo>` v `DATABASE_URL`.
   - `BRICKSET_API_KEY` – ključ za Brickset API.
   - `ADMIN_EMAIL`, `ADMIN_PASSWORD` – administratorski račun, ki ga ustvari skripta za začetne podatke.
   - `SECRET_KEY` – poljuben dolg naključen niz, s katerim backend podpisuje piškotek seje.
2. Zaženite podatkovno bazo. Ob prvem zagonu se izvede `db/schema.sql`, ki ustvari tabele:
   ```
   docker compose up -d
   ```
3. Ustvarite virtualno okolje in namestite knjižnice:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Napolnite katalog kompletov in ustvarite administratorski račun (če se baza še zaganja, ukaz po nekaj sekundah ponovite):
   ```
   python seed/seed.py
   ```
5. Zaženite backend, ki streže tudi frontend:
   ```
   uvicorn backend.main:app --reload
   ```
6. Odprite `http://127.0.0.1:8000`.

Ob spremembi `db/schema.sql` bazo izbrišite in ustvarite na novo: `docker compose down -v`, nato koraka 2 in 4.

## Dokumentacija

1. [Zasnova rešitve](docs/01-zasnova-resitve.md)
2. [Funkcionalnosti in obseg](docs/02-funkcionalnosti-in-obseg.md)
3. [Podatkovni model](docs/03-podatkovni-model.md)
4. [Arhitektura in tehnološki sklad](docs/04-arhitektura-in-tehnoloski-sklad.md)
5. [Uporabniške zgodbe](docs/05-uporabniske-zgodbe.md)
6. [Wireframes](docs/06-wireframes.md)
7. [Arhitekturne odločitve (ADR)](docs/adr/)
