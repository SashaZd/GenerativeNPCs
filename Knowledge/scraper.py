from lxml import html 
import requests 
import json 
import itertools

######### Global Variables ##########

URL_ALLSIDES_TOPICS_LIST = "https://www.allsides.com/topics-issues"
URL_BASE = "https://www.allsides.com/"

#####################################


class AllSidesScraper(object):
	"""docstring for AllSidesScraper"""
	def __init__(self):
		super(AllSidesScraper, self).__init__()
		# self.get_topics()
		pass


	def get_curated_topics_from_all_sides(self):
		topics_list_page = requests.get(URL_ALLSIDES_TOPICS_LIST)
		tree = html.fromstring(topics_list_page.text)
		infoTable = tree.xpath("//div[contains(@class,'views-row')]/div/a")

		topics = {}

		for topic in infoTable: 
			topics[topic.text_content()] = topic.values()[0]

		return topics


	def get_topic_description(self, topic):
		topic_page = requests.get(URL_BASE+topic.url)
		tree = html.fromstring(topic_page.text)
		infoTable_desc = tree.xpath("//div[contains(@class, 'topic-description')]")

		description = ""

		for desc in infoTable_desc: 
			description += desc.text_content().strip()

		return description


	def get_topic_articles(self, topic):
		topic_page = requests.get(URL_BASE+topic.url)
		tree = html.fromstring(topic_page.text)

		num_pages = self.get_num_articles_in_topic(tree)
		topic._pagination = num_pages

		infoTable_articles = tree.xpath("//div[contains(@class, 'news-title')]/a")

		return []



	def get_num_articles_in_topic(self, tree):
		infoTable_pages = tree.xpath("//li[contains(@class, 'pager-current')]")

		num_pages = []
		for item in infoTable_pages: 
		    num_pages.append(item.text_content().strip().split()[-1])

		try: 
			num_pages = max(map(int, num_pages))
		except (ValueError):
			print "No articles found"
			return None

		num_pages = num_pages if num_pages <= 10 else 10
		
		return num_pages




		


class ManagerTopics(object):
	"""docstring for ManagerTopics"""
	def __init__(self):
		super(ManagerTopics, self).__init__()
		self.topics = {}


	def set_new_topics_list(self):
		"""Gets a list of all the topics from the recommended list in the AllSides.com site
		""" 
		allSides = AllSidesScraper()
		topics = allSides.get_curated_topics_from_all_sides()

		for title, url in topics.items():
			print "--------------------"
			print "Topic: ", title
			topic = Topic(title, url)
			self.add_new_topic(topic)
			topic.description = allSides.get_topic_description(topic)
			# topic.articles = allSides.get_topic_articles(topic)


	def write_topics_file(self):
		topics_list_file = open("topics.json","w")
		
		topics_list = []

		for topic in self.topics.values():
			topics_list.append(topic.get_response_data())

		json.dump(topics_list, topics_list_file)




	# def get_topic_details(self):
	# 	for topic in self.topics.values():
	# 		allSides = AllSidesScraper()

	# 		# Description
	# 		topic.description = 

	# 		# Articles
	# 		allSides.get_topic_articles(topic.url)

			

	def add_new_topic(self, topic):
		self.topics[topic.title] = topic


	def get_topic_by_title(self, title):
		return self.topics[title]



class Topic(object):
	"""A topic from the curated list of topics from the AllSides.com website"""
	t_id = itertools.count().next


	def __init__(self, title, url):
		super(Topic, self).__init__()
		self.id = Topic.t_id()
		self.title = title
		self.url = url
		self.description = None
		self.articles = []
		self._pagination = None


	@property
	def description(self):
		return self.__description


	@description.setter
	def description(self, description=None):
		""" Initializing a description
		""" 
		# if not hasattr(self, 'description') and description: 
		if description and len(description) >= 100: 
			self.__description = description

		else: 
			# print "Todo: No description"
			self.__description = "Description Not Available"


	def get_response_data(self):
		return {
			"title": self.title, 
			"url": self.url, 
			"description": self.description
		}


	def __str__(self):
		return "%s | #Articles: %s"%(self.title, len(self.articles))

	def __repr__(self):
		return "%s | #Articles: %s"%(self.title, len(self.articles))















