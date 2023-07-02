from sqlalchemy import create_engine, text
from bootstrap import app
from exts import db
from seed import seed
from common.constants import *

sqlalchemy_init()
# initiate DB

app.app_context().push()
seed(db)
