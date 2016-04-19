# Word Frequency

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
