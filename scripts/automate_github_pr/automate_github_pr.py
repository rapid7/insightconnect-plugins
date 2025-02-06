#!/usr/bin/env python3
import argparse
import json
import requests
import os
import time


class GithubClient:
    def __init__(self, org, repo, token):
        self.base_url = f"https://api.github.com/repos/{org}/{repo}"
        self.token = token

    def get_pull_request(self, pull_number):
        resp = requests.get(url=f"{self.base_url}/pulls/{pull_number}",
                            headers={'Authorization': f"token {self.token}"})
        if resp.status_code == 200:
            return resp.json()
        else:
            raise Exception(f"Failed to get pull request: {resp.text}, {resp.status_code}")

    def create_pull_request(self, title, body, branch, base_branch):
        print(f"Creating pull request to merge {branch} into {base_branch}")
        payload = {
            'title': title,
            'body': body,
            'head': branch,
            'base': base_branch
        }

        resp = requests.post(url=f"{self.base_url}/pulls",
                             data=json.dumps(payload),
                             headers={'Authorization': f"token {self.token}"})
        if resp.status_code == 201:
            title, pull_number, sha = resp.json()['title'], resp.json()['number'], resp.json()['head']['sha']

            print(f"Pull Request created; title: {title}, pull number: {pull_number}, branch sha: {sha}")

            return pull_number, sha
        else:
            raise Exception(f"Failed to create pull request: {resp.text}, {resp.status_code}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload extensions to hub.')
    parser.add_argument('--branch', '-b', required=True, action='store', type=str,
                        help='The branch name with committed changes')
    parser.add_argument('--base', '-d', action='store', type=str, default='master',
                        help='The destination branch to merge changes')
    parser.add_argument('--ghorg', action='store', type=str, default='rapid7',
                        help='The github organization in scope')
    parser.add_argument('--ghrepo', required=True, action='store', type=str,
                        help='The github repository in scope')
    parser.add_argument('--pr_release_title', required=True, action='store', type=str,
                        help='The title of the release PR')
    args = parser.parse_args()

    # Generate client
    github_client = GithubClient(args.ghorg, args.ghrepo, os.getenv('GITHUB_API_KEY'))

    body = f"Automated pull request to bump the SDK version to <SDK_VERSION> for <PLUGIN_NAME>"
    
    n, s = github_client.create_pull_request(
        args.pr_release_title,
        body,
        args.branch,
        args.base)
