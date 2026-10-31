CREATE TABLE users (
    id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name          TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL CHECK (role IN ('buyer', 'seller', 'admin'))
);

CREATE TABLE sets (
    id           BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    set_number   TEXT NOT NULL UNIQUE,
    name         TEXT NOT NULL,
    theme        TEXT NOT NULL,
    piece_count  INTEGER NOT NULL,
    release_year INTEGER NOT NULL
);

CREATE TABLE listings (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    set_id           BIGINT NOT NULL REFERENCES sets (id),
    seller_id        BIGINT NOT NULL REFERENCES users (id),
    buyer_id         BIGINT REFERENCES users (id),
    condition        TEXT NOT NULL CHECK (condition IN ('sealed', 'new', 'used')),
    price            NUMERIC(10, 2) NOT NULL CHECK (price > 0),
    description      TEXT,
    status           TEXT NOT NULL DEFAULT 'pending'
                     CHECK (status IN ('pending', 'approved', 'rejected', 'reserved', 'sold')),
    rejection_reason TEXT,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE searches (
    id         BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    buyer_id   BIGINT NOT NULL REFERENCES users (id),
    set_id     BIGINT NOT NULL REFERENCES sets (id),
    max_price  NUMERIC(10, 2) NOT NULL CHECK (max_price > 0),
    conditions TEXT[] NOT NULL
               CHECK (cardinality(conditions) > 0 AND conditions <@ ARRAY['sealed', 'new', 'used']),
    status     TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'fulfilled')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX searches_one_active_per_set ON searches (buyer_id, set_id) WHERE status = 'active';
