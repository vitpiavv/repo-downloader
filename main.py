#!usr/bin/python
import subprocess
import sys
from pathlib import Path

file_path = Path(__file__).parent / 'repos.txt'

with open('repos.txt') as f: 
    repos = [line.strip() for line in f if line.strip()]


def ensure_git(repos):
    if not repos.endswith('.git'):
        return repos +'.git'
    return repos


for url in repos:
    try:
        subprocess.run(['git', 'clone', url])

    except Exception as e: 
        print(f'Failed to clone {url} {e}')
        continue




