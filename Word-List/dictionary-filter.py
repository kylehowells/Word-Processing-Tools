import re
import string
import argparse
import os
import plistlib




wordDict = dict()

def loadWordDictionary(filepath):
	global wordDict
	wordDict = plistlib.readPlist(filepath)

def getLexicalClass(word, _definition=None):
	lexicalToken = "▶"
	tokenLength = len(lexicalToken)
	definition = _definition or wordDict[word]
	# wordDict[word] = word defintion
	# wordDict[word].split() = split into parts
	# "if lexicalToken in _word" = check this part has lexical class
	# transform _word to _word[tokenLength:] = "1Word" -> "Word"
	return set([_word[tokenLength:] for _word in definition.split() if lexicalToken in _word])



def main():
	# Command line arguments
	parser = argparse.ArgumentParser(description='Scans a text file (or a directory) and generates a word list from that file.')
	# Basics
	parser.add_argument('-d', action='store', dest='dict', required=True, help='The input filepath for the dictionary plist file to be used.')
	parser.add_argument('-i', action='store', dest='input', required=True, help='The input filepath')
	parser.add_argument('-o', action='store', dest='output', help='The output filepath (defaults to overriding the input file)')
	# Filters
	parser.add_argument('-vulgar', action='store_true', dest='vulgar', help='Filter out words with "vulgar slang" in the definition.')
	parser.add_argument('-abbr', action='store_true', dest='abbr', help='Filter out abbreviations.')
	parser.add_argument('-names', action='store_true', dest='names', help='Filter out proper names (words without a lexical class).')
	parser.add_argument('-len', action='store', dest='lenth', type=int, default=0, help='The minimum required word lenth') # TODO: Add a maximum length
	# TODO: Find some way to filter out words that ONLY have an 'informal' meaning
	# TODO: Some abbreviations aren't marked as such: Example: "pac" = political action committee. "short for "
	args = parser.parse_args()

	inputPath = args.input

	# Check the input file exists
	if os.path.isfile(inputPath) == False:
		print("ERROR: input must be a valid file")
		print(inputPath)
		exit()

	# Check the dictionary file exists
	if os.path.isfile(args.dict) == False:
		print("ERROR: dictionary must be a valid plist file")
		print(args.dict)
		exit()


	# Load word dictionary
	loadWordDictionary(args.dict)

	# Load word list
	words = list()
	with open(inputPath, encoding='utf8', mode="r") as f:
		for line in f:
			# Info
			word = line.strip()
			definition = wordDict.get(word)
			if definition == None:
				continue
			lexicalClasses = getLexicalClass(word, _definition=definition)
			# Filter out things
			if len(word) < args.lenth: # Minimum word length
				continue
			if args.names and len(lexicalClasses) == 0: # Names have no lexical class in our dictionary
				continue
			if args.abbr and len(lexicalClasses) == 1 and "abbreviation" in lexicalClasses: # If the word is only an abbreviation
				# TODO: filter out 'suffix' words as well ("ful"). Remove all disallowed lexicalClasses then check if len(lexicalClasses) == 0 and remove as needed
				continue
			if args.vulgar and "vulgar slang" in definition: # Swear words
				continue

			# Save this word
			words.append(word)

	#
	# Save Results
	#

	#Save 'all_words' to a file
	fileString = '\n'.join( sorted(words) )

	with open( (args.output or inputPath) , "w") as f:
		f.write(fileString)


if __name__ == "__main__":
	main()
