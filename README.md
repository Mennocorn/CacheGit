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
# List of Requirements
````
discord.ext.tasks
json
https://github.com/Mennocorn/MediaManager
````
# License
````
MIT License

Copyright (c) 2021 Unicorn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````


