import os, socket, time


def is_database_available(database_host, database_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock.connect_ex((database_host, database_port)) == 0


def wait_for_database(database_host, database_port, retry_limit_seconds=60):
    """ Waits for the database to become available. """
    """ TODO: Use logging instead of print functions. """
    for attempt in range(0, retry_limit_seconds - 1):
        if is_database_available(database_host, database_port):
            return True

        print("Waiting for DB at %s:%d (attempt %d of %d)" % (database_host, database_port, attempt,
                                                              retry_limit_seconds))
        time.sleep(1)

    return False
