import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

#------------------------------------------------------------------------------
#   Build distributions for the core Curveship library.
#------------------------------------------------------------------------------
shared_metadata = {
    'version': '0.1',
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Topic :: Games/Entertainment",
        ],
     'keywords': "interactive fiction",
     'author': "Nick Montfort",
     'author_email': "nickm@nickm.com",
     'url': "http://www.curveship.com",
     'license': "ISCL",
}

setup(name='curveship',
      description='Interactive Narrating for Interactive Fiction',
      long_description=README + "\n\n" + CHANGES,
      packages=['curveship'],
      scripts=['curveship.py'],
      **shared_metadata
      )

#------------------------------------------------------------------------------
#   Build distributions for add-ons.
#------------------------------------------------------------------------------
ADD_ONS = [
    ('spins', 'Example spins, potentially useful for any fiction'),
    ('adventure', 'Classic Adventure retold under Curveship'),
    ('artmaking', 'Simple example fiction with victory condition'),
    ('cloak', 'Variations on classic Cloak of Darkness fiction'),
    ('lost_one', 'Example of discourse-modifying fiction'),
    ('robbery', 'The Simulated Bank Robbery, a story (not an IF) '
                'for telling via Curveship.'),
]

for name, description in ADD_ONS:
    add_on = 'curveship_%s' % name
    setup(name=add_on,
          description=description,
          packages=[add_on],
          **shared_metadata
         )

