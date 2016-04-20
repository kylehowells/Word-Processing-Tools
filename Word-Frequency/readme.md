# Word Frequency Tools

## wordfrequency.py

Scans a text file (or all text files in a directory) and and counts how many times it has seen each word.

#### Usage:

```bash
python wordfrequency.py -i "input_file.txt"
python wordfrequency.py -i "input_directory"
python wordfrequency.py -i "input_file.txt" -o "output-wordlist.txt"
```

#### Example:
Input

    This a simple sentence. In fact, this sentence is so simple it doesn't contain very many words at all.

Output

```
this 2
simple 2
sentence 2
so 1
all 1
contain 1
doesn 1
is 1
fact 1
a 1
in 1
t 1
many 1
very 1
it 1
words 1
at 1
```


**Note:** This is written to scan files line by line to minimise ram requirements and allow it to process very large files.


## wordfilters.py

Takes the output from wordfrequency.py ("word count\n") and filters out certain words.

**Options**

- '-w': The filepath for a word "white list" to use (excludes all words not in the list).
- '-min': The minimum word frequency for a word to be included in the output.
- '-len': The minimum required word lenth.


#### Usage:

```bash
# Removes all words that occurred less than 3 times
python wordfilters.py -i "input_word_count.txt" -min 3
# Removes all words that are shorter than 3 letters
python wordfilters.py -i "input_word_count.txt" -len 3
# Excludes all words not found in the whitelist, that are less than 4 letters long, or that occur less than 5 times and saves the result to a new file. 
python wordfilters.py -w "whitelist_wordlist.txt" -i "input_file.txt" -min 5 -len 4 -o "output-wordlist.txt"
```

#### Example:
Input (example.txt)

```
this 2
simple 2
sentence 2
so 1
all 1
contain 1
doesn 1
is 1
fact 1
a 1
in 1
t 1
many 1
very 1
it 1
words 1
at 1
```

Command

    python wordfilters.py -min 1 -len 3 -i "example.txt" -o "example-filtered.txt"

Output (example-filtered.txt)

```
sentence 2
simple 2
this 2
all 1
contain 1
doesn 1
fact 1
many 1
very 1
words 1
```
