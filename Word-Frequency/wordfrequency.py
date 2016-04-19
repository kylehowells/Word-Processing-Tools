import re
import string
import argparse
import os


def getWordsCountsFromFile(filepath):
	wordCounts = dict()

	# Open the file, go through line by line seperating words
	with open(filepath, encoding='utf8', mode="r") as f:
		for line in f:
			words = re.findall(r'\w+', line)
			for word in words:
				lowercase = word.lower()
				wordCount = wordCounts.get(lowercase, 0) + 1
				wordCounts[lowercase] = wordCount
	
	return wordCounts


def main():
	# Command line arguments
	parser = argparse.ArgumentParser(description='Scans a text file (or a directory) and generates a word list from that file.')
	parser.add_argument('-i', action='store', dest='input', required=True, help='The input filepath')
	parser.add_argument('-o', action='store', dest='output', default="wordfrequency.txt", help='The output filepath')
	args = parser.parse_args()


	#
	# Process the text files
	#
	wordCounts = dict()

	# Add up the word counts as we go
	def mergeCountsInto(originalCounts, extraCounts):
		for key, newCount in extraCounts.items():
			originalCounts[key] = (originalCounts.get(key, 0) + newCount)


	# Process the file, or directory
	inputPath = args.input
	if os.path.exists(inputPath) == False:
		print("Error: input file does not exist")
		print(inputPath)
		exit()

	if os.path.isdir(inputPath):
		for f in os.listdir(inputPath):
			if f.endswith(".txt"):
				filepath = os.path.join(inputPath, f)
				mergeCountsInto(wordCounts, getWordsCountsFromFile(filepath) )
	else:
		mergeCountsInto(wordCounts, getWordsCountsFromFile(inputPath) )


	#
	# Save word counts to a file
	#

	# Create a list we can sort
	wordList = list()
	for key, value in wordCounts.items():
		wordList.append( (key, value) ) # ("word", count)

	# sort by the 2nd element in the tuple (highest first)
	wordList.sort(key=lambda tup: tup[1], reverse=True)

	# Create a string: with the pattern "word count\n"
	fileString = '\n'.join( [(word + " " + str(count)) for (word, count) in wordList] )


	# Save the result
	with open(args.output, mode="w", encoding='utf8') as f:
		f.write(fileString)


if __name__ == "__main__":
	main()
