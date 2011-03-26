import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    HAS_SETUPTOOLS = False
    extra_args = {'scripts': ['scripts/narrate.py']}
else:
    HAS_SETUPTOOLS = True
    extra_args = {'entry_points':
                    {'console_scripts':
                      ['narrate = curveship.runner:main'],
                    },
                 }

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

main_extras = {}
main_extras.update(shared_metadata)
main_extras.update(extra_args)

# Allow for separate sdists from the same checkout
if os.path.isdir('curveship'):
    setup(name='curveship',
          description='Interactive Narrating for Interactive Fiction',
          long_description=README + "\n\n" + CHANGES,
          packages=['curveship'],
          **main_extras
         )

#------------------------------------------------------------------------------
#   Build distributions for add-ons.
#------------------------------------------------------------------------------
ADD_ONS = [
    ('spins', 'Example spins, potentially useful for any fiction', {}),
    ('adventure', 'Classic Adventure retold under Curveship',
        {'entry_points': {
            'console_scripts':
                ['adventure = curveship_adventure.runner:main'],
            },
        }),
    ('artmaking', 'Simple example fiction with victory condition',
        {'entry_points': {
            'console_scripts':
                ['artmaking = curveship_artmaking.runner:main'],
            },
        }),
    ('cloak', 'Variations on classic Cloak of Darkness fiction',
        {'entry_points': {
            'console_scripts':
                ['cloak = curveship_cloak.runner:main',
                 'cplus = curveship_cloak.runner:cplus_main',
                ],
            },
        }),
    ('lost_one', 'Example of discourse-modifying fiction',
        {'entry_points': {
            'console_scripts':
                ['lost_one = curveship_lost_one.runner:main'],
            },
        }),
    ('robbery', 'The Simulated Bank Robbery, a story (not an IF) '
                'for telling via Curveship.',
        {'entry_points': {
            'console_scripts':
                ['robbery = curveship_robbery.runner:main'],
            },
        }),
]

for name, description, extras in ADD_ONS:
    # Allow for separate sdists from the same checkout
    add_on = 'curveship_%s' % name
    if os.path.isdir(add_on):
        add_on_extras = {}
        add_on_extras.update(shared_metadata)
        add_on_extras.update(extras)
        if not HAS_SETUPTOOLS:
            if 'entry_points' in add_on_extras:
                del add_on_extras['entry_points']
        setup(name=add_on,
              description=description,
              packages=[add_on],
              **add_on_extras
             )

