from sqlalchemy import create_engine, text
from server.bootstrap import app
from server.exts import db
from server.seed import seed
from server.common.constants import *

sqlalchemy_init()
# initiate DB

app.app_context().push()
seed(db)
