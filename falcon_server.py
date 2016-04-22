import falcon
import json
from pymongo import MongoClient

class StorageEngine(object):
  """
  Class to directly communicate with the data server
  Handles communication with the server
  """
  pass

class NewsParser(object):
  """
  Parser class to provide clean and processed data to NewsResource
  Data provided by the engine
  can have multiple engines, but will only use the same parsing syntax for
  each data engine
  PLAN: Different news parser for each candidate
  """
  def __init__(self, engine):
    """
    Initialization
    """
    pass

  def get_article_hits(self, last_name, first_name):
    """
    Retrieves raw data from local DB,
    Searches the news article body for the name of the presidentiable
    Returns a JSON for the following keys and values:
      name - Name of the presidentiable
      total_hits - Total number of articles related to the name
      article_list - the list of articles that is related to the name.
      total_hits must correspond to the same length of article_list
    """
    pass

class NewsResource(object):

  def __init__(self):
    """
    Initialization
    1. Read data file
    2. Load as JSON
    3. populate self.data?
    """
    self.data = None
    # data_file = open('data/', 'r')

  def on_get(self, req, resp):
    """
    Handles GET requests
    """
    resp.body = json.dumps({
      'name' : 'Rodrigo Duterte',
      'total_hits' : '5',
      'article_list' : [
        'http://www.rappler.com/nation/politics/elections/2016/130033-rappler-sms-poll-march-results-duterte',
        'http://newsinfo.inquirer.net/category/latest-stories',
        'http://newsinfo.inquirer.net/780401/pulse-duterte-pulls-away',
        'http://newsinfo.inquirer.net/780555/pdp-laban-duterte-may-not-be-good-husband-but-can-be-great-president',
        'http://news.abs-cbn.com/halalan2016/nation/04/20/16/duterte-marcos-lead-show-grievance-politics-analyst'
      ]
    })

  def on_post(self, req, resp):
    """
    Handles POST requests
    However, this class does not allow post requests.
    """
    pass

api = falcon.API()

# Long-lived class instances
newsResource = NewsResource()
newsParser = NewsParser()

# URL path routing handlers mapping
api.add_route('/', newsResource)
