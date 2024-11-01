# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "django~=3.2.0",
#     "httpx~=0.25.0",
# ]
# ///

import sys

import django
import httpx

major, minor, micro = sys.version_info[:3]
print(f'using python version, ``{major}.{minor}.{micro}``')
print(f'using django version, ``{django.get_version()}``')
print(f'using httpx version, ``{httpx.__version__}``')
