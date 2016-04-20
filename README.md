# Word-Processing-Tools
A collection of command line tools I wrote to process text files. Written in Python 3

**Notes:**
- These tools are written to scan files line by line to minimise ram requirements and allow it to process very large files.
- These tools are written to be cross platform, so they can be used on OSX and Windows.

## Word-List
This scans a text file (or all text files in a directory) and builds a word list of all the words it finds.

#### Usage:

```bash
python wordlist.py -i "input_file.txt"
python wordlist.py -i "books/" -o "words.txt"
python wordlist.py -i "input_file.txt" -o "output-wordlist.txt"
```

`dictionary-filter.py` is a tool to filter the resulting wordlist to remove non-words, names, abbreviations and swear words from the resulting word list (requires a Plist dictionary file generated on OSX).


## Word-Frequency

Scans a text file (or all text files in a directory) and and counts how many times it has seen each word.

#### Usage:

```bash
python wordfrequency.py -i "input_file.txt"
python wordfrequency.py -i "input_directory"
python wordfrequency.py -i "input_file.txt" -o "output-wordlist.txt"
```

`wordfilters.py` is a small tool to filter the output from `wordfrequency.py` in several different ways.

