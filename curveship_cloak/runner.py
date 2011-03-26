import sys

from curveship.runner import main as curveship_main


def main(argv=sys.argv):
    argv.insert(1, 'curveship_cloak.cloak')
    curveship_main(argv)


def cplus_main(argv=sys.argv):
    argv.insert(1, 'curveship_cloak.cplus')
    curveship_main(argv)
