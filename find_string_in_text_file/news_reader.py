
import os
import sys

import re

class news_reader:

	def find_matched_words(file_path, keyword):
	    """
	    Get the list of matching words in the text file.

	    Arguments:
		file_path (str): A complete path for the text file
		keyword (str): A string to find in the text file
	 
	    """
	    if not os.path.exists(file_path):
		print 'We were unable to find the file at provided path.'
		return []

	    with open(file_path, 'r') as text_file:
		text_file_content = text_file.read()

	    keyword_matches = re.findall(keyword, text_file_content, re.IGNORECASE)
	    return keyword_matches


	def number_of_matches(file_path, keyword):
	    """
	    Get the number of matches matched from keyword in text file

	    Arguments:
		file_path (str): A complete path for the text file
		keyword (str): A string to find in the text file
	
	    """
	    if not os.path.exists(file_path):
		print 'We were unable to find the file at provided path.'
		return []

	    with open(file_path, 'r') as text_file:
		text_file_content = text_file.read()

	    keyword_matches = re.findall(keyword, text_file_content, re.IGNORECASE)
	    return len(keyword_matches)



	if len(sys.argv) != 3:
	    print 'The provided information is not complete. The input should be ' \
	       'provided in following format: ~/workspace/project/text_file Pakistan'
	    sys.exit()

	file_path = sys.argv[1]
	keyword = sys.argv[2]

	if not os.path.isfile(file_path):
	    print 'The provided path for file is incorrect. Please re-try'
	    sys.exit()



	# Absolute path for the text file in which we have to find the keyword 
	# file_path = 'NewsReader.txt'
	# keyword = 'pakistan'

	print find_matched_words(file_path, keyword)
	print 'Number of matches found ' , number_of_matches(file_path, keyword)
