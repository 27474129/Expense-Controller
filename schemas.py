from pydantic import BaseModel

from postgresql import PostgresqlConnection


class Users(BaseModel):
    email: str
    password: str

    @staticmethod
    def create_user(email: str, password: str) -> None:
        query = f"""
        INSERT INTO users (email, password) 
        VALUES ('{email}', '{password}');
        """

        with PostgresqlConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

    @staticmethod
    def check_user_data(email: str, password: str) -> int:
        query = f"""
        SELECT id
        FROM users
        WHERE 1=1 
            AND email = '{email}'
            AND password = '{password}';
        """

        with PostgresqlConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

            # Returning user_id for create jwt token in future
            return cursor.fetchone()[0]


class Categories(BaseModel):
    user_id: int = None
    name: str
    amount_limit: int
    current_amount: float = None
    time_distance: int

    @staticmethod
    def create_category(
        user_id: int, name: str, amount_limit: int, time_distance: int
    ):
        query = f"""
        INSERT INTO categories (user_id, name, amount_limit, time_distance)
        VALUES ({user_id}, '{name}', {amount_limit}, {time_distance});
        """

        with PostgresqlConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

    @staticmethod
    def find_category_by_name(name: str, user_id: int):
        query = f"""
        SELECT user_id
        FROM categories
        WHERE 1=1
            AND name = '{name}'
            AND user_id = {user_id};
        """

        with PostgresqlConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

            # Returning user_id for create jwt token in future
            return cursor.fetchone()
