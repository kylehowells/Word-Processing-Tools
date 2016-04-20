# Word List

## wordlist.py

Scans a text file (or all text files in a directory) and builds a word list (Set) of all the words it finds.

#### Usage:

```bash
python wordlist.py -i "input_file.txt"
python wordlist.py -i "books/" -o "words.txt"
python wordlist.py -i "input_file.txt" -o "output-wordlist.txt"
```

**Note:** This is written to scan files line by line to minimise ram requirements and allow it to process very large files.



## dictionary-filter.py

Processes a wordlist and applies filters to it. Including excluding words not found in the supplied dictionary.


**Options**

- '-d' [required]: The input filepath for the dictionary plist file to be used.
- '-i' [required]: The input filepath.
- '-o': The output filepath (defaults to overriding the input file).
- '-vulgar': 'Filter out words with "vulgar slang" in the definition.
- '-abbr': Filter out abbreviations.
- '-names': Filter out proper names (words without a lexical class).
- '-len': The minimum required word lenth.

#### Usage:

```bash
# Filter out everything not in the dictionary
python dictionary-filter.py -d "dictionary.plist" -i "input_file.txt"
# Filter out all names (dictionaries have a lot of names in them)
python dictionary-filter.py -d "dictionary.plist" -i "input_file.txt" -o "outputfile.txt" -names
# Filter out abbreviations
python dictionary-filter.py -d "dictionary.plist" -i "input_file.txt" -o "outputfile.txt" -abbr
# Filter out swear words, abbreviations, small words and unknown words
python dictionary-filter.py -d "dictionary.plist" -i "input_file.txt" -o "outputfile.txt" -vulgar -abbr -len 3 -names
```


#### Dictionary Plist format:

```xml
<dict>
	<key>word</key>
	<string>definition</string>
	...
</dict>
```
