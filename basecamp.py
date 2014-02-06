#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module manages the basecamp api.

Docs: https://github.com/basecamp/bcx-api

"""

import sys
import requests as r


class Basecamp(object):
    def __init__(self, account, user, password, agent):
        self.account = account
        self.user = user
        self.password = password
        self.basepath = 'https://basecamp.com/{0}/api/v1'.format(self.account)
        self.agent = agent

    def __makeRequest(self, path, method='get', payload=None):
        # TO-DO
        # control response status codes
        # Implement Etag/If-None-Match

        endpoint = self.basepath + path

        auth = (self.user, self.password)

        headers = {
            'User-Agent': self.agent,
            'Content-Type': 'application/json'
        }

        #data = json.loads(payload)
        data = payload

        requestMethod = getattr(r, method)

        try:
            request = requestMethod(endpoint, auth=auth, data=data,
                                headers=headers)
        except r.exceptions.RequestException as e:
            print e
            sys.exit(1)

        return request.json()

    def getProjects(self):
        path = '/projects.json'
        return self.__makeRequest(path)
