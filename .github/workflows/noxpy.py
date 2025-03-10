# Set NOXPY env var based on GitHub Actions' set-python version

import os
import sys

_, github_python_version = sys.argv

mapping = {'3.7':                 '3.7',
           '3.8':                 '3.8',
           '3.9':                 '3.9',
           '3.10':                '3.10',
           '3.11.0-alpha - 3.11': '3.11',
           'pypy-3.8':            'pypy3',
           'pypy-3.9':            'pypy3',
           'pypy-3.10':           'pypy3',
           'pypy-3.11':           'pypy3'}

noxenv = os.getenv('NOXENV')
pyfactor = mapping[github_python_version]

if noxenv in ('unit', 'regression'):
    with open(os.getenv('GITHUB_ENV'), 'a') as env:
        print(f'NOXENV={noxenv}-{pyfactor}', file=env)
