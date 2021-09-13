import time

from sqlalchemy.exc import OperationalError

def wait_for_db(db):
    print('Waiting for db...')
    tries = 0
    db_connection = False
    while db_connection is False:
        try:
            db.session.execute('SELECT 1')
            print("connected")
            db_connection = True
        except OperationalError:
            tries += 1
            time.sleep(3)
