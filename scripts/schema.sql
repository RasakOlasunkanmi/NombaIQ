CREATE TABLE IF NOT EXISTS merchants (
    merchant_id     VARCHAR PRIMARY KEY,
    business_name   VARCHAR,
    business_type   VARCHAR,
    state           VARCHAR,
    registered_at   TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id  VARCHAR PRIMARY KEY,
    merchant_id     VARCHAR REFERENCES merchants(merchant_id),
    amount_ngn      DECIMAL(15, 2),
    type            VARCHAR,
    category        VARCHAR,
    channel         VARCHAR,
    narration       TEXT,
    timestamp       TIMESTAMP,
    raw_payload     JSONB,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_txn_merchant   ON transactions(merchant_id);
CREATE INDEX IF NOT EXISTS idx_txn_timestamp  ON transactions(timestamp);
CREATE INDEX IF NOT EXISTS idx_txn_type       ON transactions(type);

INSERT INTO merchants (merchant_id, business_name, business_type, state)
VALUES ('DEMO_001', 'Mama Titi Kitchen', 'food_hospitality', 'Lagos')
ON CONFLICT DO NOTHING;

SELECT * FROM merchants;