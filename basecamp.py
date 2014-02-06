#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module manages the basecamp api.

Docs: https://github.com/basecamp/bcx-api

"""

import sys
import json
import requests as r


class Basecamp(object):
    def __init__(self, account, user, password, agent):
        self.account = account
        self.user = user
        self.password = password
        self.basepath = 'https://basecamp.com/{0}/api/v1'.format(self.account)
        self.agent = agent

    def __makeRequest(self, path, method='get', payload=None):
        ''' Request handler '''

        # TO-DO
        # Implement Etag/If-None-Match

        endpoint = self.basepath + path

        auth = (self.user, self.password)

        headers = {
            'User-Agent': self.agent,
            'Content-Type': 'application/json'
        }

        if payload:
            data = json.dumps(payload)
        else:
            data = payload

        requestMethod = getattr(r, method)

        try:
            request = requestMethod(endpoint, auth=auth, data=data,
                                headers=headers)
        except r.exceptions.RequestException as e:
            print e
            sys.exit(1)

        if request.status_code in [200, 201, 304]:
            return (request.json(), request.headers)

        return request.status_code

    def getProjects(self):
        '''Returns all active projects'''

        path = '/projects.json'
        return self.__makeRequest(path)

    def getArchivedProjects(self):
        '''Returns all archived projects'''

        path = '/projects/archived.json'
        return self.__makeRequest(path)

    def getProject(self, id):
        '''Returns single project'''

        path = '/projects/{0}.json'.format(id)
        return self.__makeRequest(path)

    def createProject(self, payload):
        '''Creates a project'''

        path = '/projects.json'
        return self.__makeRequest(path, 'post', payload)

    def updateProject(self, id, payload):
        '''Updates a project'''

        path = '/projects/{0}.json'.format(id)
        return self.__makeRequest(path, 'put', payload)