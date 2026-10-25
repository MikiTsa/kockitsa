# Poizvedbe SQL s knjižnico psycopg brez ORM

## Kontekst in problem

Backend bere in zapisuje podatke v štiri tabele (`users`, `sets`, `listings`, `searches`). Najzahtevnejša poizvedba poišče oglase, ki ustrezajo iskanju (isti komplet, status `approved`, cena in stanje v mejah iskanja). Odločiti se je treba, ali backend do baze dostopa prek ORM ali z neposrednimi poizvedbami SQL.

## Obravnavane možnosti

* Poizvedbe SQL s knjižnico psycopg (različica 3)
* ORM SQLAlchemy
* SQLModel (ORM na osnovi SQLAlchemy in Pydantic)

## Odločitev

Izbrana možnost: »Poizvedbe SQL s knjižnico psycopg«, ker ima model samo štiri tabele in so poizvedbe kratke, zato dodaten sloj ne prinese dovolj koristi. Poizvedba za ujemanje uporablja polje tipa `text[]` (`condition = ANY(conditions)`), ki je v SQL zapisana neposredno.

### Posledice

* Dobro, ker je v kodi vidno, katera poizvedba SQL se izvede, kar olajša razumevanje in iskanje napak.
* Dobro, ker psycopg vrednosti pošlje kot parametre poizvedbe, zato vnosi uporabnikov ne morejo spremeniti poizvedbe (napad SQL injection).
* Slabo, ker je treba vrstice iz baze ročno pretvoriti v odgovore JSON.
* Slabo, ker ni samodejnih migracij; ob spremembi sheme je treba popraviti datoteko SQL in vse poizvedbe, ki uporabljajo spremenjeno tabelo.
