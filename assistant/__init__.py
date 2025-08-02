import logging

from config import *
from git import Repo
from pyAyiin import PyrogramXd
from pyAyiin.Clients import *
from pyAyiin.config import Var


repo = Repo()
branch = repo.active_branch
yins = PyrogramXd()
var = Var()

logs = logging.getLogger(__name__)
