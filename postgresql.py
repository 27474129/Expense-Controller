import psycopg2
import logging

from config import PostgresqlConfig


logger = logging.getLogger(__name__)


class PostgresqlConnection(object):
    __slots__ = ["connection"]

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                f"dbname={PostgresqlConfig.database} "
                f"user={PostgresqlConfig.username} "
                f"password={PostgresqlConfig.password} "
                f"host={PostgresqlConfig.host} "
                f"port={PostgresqlConfig.port}"
            )
            logger.info(f"{PostgresqlConfig.prefix}: "
                        f"successfully connected to postgres")
        except Exception as e:
            logger.error(e)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        logger.info(f'{PostgresqlConfig.prefix}: connection refused')
