import psycopg2
import psycopg2.extras
import logging
import config

log = logging.getLogger('app')

class DBConnection:
    def __init__(self):
        self.db_name = config.db_name
        self.user = config.postgres_username
        self.host = config.postgres_host
        self.password = config.postgres_password

    def connect(self):
        """Connect to the database.

        Returns a cursor and a connection object.
        """
        connect_str = "user=%s password=%s host=%s" % (
            self.user, self.password, self.host)
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        logging.info('Successfully connected to the database')
        return cursor, conn
