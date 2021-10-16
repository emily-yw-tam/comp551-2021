# Libraries
import csv
import glob
import re

# load text file and return the content
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

if __name__ == "__main__":
    
    pattern = re.compile(r"_([0-9]+)\.[^\.]+$")

	# Write the training data to csv
    with open('IMDB_training_rating.csv', mode='w') as train_csvfile:
        writer = csv.writer(train_csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Text', 'Label']) # write column names

        # write negative labelled data to the csv
        for fileName in glob.glob('./aclImdb/train/neg/*'):
            rating = pattern.search(fileName).group(1)
            writer.writerow([load_doc(fileName), rating]) 

        # write positive labelled data to the csv
        for fileName in glob.glob('./aclImdb/train/pos/*'):
            rating = pattern.search(fileName).group(1)
            writer.writerow([load_doc(fileName), rating])

	# Write the testing data to csv
    with open('IMDB_testing_rating.csv', mode='w') as train_csvfile:
        writer = csv.writer(train_csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Text', 'Label']) # write column names

        # write negative labelled data to the csv
        for fileName in glob.glob('./aclImdb/train/neg/*'):
            rating = pattern.search(fileName).group(1)
            writer.writerow([load_doc(fileName), rating]) 

        # write positive labelled data to the csv
        for fileName in glob.glob('./aclImdb/train/pos/*'):
            rating = pattern.search(fileName).group(1)
            writer.writerow([load_doc(fileName), rating])
