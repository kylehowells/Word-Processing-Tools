# Word-Processing-Tools
A collection of command line tools I wrote to process text files. Written in Python 3

**Note:** These tools are written to scan files line by line to minimise ram requirements and allow it to process very large files.

## Word-List
This scans a text file (or all text files in a directory) and builds a word list of all the words it finds.

#### Usage:

```bash
python wordlist.py -i "input_file.txt"
python wordlist.py -i "books/" -o "words.txt"
python wordlist.py -i "input_file.txt" -o "output-wordlist.txt"
```

## Word-Frequency

Scans a text file (or all text files in a directory) and and counts how many times it has seen each word.

#### Usage:

```bash
python wordfrequency.py -i "input_file.txt"
python wordfrequency.py -i "input_directory"
python wordfrequency.py -i "input_file.txt" -o "output-wordlist.txt"
```
