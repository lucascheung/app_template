# for db
import pdb
from sqlalchemy import event

from server.exts import db
from server.config.config import IS_DEV
from server.seed import seed

def init_db(app):
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        if IS_DEV:
            seed(db) 