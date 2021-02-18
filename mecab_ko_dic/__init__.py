import os
import sys

def _get_version(dicdir):
    vpath = os.path.join(dicdir, 'version')
    with open(vpath) as vfile:
        return vfile.read().strip()

_curdir = os.path.dirname(__file__)

# This will be used elsewhere to initialize the tagger
DICDIR = os.path.join(_curdir, 'dicdir')
VERSION = _get_version(DICDIR)

mecabrc = os.path.join(DICDIR, 'mecabrc')
MECAB_ARGS = '-r "{}" -d "{}"'.format(mecabrc, DICDIR)
