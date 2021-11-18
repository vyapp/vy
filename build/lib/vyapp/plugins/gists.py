"""
Overview
========

This plugin is used to create gists on github.

Commands
========

Command: cgist()
Description: Create public gist.

Command: rgist()
Description: Create private gist.

"""

from vyapp.plugins import Command, ENV
from os.path import basename
import webbrowser
import requests
import json

class GistCreate:
    GITHUB_API="https://api.github.com/gists"
 
    def __init__(self, api_token):
        self.api_token = api_token

        self.headers = {
        'Authorization':'token %s' % api_token}

        ENV['cgist'] = self.cgist
        ENV['rgist'] = self.rgist

    def rgist(self, description=''):
        """
        Create private gist.
        """
        self.create(description, False)

    def cgist(self, description=''):
        """
        Create public gist.
        """
        self.create(description, True)

    def create(self, description='', public=False,):
        data = Command.area.get('1.0', 'end')
        payload = {"description": description, "public":True, "files": {
        basename(Command.area.filename): {'content': data}}}
        params = {'scope':'gist'}

        req = requests.post(self.GITHUB_API, headers=self.headers,
            params=params, data=json.dumps(payload))

        rsp = json.loads(req.text)
        print('Gist URL:', rsp['html_url'])
        webbrowser.open(rsp['html_url'])
        
