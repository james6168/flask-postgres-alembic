from psycopg2 import OperationalError, connect
from time import sleep
from logging import getLogger


logger = getLogger("postgres")


def is_postgres_healthy(
    db_connection_string: str,
    retries=5,
    delay=2,
):
    for attempt in range(1, retries + 1):
        try:
            conn = connect(
                dsn=db_connection_string,
                connect_timeout=3
            )
            conn.close()
            logger.info(f"[✓] PostgreSQL is available (attempt {attempt})")
            return True
        except OperationalError as e:
            logger.info(f"[!] Connection error (attempt {attempt}): {e}")
            sleep(delay)

    logger.info("[✗] PostgreSQL is not avialable after all attempts")
    return False