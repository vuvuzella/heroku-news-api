"""
  class: StorageEngine 
  methods:
    get_collection()
"""
import psycopg2
import sqlite3

from pymongo import MongoClient


class StorageEngine(object):
  """
  Class to directly communicate with the data server
  Handles communication with the server
  """
  def __init__(self, engine):
    """
    Initialization
    """
    self.mongoClient = MongoClient('localhost', 27017)
    self.mongoDb = self.mongoClient['test_news']
    self.postgreDb = psycopg2.connect('dbname=test_news user=devbox password=1234')
    self.sqlite3Db = sqlite3.connect('migrate.db')

    self.db = None

    switcher = {
      'mongodb' : self.mongoDb,
      'postgresql' : self.postgreDb,
      'sqlite3' : self.sqlite3Db
    }

    self.db = switcher.get(engine, None)

  def get_collection(self, coll_name):
    """
    retrieves the collection to query from
    """
    # return self.db[coll_name]
    cursor = self.sqlite3Db.cursor()
    return cursor.execute('select * from articles')

  def get_title(self, article_sorce):
    """
     returns the news article title string
    """
    pass

if __name__ == '__main__':
  se = StorageEngine()
  db_legit = se.get_collection('articles')
  """
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
  """

  """ Migrate data from mongoDB to postgreSQL """
