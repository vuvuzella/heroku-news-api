from StorageEngine import StorageEngine
from NewsParser import NewsParser

class HitStore(object):
  """
  Stores the current:
    1. Total article hits
    2. list of articles
  """
  def __init__(self, l_name, f_name):
    self.total_hits = 0
    self.article_list = []
    self.last_name = l_name
    self.first_name = f_name
    self.populate()

  def get_total_hits(self):
    return self.total_hits

  def get_article_list(self):
    return self.article_list

  def populate(self):
    """
    Populates the HitStore data members for query by the server code 
    """
    se = StorageEngine()
    parser = NewsParser(self.last_name, self.first_name)
    articles = se.get_collection('articles')
    for document in articles.find():
      news = parser.parse_doc(document)
      if parser.is_article_hit(news):
        self.total_hits += 1
        self.article_list.append(news['link'])

if __name__ == '__main__':
  duterte_hits = HitStore('Duterte', 'Rodrigo')
  duterte_hits.populate()
  print duterte_hits.get_total_hits()
  print len(duterte_hits.get_article_list())

  for link in duterte_hits.get_article_list():
    print link

