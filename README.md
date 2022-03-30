# CacheGit
A simple, easy to use python Cache for .json files

# Usage
As a first step import the `Cache` Class to your file
```python
from Cache import Cache
```
Then you have to create an Instance of `Cache`, passing a valid .json file.
```python
cache = Cache(file='example.json')
```
Before you can use the `Cache` you have to load the .json file.
```python
cache = Cache(file='example.json')

cache.load()
```
To save back to the json file use:
````python
await cache.save()
````
The loaded .json file is represented as a python dictionary
Let this be `example.json`:
````json
{
  "key_1": {
    "value_1": 1,
    "value_2": 2,
    "value_3": 3
  },
  "key_2": {
    "value_1": 1,
    "value_2": 2,
    "value_3": 3
  }
}
````
You would do something like this
````python
import asyncio
from Cache import Cache

cache = Cache('example.json')
cache.load()

print(cache.cache['key_1']['value_1'])
>>> 1
print(cache.cache['key_2']['value_3'])
>>> 3

cache.cache['key_2']['value_2'] = 5

asyncio.run(cache.save())
````
`example.json`:
````json
{
  "key_1": {
    "value_1": 1,
    "value_2": 2,
    "value_3": 3
  },
  "key_2": {
    "value_1": 1,
    "value_2": 5,
    "value_3": 3
  }
}
````

