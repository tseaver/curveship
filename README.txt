 __________
/ Curveship
  Interactive Narrating for Interactive Fiction
                                               http://curveship.com
                                               Nick Montfort

Curveship is a command-line Python program. Python 2.7.1 is recommended, though
earlier 2.X versions will work. Opening a terminal window (e.g., xterm on Linux
Terminal on Mac, or the cmd.exe Windows Command Line) and working in that 
window is necessary for any use of Curveship.

The system is a Python framework that provides a way to:

<> Simulate a fictional world to be presented in text, as all interactive
   fiction systems do.

<> Vary the way that the same underlying events are told, changing order,
   speed, focalization, distance, time of narrating, and other qualities of the
   narrating, a new contribution.

Curveship is a complex system, developed for researchers in AI, computational
creativity, narrative theory, and other fields in addition to IF author/
programmers. The system will be most easily understood by those familiar with
both interactive fiction and narrative theory.

The most obvious things to do with the system at this point include writing
interactive fiction for people to enjoy; teaching about interactive narrative
and narrative theory; and integrating the system with story generators, drama
managers, commonsense reasoning systems, and other AI systems for research
purposes.

There is not a manual or other extensive documentation for Curveship ready
at the first time of release. The code is commented throughout. Also, several 
articles have been published about the system. Beyond that, a short reference
and a guide to writing string-with-slots templates can be found at 
http://curveship.com. For now, familiarity with Python, a willingness to look 
at the system's code, and a willingness to go through examples will be most 
helpful in learning about Curveship.



## CONTENTS

Installing Python
Example Fictions, a.k.a. Games
Starting a Fiction, a.k.a. Game
Debugging Directives
Automated Play and Testing



## INSTALLING PYTHON

LINUX: Python is installed by default in most distribtuions. If necessary,
install it via apt-get, rpm, GUI package installers, or other usual means.

MAC OS X: Python is installed by default.

WINDOWS: Install Python by downloading the Windows installer from Python.org.
For instance, the current version at the release of Curveship was at:

    http://www.python.org/ftp/python/2.7.1/python-2.7.1.msi

Ensure that you can run Python from the command line by typing "python" there.
You may need to add the Python directory to your path or type the full
pathname. On Windows, for instance, this would be "\Python27\python" if you
installed the version above in the default location.



## EXAMPLE FICTIONS, A.K.A. GAMES

The relative paths of all the example games are given in Linux/Mac OS X format.
On Windows, "\" should be used instead of "/", as in "fiction\artmaking.py" All
of these are found in the "fiction" directory.

<> Artmaking -- An extremely simple but solvable one-page example game.
   Introduces the major types of Items, subclassing Items, refusals, initial 
   actions, and metadata.
                                       artmaking.py

<> The Simulated Bank Robbery -- Not an interactive fiction, but a static
   story that can be told in many different ways. This defines actions and 
   items in a minimal way; spin files can be applied to the fiction file to
   produce different tellings.
                                       robbery.py

<> Cloak of Darkness -- The standard small demo game for IF, which has been
   implemented in many different IF systems. Like Artmaking, it is not intended
   to be fun, but instructive. Introduces multiple rooms, dark rooms, wearable
   things, items that are part of others, consequences of failed actions, and a
   darkness-causing item.
                                       cloak.py

<> Cloak of Darkness Plus -- An extended version of Cloak of Darkness.
   Introduces an additional actor, items that serve as compartments which 
   actors can enter, a thing which is a light source and can be turned on and
   off, a substance, and a vessel.
                                       cplus.py
                                       cloak.py

<> Lost One -- A demo of many actors performing actions in a large open area,
   and of the way that the spin (the parameters for narrating) can change
   based on the actions of the player character. Introduces views onto other
   rooms and dynamic spin.
                                       lost_one.py
                                       plaza.py

<> Adventure in Style -- A slightly modified version of the classic game
   by Crowther and Woods, crossed with Queneau's Exercises in Style. A simple
   built-in way to vary the telling is provided. For those familiar with the
   original Adventure, this will be a very useful reference. The game provided 
   is winnable, but has not been extensively tested, so some aspects of the
   original Adventure (such as ways to perish) may not be implemented fully.
   Nevertheless, this is the largest example and shows how many aspects of a
   large-scale game can be implemented.
                                       adventure.py



## STARTING A FICTION, A.K.A. GAME

To start the simplest example, Artmaking, first change to the main Curveship
directory by typing:

    cd CURVESHIP_PATH

Where "CURVESHIP_PATH" is the directory where the main Curveship files are
located. Then, type:

    python curveship.py fiction/artmaking.py

Except on WINDOWS, where it is necessary to use "\" instead of "/":

    python curveship.py fiction\artmaking.py

If you need to the type the full pathname of python to run it, substitute that
for "python" in all of these commands.

On LINUX & MAX OS X, "python curveship.py" can be abbreviated "./curveship.py"
or (if the Curveship directory is added to one's path) "curveship.py".

By default, Curveship does not start in debugging mode, but this mode will
almost always be desired by IF authors and researchers. Debug mode allows the 
directive "spin" (which displays and sets narrative parameters) to be used, as
well as the "world" and "concept" directives. To run Curveship in this mode,
use the "--debug" flag:

    python curveship.py --debug fiction/artmaking.py

You may wish to create an alias to curveship with the "--debug" flag to 
facilitate use of the system.

To start Adventure in Style, change to the main Curveship directory and type:

    python curveship.py fiction/adventure.py

To start "plain" Cloak of Darkness, Cloak of Darkness Plus, or Lost One:

    python curveship.py fiction/cloak.py
    python curveship.py fiction/cplus.py
    python curveship.py fiction/lost_one.py

Lost One uses fiction/plaza.py, but that module is not itself a fiction file,
just the setting for Lost One. Cloak of Darkness Plus uses the basic Cloak of 
Darkness file, cloak.py.

You can update a fiction file with one or more additional spin when you start
a fiction, e.g.:

    python curveship.py fiction/cplus.py spin/personal.py
    python curveship.py fiction/cplus.py spin/personal.py spin/surprise.py
    python curveship.py fiction/cplus.py spin/surprise.py spin/hesitant.py

Because Lost One uses a dynamic spin, some of the settings will be changed
unless you type the directive "spin dynamic off" at the first prompt. If you
turn on the lamp in Adventure in Style, the spin will similarly be changed.

To produce a telling of a story, without the chance to interact, based on The
Simulated Bank Robbery:

    python curveship.py fiction/robbery.py

Add the names of any span files afterwards to apply those spins. For instance:

    python curveship.py fiction/cplus.py spin/valley.py spin/retrograde.py



## DEBUGGING DIRECTIVES

Some interesting debugging directives are "spin", "world", and "concept".

Type "spin" to see the current narrative parameters. Type "spin" with 
additional parameters to see particular settings or to change them. For 
instance, "spin time" gives the time of narrating and "spin time after" sets 
the time of narrating to after the events.

Type "world" and "concept" to see how you can view the state of the IF world
or of a particular actor's concept of the world.

All possible debugging directives can be found in discourse_model.py within
the Discourse class:

    debugging_verbs
    spin_arguments (these are possible arguments to "spin")

They include "world tree" (see every item in the game, arranged in a tree,
according the main simulation) and "world actions" (same for the actions).

Also in Discourse is command_grammar, which shows which command verbs exist. A 
small set (essentially, the verbs necessary to implement Adventure) has been 
implemented.



## AUTOMATED PLAY AND TESTING

Inputs are available in the "walk" directory for all of the fiction files. If 
you start them using the "--auto" flag AND a filename argument:

    python curveship.py fiction/adventure.py --auto walk/adventure_win.txt

Or, on Windows:

    python curveship.py fiction\adventure.py --auto walk\adventure_win.txt

Curveship will automatically run the series of commands which will bring you
through the game to a winning ending.

This can be used in testing fictions/games and in regression testing for the
system itself.

