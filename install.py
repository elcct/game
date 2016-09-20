from database.base import init_db, db_session

# initialize our database
init_db()

db_session.commit()
