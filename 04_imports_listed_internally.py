# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "django",
#     "httpx",
# ]
# ///

import sys

import django
import httpx

major, minor, micro = sys.version_info[:3]
print(f'using python version, ``{major}.{minor}.{micro}``')
print(f'using django version, ``{django.get_version()}``')
print(f'using httpx version, ``{httpx.__version__}``')
