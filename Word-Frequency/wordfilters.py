import string
import argparse
import os
import collections



def main():
	#
	# Command line arguments
	#
	parser = argparse.ArgumentParser(description='Scans a text file (or a directory) and generates a word list from that file.')
	# Basics
	parser.add_argument('-i', action='store', dest='input', required=True, help='The frequency file (in the format output by wordfrequency.py) to be processed.')
	parser.add_argument('-o', action='store', dest='output', help='The output filepath (by default the input file will be overriden)')
	# Filters
	parser.add_argument('-w', action='store', dest='whitelist', help='The filepath for the word white list to use.')
	parser.add_argument('-min', action='store', dest='minfreq', type=int, default=0, help='The minimum word frequency for a word to be included in the output')
	parser.add_argument('-len', action='store', dest='lenth', 	type=int, default=0, help='The minimum required word lenth')

	args = parser.parse_args()


	#
	# Process the file, or directory
	#

	inputPath = args.input
	# Check the input file exists
	if os.path.isfile(inputPath) == False:
		print("ERROR: input must be a valid file")
		print(inputPath)
		exit()

	# Load whitelist (if specified)
	whitelist = None
	if args.whitelist:
		with open(args.whitelist, encoding='utf8', mode="r") as f:
			whitelist = set()
			for line in f:
				whitelist.add( line.strip() )

	# Read the file into a list (we are presuming the input is valid and does not contain any duplicate records)
	wordCounts = list()
	WordCount = collections.namedtuple('WordCount', ['word', 'count'])

	# Read and process the input file
	with open(inputPath, encoding='utf8', mode="r") as f:
		for line in f:
			parts = line.strip().split()
			result = WordCount(parts[0].strip(), int(parts[1])) # (word:string, count:int)
			# Filters
			if len(result.word) < args.lenth: # Word Lenth
				continue
			if result.count < args.minfreq: # Word Frequency
				continue
			if whitelist != None:
				if result.word not in whitelist: # Whitelist
					continue
			# Add it to the array if it passed the filters
			wordCounts.append( result )


	#
	# Export the result
	#

	# Sort by count first, then by word. (sorts smallest first so -count for biggest first, then a,b,c...)
	wordCounts.sort(key=lambda x: (x.count * -1, x.word))

	# Generate the resulting string
	fileString = '\n'.join( [(result.word + " " + str(result.count)) for result in wordCounts] )

	# Get the output file path
	outputFile = args.output or inputPath

	# Save the result
	with open(outputFile, mode="w", encoding='utf8') as f:
		f.write(fileString)


if __name__ == "__main__":
	main()
