#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module manages the basecamp api.

Docs: https://github.com/basecamp/bcx-api

"""

import requests as r
import json


class Basecamp(object):
    def __init__(self, account, user, password, agent):
        self.account = account
        self.user = user
        self.password = password
        self.basepath = 'https://basecamp.com/{0}/api/v1'.format(self.account)
        self.agent = agent

    #helper methods
    def prettyPrint(self, string):
        parsed = json.loads(string)
        return json.dumps(parsed, indent=4, sort_keys=True)

    def __makeRequest(self, path, method='get', payload=None):
        # control exceptions

        endpoint = self.basepath + path

        auth = (self.user, self.password)

        headers = {
            'User-Agent': self.agent,
            'Content-Type': 'application/json'
        }

        #data = json.loads(payload)
        data = payload

        requestMethod = getattr(r, method)

        request = requestMethod(endpoint, auth=auth, data=data,
                                headers=headers)

        return request.text

    def getProjects(self):
        path = '/projects.json'
        return self.__makeRequest(path, 'get')
