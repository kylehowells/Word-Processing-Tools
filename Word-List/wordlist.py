import re
import string
import argparse
import os


def getWordsFromFile(filepath):
	all_words = set()

	# Open the file, go through line by line seperating words
	with open(filepath, "r") as f:
		for line in f:
			words = re.findall(r'\w+', line)
			for word in words:
				all_words.add(word.lower())
	
	return all_words


def main():
	parser = argparse.ArgumentParser(description='Scans a text file (or a directory) and generates a word list from that file.')
	parser.add_argument('-i', action='store', dest='input', required=True, help='The input filepath')
	parser.add_argument('-o', action='store', dest='output', default="wordlist.txt", help='The output filepath')
	args = parser.parse_args()


	all_words = set()

	inputPath = args.input


	if os.path.isdir(inputPath):
		for f in os.listdir(inputPath):
			if f.endswith(".txt"):
				filepath = os.path.join(inputPath, f)
				all_words.update( getWordsFromFile(filepath) )
	else:
		all_words.update( getWordsFromFile(inputPath) )


	#Save 'all_words' to a file
	fileString = '\n'.join( sorted(all_words) )

	with open(args.output, "w") as f:
		f.write(fileString)


if __name__ == "__main__":
	main()
