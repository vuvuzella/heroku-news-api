"""
  class: StorageEngine 
  methods:
    get_collection()
"""
from pymongo import MongoClient

class StorageEngine(object):
  """
  Class to directly communicate with the data server
  Handles communication with the server
  """
  def __init__(self):
    """
    Initialization
    """
    self.client = MongoClient('localhost', 27017)
    self.db = self.client['test_news']

  def get_collection(self, coll_name):
    """
    retrieves the collection to query from
    """
    return self.db[coll_name]

if __name__ == '__main__':
  se = StorageEngine()
  db_legit = se.get_collection('articles')
  db_missing = se.get_collection('non_existing_db')
  if db_legit.find_one() is not None:
    print type(db_legit)
  else:
    print 'test_news db is non-existent'
  if db_missing.find_one() is not None:
    print type(db_missing)
  else:
    print 'non_existing_db is non-existent'

  if db_legit.find_one() is not None:
    for entry in db_legit.find():
      print entry['article_title']
