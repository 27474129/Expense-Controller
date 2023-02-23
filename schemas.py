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
            return cursor.fetchone()
