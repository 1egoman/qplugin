# basic plugin
# example by Ryan Gaus
from base import *


class basic_parser(parser):
  """ A basic, demo parser for quail """
  
  # tells the main program if it should use this plugin to parse its query
  # the query is contained within self.query
  def validate(self):
    return "phrase" in self.query

  # the real code of the plugin, this should parse the incoming
  # query (again, self.query) and return status information
  def parse(self, parent):

    # the response
    self.resp["text"] = "This is a sample response!"

    # an id: give your plugin a unique one, it is used to distinguish
    # which plugins made queries
    self.resp["type"] = "basic"

    # the query went fine! Also, STATUS_ERR for a general error, or
    # STATUS_NO_HIT if the program couldn't find what it was looking for
    self.resp["status"] = STATUS_OK
    
    # return the query
    return self.resp
