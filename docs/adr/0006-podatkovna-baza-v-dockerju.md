# PostgreSQL v Dockerjevem zabojniku za lokalni razvoj

## Kontekst in problem

PostgreSQL (ADR-0005) mora teči na vsakem računalniku, na katerem se rešitev razvija ali preizkuša. Shema baze naj se ustvari brez ročnih korakov. Odločiti se je treba, kako se baza zažene lokalno.

## Obravnavane možnosti

* PostgreSQL v Dockerjevem zabojniku, zagnan z Docker Compose
* PostgreSQL, nameščen neposredno v operacijski sistem
* Podatkovna baza v oblaku

## Odločitev

Izbrana možnost: »PostgreSQL v Dockerjevem zabojniku«, ker se baza z ukazom `docker compose up -d` na vsakem računalniku zažene v enaki različici in z enakimi nastavitvami, datoteka SQL s shemo pa se ob prvem zagonu izvede samodejno.

### Posledice

* Dobro, ker PostgreSQL ni treba nameščati in nastavljati v operacijskem sistemu.
* Dobro, ker je različica baze zapisana v datoteki Docker Compose in je zato enaka pri vseh razvijalcih.
* Dobro, ker je razvojno bazo mogoče hitro izbrisati in ustvariti na novo (`docker compose down -v`).
* Slabo, ker je potreben Docker Desktop, ki porabi dodaten pomnilnik.
* Slabo, ker se datoteka s shemo izvede samo ob prvem zagonu, zato je treba ob spremembi sheme razvojno bazo izbrisati in podatke znova naložiti s skripto za začetne podatke.
