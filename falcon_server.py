from HitStore import HitStore
import falcon
import json


class NewsResource(object):

  def __init__(self, hits_resource):
    """
    Initialization
    1. Read data file
    2. Load as JSON
    3. populate self.data?
    """
    self.hit_data = hits_resource

  def on_get(self, req, resp):
    """
    Handles GET requests
    """
    total_hits = self.hit_data.get_total_hits()
    article_list = self.hit_data.get_article_list()

    resp.body = json.dumps({
      'name' : 'Rodrigo Duterte',
      'total_hits' : total_hits,
      'article_list' : article_list
    })

api = falcon.API()

# Long-lived class instances
# newsParser = NewsParser()
du_hitStore = HitStore('duterte', 'rodrigo')
newsResource = NewsResource(du_hitStore)

# URL path routing handlers mapping
api.add_route('/', newsResource)
