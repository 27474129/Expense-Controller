INSERT INTO users (email, password)
VALUES ('harlanvova03@gmail.com', 'Harlan483');

INSERT INTO users (email, password)
VALUES ('adasdasdsd@mail.com', '234r234');

INSERT INTO users (email, password, is_active)
VALUES ('123@yandex.com', '123', TRUE);

INSERT INTO users (email, password)
VALUES ('53453@yandex.com', '543345');

INSERT INTO users (email, password, is_active)
VALUES ('532@asd.com', '5423', TRUE);



INSERT INTO categories (user_id, name, amount_limit, time_distance)
VALUES (1, 'food', 5000, 7);

INSERT INTO categories (user_id, name, amount_limit, time_distance)
VALUES (1, 'weekend', 3000, 7);

INSERT INTO categories (user_id, name, amount_limit, time_distance)
VALUES (2, 'food', 45000, 30);

INSERT INTO categories (user_id, name, amount_limit, time_distance)
VALUES (2, 'weekends', 10000, 30);

INSERT INTO categories (user_id, name, amount_limit, time_distance)
VALUES (2, 'other', 2000, 30);



INSERT INTO expenses (user_id, category_id, amount)
VALUES (1, 1, 100);

INSERT INTO expenses (user_id, category_id, amount)
VALUES (2, 2, 43);

INSERT INTO expenses (user_id, category_id, amount)
VALUES (3, 3, 200);

INSERT INTO expenses (user_id, category_id, amount)
VALUES (4, 4, 43);

INSERT INTO expenses (user_id, category_id, amount)
VALUES (1, 4, 54);