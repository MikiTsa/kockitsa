import json
import os
import urllib.parse
import urllib.request

import bcrypt
import psycopg
from dotenv import load_dotenv

N_SETS = 100

load_dotenv()

query = urllib.parse.urlencode({
    "apiKey": os.environ["BRICKSET_API_KEY"],
    "userHash": "",
    "params": json.dumps({"year": "2020,2021,2022,2023,2024,2025",
                          "orderBy": "Random", "pageSize": 500}),
})
with urllib.request.urlopen(f"https://brickset.com/api/v3.asmx/getSets?{query}") as response:
    data = json.load(response)
if data["status"] != "success":
    raise SystemExit(f"Brickset error: {data.get('message')}")

brickset = [s for s in data["sets"]
            if s.get("pieces") and s.get("LEGOCom", {}).get("DE", {}).get("retailPrice")][:N_SETS]

sets = [(f"{s['number']}-{s['numberVariant']}", s["name"], s["theme"], s["pieces"], s["year"])
        for s in brickset]

password_hash = bcrypt.hashpw(os.environ["ADMIN_PASSWORD"].encode(), bcrypt.gensalt()).decode()

with psycopg.connect(os.environ["DATABASE_URL"]) as conn, conn.cursor() as cur:
    cur.executemany(
        "INSERT INTO sets (set_number, name, theme, piece_count, release_year) "
        "VALUES (%s, %s, %s, %s, %s) "
        "ON CONFLICT (set_number) DO NOTHING",
        sets,
    )
    cur.execute(
        "INSERT INTO users (name, email, password_hash, role) "
        "VALUES ('Administrator', %s, %s, 'admin') "
        "ON CONFLICT (email) DO NOTHING",
        (os.environ["ADMIN_EMAIL"], password_hash),
    )

print(f"Seeded {len(sets)} sets and the admin account {os.environ['ADMIN_EMAIL']}")
