import xml.etree.ElementTree as ET
from pprint import pprint
from lxml import etree
import codecs

# ==========CONSTANTS============
REVIEW_TYPE = 'positive'

def extractData(reviewType):
	
	fileName = '../raw_data/'+reviewType+'.review'
	reviewTitleFilepath = '../raw_data/'+reviewType+'.review_title'
	reviewTextFilepath = '../raw_data/'+reviewType+'.review_text'
	reviewRatingFilepath = '../raw_data/'+reviewType+'.review_rating'
	
	reviewTextList = []
	reviewRatingList = []
	reviewTitleList = []
	
	parser = etree.XMLParser(recover=True)
	tree = etree.parse(fileName, parser=parser)
	root = tree.getroot()

	# tree = ET.parse(filename)
	# root = tree.getroot()

	for review in root.findall('review'):
		reviewTitle = review.find('title')
		reviewTitleList.append(reviewTitle.text)
		reviewText = review.find('review_text')
		reviewTextList.append(reviewText.text.replace('\n',' '))
		reviewRating = review.find('rating')
		reviewRatingList.append(reviewRating.text)
	
	# pprint(reviewRatingList)
	# pprint(reviewTitleList)
	# pprint(reviewTextList)

	with codecs.open(reviewTitleFilepath,"w","utf-8") as f2:
		for title in reviewTitleList:
			f2.write(unicode(title))
	
	with codecs.open(reviewTextFilepath,"w","utf-8") as f1:
		for text in reviewTextList:
			f1.write(unicode(text)+'\n')

	with codecs.open(reviewRatingFilepath,"w","utf-8") as f3:
		for rating in reviewRatingList:
			f3.write(unicode(rating))

if __name__ == '__main__':
	extractData(reviewType = REVIEW_TYPE)