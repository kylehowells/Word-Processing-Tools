# Word List

Scans a text file (or all text files in a directory) and builds a word list (Set) of all the words it finds.

Usage:

```bash
python wordlist.py -i "input_file.txt"
python wordlist.py -i "books/" -o "words.txt"
python wordlist.py -i "input_file.txt" -o "output-wordlist.txt"
```

**Note:** This is written to scan files line by line so as to minimise ram requirements and allow it to process very large files.
