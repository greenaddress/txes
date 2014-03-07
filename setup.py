from setuptools import setup, find_packages
import sys, os

version = '0.3.4'

setup(name='txes',
      version=version,
      description="Twisted interface to elasticsearch",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='twisted elasticsearch',
      author='Jason K\xc3\xb6lker',
      author_email='jason@koelker.net',
      url='https://github.com/jkoelker/txes',
      license='BSD License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "twisted",
          "anyjson",
          "treq"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
