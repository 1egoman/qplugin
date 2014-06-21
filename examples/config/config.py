# basic plugin
# example by Ryan Gaus
from base import *
import os, json


class config_parser(parser):
  """ a parser that shows how to use a config file """
  
  # tells the main program if it should use this plugin to parse its query
  # the query is contained within self.query
  def validate(self):
    return "phrase" in self.query

  # the real code of the plugin, this should parse the incoming
  # query (again, self.query) and return status information
  def parse(self, parent):

    # open config
    with open(os.path.join(self.get_plugin_dir(__file)__), "config.json") as f:
      config = json.loads( f.read() )

    # the response
    self.resp["text"] = config["phrase"]
    self.resp["type"] = "basic"
    self.resp["status"] = STATUS_OK
    
    # return the query
    return self.resp
