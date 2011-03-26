import sys

from curveship.runner import main as curveship_main


def main(argv=sys.argv):
    argv.insert(1, 'curveship_adventure.adventure')
    curveship_main(argv)
