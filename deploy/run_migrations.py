import os
from typing import List

from postgresql import PostgresqlConnection


def get_migrations_ids(migrations_count: int) -> List[str]:
    migrations_ids = []
    for id in range(0, migrations_count + 1):
        id = str(id)
        while len(id) != 4:
            id = f'0{id}'
        migrations_ids.append(id)

    return migrations_ids


def read_and_run_migration(migration: str, cursor):
    with open(f'migrations/{migration}') as sql_script:
        commands = sql_script.read().split(';')
        for command in commands:
            if command:
                cursor.execute(command)


def run_migrations():
    migrations = os.listdir('migrations')
    with PostgresqlConnection() as connection:
        cursor = connection.cursor()
        migrations_ids = get_migrations_ids(len(migrations))

        for migration_id in migrations_ids:
            for migration in migrations:
                if migration[:4] == migration_id:
                    read_and_run_migration(migration, cursor)


if __name__ == '__main__':
    run_migrations()
