#!/usr/bin/env python3
"""
client
"""
from client import GithubOrgClient


client = GithubOrgClient("google")
#org_items = client.org()
for key, value in client.org().items():
    print(f"{key}: {value}")
