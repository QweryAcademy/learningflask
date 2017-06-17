from src.settings.local import *
TESTING=True
database = os.path.join(BASE_DIR, "test.db")
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(database)
