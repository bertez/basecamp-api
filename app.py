#!/usr/bin/python
# -*- coding: utf-8 -*-

from basecamp import Basecamp

#config, check this for docs: https://github.com/basecamp/bcx-api
account = ''
user = ''
password = ''
user_agent = ''

#development config
try:
    from dev_config import *
except ImportError:
    pass

bc = Basecamp(account, user, password, user_agent)

projects = bc.getProjects()

print bc.prettyPrint(projects)
