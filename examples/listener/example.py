from base import *


class exampleParser(parser):
  """ Example Parser """

  def validate(self):
    return "example" in self.query

  def parse(self, parent):

    # return
    self.resp["text"] = "Example Listener Test!"
    self.resp["status"] = STATUS_OK
    return self.resp


def exampleListener(parent):
  """ example listener """

  # send packet to client
  msg = {"status": STATUS_OK, "type": TYPE_PUSH, "text": "test notification!"}
  parent.stack.append(msg)