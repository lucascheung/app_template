# common configs
import os, sys, traceback
from server.config import config_dev, config_prod
from server.common.constants import *

IS_DEV = os.environ.get("ENV", "dev") == "dev"
CONF = config_dev if IS_DEV else config_prod








