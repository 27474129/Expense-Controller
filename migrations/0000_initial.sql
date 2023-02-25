CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_active BOOL DEFAULT FALSE
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name VARCHAR(50) NOT NULL,
    amount_limit INTEGER NOT NULL,
    current_amount FLOAT DEFAULT 0,
    time_distance INTEGER NOT NULL,
    CONSTRAINT user_fk
        FOREIGN KEY(user_id)
        REFERENCES users(id)
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    category_id INTEGER,
    amount FLOAT,
    moment TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT user_fk
        FOREIGN KEY(user_id)
        REFERENCES users(id),
    CONSTRAINT category_fk
        FOREIGN KEY(category_id)
        REFERENCES categories(id)
);