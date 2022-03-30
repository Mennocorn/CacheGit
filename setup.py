from setuptools import setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
    name='CacheGit',
    version='1.0.0',
    packages=['Cache'],
    url='https://github.com/Mennocorn/CacheGit',
    license='MIT',
    author='Unicorn',
    author_email='kilian.wiendl@gmx.de',
    description='A simple, easy to use Cache system'
)
