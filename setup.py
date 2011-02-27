import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

#------------------------------------------------------------------------------
#   Build distributions for the core Curveship library.
#------------------------------------------------------------------------------

setup(name='curveship',
      version='0.1',
      description='Interactive Narrating for Interactive Fiction',
      long_description=README + "\n\n" + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Topic :: Games/Entertainment",
        ],
      keywords="interactive fiction",
      author="Nick Montfort",
      author_email="nickm@nickm.com",
      url="http://www.curveship.com",
      license="ISCL",
      packages=['curveship'],
      scripts=['curveship.py'],
      )
