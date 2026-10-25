# Relacijska podatkovna baza PostgreSQL

## Kontekst in problem

Podatki rešitve so med seboj povezani: oglas pripada kompletu, prodajalcu in morebitnemu kupcu, iskanje pripada kupcu in kompletu. Statusi oglasov in iskanj morajo biti vedno veljavni, kupec pa ima za isti komplet največ eno aktivno iskanje. Odločiti se je treba, katera podatkovna baza hrani te podatke.

## Obravnavane možnosti

* PostgreSQL
* MySQL
* SQLite
* MongoDB

## Odločitev

Izbrana možnost: »PostgreSQL«, ker je relacijska baza s tujimi ključi in omejitvami primerna za povezane podatke, poleg tega pa podpira tip `text[]` (sprejemljiva stanja iskanja) in delne enolične indekse, s katerimi baza sama prepreči drugo aktivno iskanje za isti komplet.

### Posledice

* Dobro, ker tuji ključi in omejitve `CHECK` preprečijo neveljavne povezave in statuse tudi, če bi backend vseboval napako.
* Dobro, ker pravilo »največ eno aktivno iskanje na komplet« velja v bazi z enoličnim indeksom nad `buyer_id` in `set_id` za vrstice s statusom `active`.
* Dobro, ker PostgreSQL zanesljivo obravnava hkratne zahtevke, na primer ko dva kupca hkrati rezervirata isti oglas.
* Slabo, ker mora baza teči kot ločen strežnik; za razliko od SQLite ni le datoteka (rešeno z ADR-0006).
* Slabo, ker tip `text[]` in delni indeksi niso del vseh baz SQL, zato bi bil prehod na drugo bazo zahtevnejši.
