
from setuptools import setup


setup(name='py_algo',
      version='0.1',
      description='Algorithms in Python',
      long_description=open('README.md').read(),
      keywords='algorithms search sort tree graph',
      url='https://github.com/itratrahman/py_algo',
      author='Itrat Rahman',
      author_email='rahmanitrat@outlook.com',
      license='MIT',
      packages=['py_algo'],
      test_suite='nose.collector',
      tests_require=['nose'])
