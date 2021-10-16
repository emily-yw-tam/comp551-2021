import csv
import glob

# load text file and return the content
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

#when we run this script, __name__ will implicitly equal to "__main__",
#when we import this script from other scripts, __name__ will equal to the name of this script
#So we use "if __name__ == "__main__": " statement as a main function for this class (just like main() in Java)
if __name__ == "__main__":
    
	# Write the training data to csv
	with open('IMDB_training.csv', mode='w') as train_csvfile:
		writer = csv.writer(train_csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Text', 'Label']) # write column names
		
		# write negative labelled data to the csv
		for fileName in glob.glob('./aclImdb/train/neg/*'):
   			writer.writerow([load_doc(fileName), '0'])
		# write positive labelled data to the csv
		for fileName in glob.glob('./aclImdb/train/pos/*'):
   			writer.writerow([load_doc(fileName), '1'])

	# Write the testing data to csv
	with open('IMDB_testing.csv', mode='w') as train_csvfile:
		writer = csv.writer(train_csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Text', 'Label']) # write column names
		
		# write negative labelled data to the csv
		for fileName in glob.glob('./aclImdb/test/neg/*'):
   			writer.writerow([load_doc(fileName), '0'])
		# write positive labelled data to the csv
		for fileName in glob.glob('./aclImdb/test/pos/*'):
   			writer.writerow([load_doc(fileName), '1'])