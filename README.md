# data_url.py

data_url is a Python 3 library which provides easy methods for creating and working with [data URL's](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs). The full API documentation is available [here](https://data-url.readthedocs.io/en/latest/).

## Examples

### Creating a data URL

If all you need is to create a URL and nothing else there is a shortcut method included so you don't need to directly instantiate the DataURL class.

```python3
import data_url

with open('image.jpeg', 'rb') as image:
  data = image.read()

url = data_url.construct_data_url(mime_type='image/jpeg', base64_encode=True, data=data)
```

If you need the information to persist it is recommended to instantiate a class through one of the factory methods on `DataURL`

```python3
import data_url

with open('image.jpeg', 'rb') as image:
  data = image.read()
  
url = data_url.DataURL.from_data('image/jpeg', True, data)
print(str(url))
```

You can access the full data URL by either converting the DataURL object to a string as above or by accessing the `url` attribute.

### Retrieving data from a URL

Given you already have a data URL you can instantiate a DataURL object and retrieve each individual attribute.

```python3
import data_url

raw_url = "data:application/json;base64,ewogICJ0ZXN0IjogMTIzCn0K"

url = data_url.DataURL.from_url(raw_url)

print(url.mime_type, url.is_base64_encoded, url.data)
```
