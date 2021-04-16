# Decode the URL using the API
import urllib.request
from urllib.parse import *

request_url = urllib.request.urlopen("https://en.wikipedia.org/wiki/Apple_Inc.")
parse_url = urlparse("https://www.youtube.com/watch?v=ZCKBmKLROXA")
print(parse_url)