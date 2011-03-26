import sys

from curveship.runner import main as curveship_main


def main(argv=sys.argv):
    argv.insert(1, 'curveship_lost_one.lost_one')
    curveship_main(argv)
