import re

class NewsParser(object):
  """
  Parser class to provide clean and processed data to NewsResource
  Data provided by the engine
  can have multiple engines, but will only use the same parsing syntax for
  each data engine
  PLAN: Different news parser for each candidate
  """
  def __init__(self, l_name, f_name):
    """
    Initialization
    """
    # self.engine_list = [ machine for machine in engine ]
    self.last_name = l_name
    self.first_name = f_name
    self.re_pattern = self.init_re_pattern()

  def init_re_pattern(self):
    """
    Creates a regular expression pattern object from the given
    first name and last names. Must be called after assigning first_name and
    last_name members
    Returns a pattern object
    """
    re_pattern = re.compile(r'(' + self.last_name + ')|(' + self.first_name +
                            ')', flags=re.I)
    return re_pattern

  def parse_doc(self, db_doc):
    """
    parses raw document data from mongodb
    """
    # title = db_doc['article_title']
    # author = db_doc['article_author']
    # body = db_doc['article_body']
    # link = db_doc['article_link']

    title = db_doc['article_title']
    author = db_doc['article_author']
    body = db_doc['article_body']
    link = db_doc['article_link']

    return {
      'title' : title,
      'author' : author,
      'body' : body,
      'link' : link
    }

  def is_article_hit(self, article):
    """
    Returns true if article is related to the candidate
    else false
    """
    ret_val = False
    if type(article) is not dict:
      raise TypeError, type(article)
    else:
      if 'title' not in article.keys() or 'body' not in article.keys():
        raise TypeError
    # pattern = re.compile(r'(Duterte)|(Rodrigo)(Duterte)', flags=re.I)
    pattern = self.re_pattern
    title_split = article['title'].split()
    body_split = article['body'].split()

    for word in title_split:
      if pattern.match(word):
        ret_val = True
        break
    if ret_val is False:
      for word in body_split:
        if pattern.match(word):
          ret_val = True
          break
    return ret_val

  def parse_title(self, title):
    """
    Parses the title for the name
    """
    title_split = title.split()
    for word in title_split:
      pass  # TODO: parse title function
    return False

  def parse_body(self, body):
    return False

if __name__ == '__main__':
  # Testing NewsParser 
  parser = NewsParser('Rodrigo', 'Duterte')
  news_dict = {
    'title' : 'Duterte\'s comments about rape',
    'body' : 'Here are his comments about the case'
  }

  if parser.is_article_hit(news_dict) is True:
    print 'article is a hit'
  else:
    print 'article is a blunt!'
