#!/usr/bin/env python
# setup.py, mb, 2012-05-28, 2012-08-14, 2012-12-07

from distutils.core import setup

import os
ospj = os.path.join

if 1:
    # Build a list of data files to be included.
    # We need to do this because the distutils offer no way
    # to include whole subtrees
    topdir = 'src/t3sphinx/'
    topdirlen = len(topdir)

    t3sphinx_package_data = []
    result = []
    for path, dirs, files in os.walk(topdir + 'themes'):
        dirs.sort()
        files.sort()
        for afile in files:
            result.append(ospj(path[topdirlen:], afile))
    t3sphinx_package_data.extend(result)

    result = []
    for path, dirs, files in os.walk(topdir + 'settings'):
        dirs.sort()
        files.sort()
        for afile in files:
            result.append(ospj(path[topdirlen:], afile))
    t3sphinx_package_data.extend(result)

    result = []
    for path, dirs, files in os.walk(topdir + 'resources'):
        dirs.sort()
        files.sort()
        for afile in files:
            result.append(ospj(path[topdirlen:], afile))
    t3sphinx_package_data.extend(result)

    result = []
    for path, dirs, files in os.walk(topdir + 'ext'):
        dirs.sort()
        files.sort()
        for afile in files:
            result.append(ospj(path[topdirlen:], afile))
    t3sphinx_package_data.extend(result)

    result = []
    for path, dirs, files in os.walk(topdir + 'builders'):
        dirs.sort()
        files.sort()
        for afile in files:
            result.append(ospj(path[topdirlen:], afile))
    t3sphinx_package_data.extend(result)

if 1:
    setup(
        name = 't3sphinx',
        version = '0.3.0',
        description = 'TYPO3 specific extensions for Sphinx',
        author = 'Martin Bless',
        author_email = 'martin@mbless.de',
        url = 'http://typo3.org/teams/documentation/',
        packages = ['t3sphinx'],
        package_dir = {'t3sphinx': 'src/t3sphinx'},
        package_data = {'t3sphinx': t3sphinx_package_data},
    )
