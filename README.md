# What does the Sanitizer do?

The Sanitizer takes a directory of files (e.g. a directory of randomizer seeds) and another directory of text files associated with the first directory (e.g. a directory of spoiler logs) and rearranges them while giving them generic names but keeping the 1-to-1 file association between directories. In practical terms, this shuffles a list of games so that you don't know what game you're playing until you start playing it.<br>

# Why?

I wanted a tool that would help me shuffle together a bunch of different randomizer seeds, generated in advance, but I didn't want to know what game had which settings, and not all of the games I wanted to include had robust mystery settings. Then I realized this script was simple enough that I could easily make something available to the public, so I did.<br>

# Using the Sanitizer

You need python installed on your system in order for the sanitizer to work. AFAIK, any version should do, but if you find you have a version of Python that doesn't work with this program, let me know so I can update this readme.<br>

1. Determine where you want the sanitizer to work. This will be your input to the program. This directory should have a subdirectory named `Games` and (optionally) a subdirectory named `Spoilers`.
2. Place all of the games you want to be sanitized in the `Games` directory.
3. Place all of the spoiler logs/other text files you want to be associated with a game in the `Spoilers` directory. Make sure each spoiler log is named exactly the same as its associated game, except with a .txt extension instead of whatever the game uses.
4. In a command line prompt in the directory containing Sanitizer.py, run `py Sanitizer.py`
5. If you do not have a `Spoilers` directory, the program will ask you to confirm that you would like to proceed without one.
6. The program will now list all of the files in the `Games` and the `Spoilers` directories. For each game, it will also determine whether or not there is an associated spoiler. Note: all games and any spoiler file associated with a game will be renamed. Any file in the `Spoilers` directory that is not a text file or is not associated with a game will be untouched.
7. After reviewing what the program has found, confirm whether to proceed or not.
8. The program will generate a back-up copy just in case, and then proceed with the sanitization. Files will be sanitized in-place, so the output will be in the same directory that you originally placed the games in. A hash of the current time and date is appended to the file names so that you can re-run the process on the same files without worrying about name collisions on subsequent runs. Note: no log telling you how the files were renamed will be generated.