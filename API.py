import json

class API_Obj:
  def __init__(self):

    file = open('./data/data.json',)
    data = json.load(file)

    self.method = data["method"]
    self.path = data["path"]
    self.operationId = data["operationId"]
    self.tag = data["tag"]
    self.summary = data["summary"]
    self.content_type = data["content_type"]
    self.authorization = data["authorization"]
    self.mandatory = data["mandatory"]

    file.close()

    file = open('./data/parameters.json',) 
    self.parameters = json.load(file)
    file.close()

    file = open('./data/requestBody.json',) 
    self.requestBody = json.load(file)
    file.close()

    file = open('./data/responses.json',) 
    self.responses = json.load(file)
    file.close()