import django
import httpx

print(f'using django version, ``{django.get_version()}``')
print(f'using httpx version, ``{httpx.__version__}``')
