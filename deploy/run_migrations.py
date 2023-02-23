import os

from postgresql import PostgresqlConnection


def run_migrations():
    migrations = os.listdir('migrations')
    with PostgresqlConnection() as connection:
        cursor = connection.cursor()
        for migration in migrations:
            with open(f'migrations/{migration}') as sql_script:
                commands = sql_script.read().split(';')
                for command in commands:
                    cursor.execute(command)


if __name__ == '__main__':
    run_migrations()
