#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
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

#API test

#Projects

# response = bc.getProjects()
# response = bc.getArchivedProjects()
# response = bc.getProject(5007093)

# new_project = {
# 	'name': 'This is a test project. Do not delete.',
# 	'description': 'Created using the API'
# }

# response = bc.createProject(new_project)

# edit_project = {
# 	'name': 'Do not delete me, please'
# }

# response = bc.updateProject(5007093, edit_project)

# response = bc.deleteProject(5007093)+

#People

# response = bc.getPeople()
# response = bc.getMe()
response = bc.getPerson(1546238)

if response[0]:
	# check if the response is json
	try:
		output = json.loads(response[1])
		print json.dumps(output, indent=4, sort_keys=True)
	except ValueError:
		print response[0]
else:
	print 'Failed'