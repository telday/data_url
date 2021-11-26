from . import *

data = input()
url = DataURL.from_url(data)
print(url.data)
