import setuptools
from distutils.core import setup
from io import open

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(name='mecab-ko-dic', 
      version='1.0.0',
      author="Robyn Speer",
      author_email="rspeer@luminoso.com",
      description="mecab-ko-dic packaged for Python",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/LuminosoInsight/mecab-ko-dic",
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
      ],
      package_data={'mecab_ko_dic': ['dicdir/*']}
      )
