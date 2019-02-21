#!/usr/bin/env python3
'''
Create number of repos on Github
set GITHUB_TOKEN environment variable
github-repos.py [repo name] ...
'''

import os, requests, json

class GitHub:

  def __init__(self, token=os.environ['GITHUB_TOKEN']):
    self.token = token
    self.github_url = 'https://api.github.com/'

  def __get_auth_header__(self):
    return {'Authorization': "token " + self.token}

  def list_repos(self):
    '''
    list_repos() -> list
    '''
    r = requests.get(self.github_url + 'user/repos', headers=self.__get_auth_header__()).json()
    repos = []
    for i in r:
      repos.append(i['name'])
    return repos

  def get_owner(self):
    '''
    get_owner()
    Return owner name -> str
    '''
    r = requests.get(self.github_url + 'user/repos', headers=self.__get_auth_header__()).json()
    return r[0]['owner']['login']

  def create_repo(self, name, description='Managed by code'):
    request_url = self.github_url + 'user/repos'
    payload = {'name': name, 'description': description, 'auto_init': 'true'}

    return requests.post(request_url, headers=self.__get_auth_header__(), data=json.dumps(payload))

  def delete_repo(self, name):
    return requests.delete("{}repos/{}/{}".format(self.github_url, self.get_owner(), name),
                               headers=self.__get_auth_header__()).status_code

def main():

  repo_name = 'some_repo'

  github = GitHub()

  print(github.list_repos())

  r = github.create_repo(repo_name).json()

  if 'errors' in r:
    print('Error: {}\n\n'.format(r['errors'][0]['message']))
    return -1

  print('Created ' + repo_name)

  code = github.delete_repo(repo_name)
  if code != 204:
    print('Unable to delete repo: {}. Return code: {}'.format(repo_name, code))
    return -1

if __name__ == "__main__":
  main()