# Search-List-Everything-Search

This is a simple Python script to copy a list of files with the same format and copy them into a directory using Everything Search program (or maybe other search apps).

the main purpose of providing this script is to find just some desirable files from numerous mp3 files (over 3GB) which have been downloaded through the other script:
https://github.com/rezadevelop/English-words-pronunciation-mp3-audio-download

Instead of write a search script, Everything Search software is used due to its high performance.

## Getting Started

* Download & install [Python 3](https://www.python.org/downloads/)
* Download & install [Everything](https://www.voidtools.com/downloads/)
* Add Python and Everything to Environment Variable
* Run command prompt as administrator
* Open collectfiles.py and set Parameters part of code as you need
* >cd <dir>
* >python3 collectfiles.py

## Content
In addition to [collectfiles.py](collectfiles.py), there are other files just in order to do a simple test. [list.txt](list.txt) contain list of words and Folder [Ref](Ref) is made up of some mp3 files. After running the script, the voice associated with the words will copy to [out](out) folder and those have not found will be listed in [NotFound.txt](NotFound.txt) file.
