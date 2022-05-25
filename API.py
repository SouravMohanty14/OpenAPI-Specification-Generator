import json
import xml.etree.ElementTree as ET

class apiObject:
  def __init__(self):

    try:
      file = open('./data/data.json', encoding='utf8')
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
    except:
      print("Error while opening/reading data.json file")

    try:
      file = open('./data/parameters.json', encoding='utf8') 
      self.parameters = json.load(file)
      file.close()
    except:
      print("Error while opening/reading parameters.json file")

    #file = open('./data/requestBody.json',)
    if self.content_type=='application/json':
      try:
        file = open('./data/requestBody.json', encoding='utf8')
        self.requestBody = json.load(file)
      except:
        print("Error while opening/reading requestBody.json file")
    elif self.content_type=='application/x-www-form-urlencoded':
      try:
        file = open('./data/requestBody.json', encoding='utf8')
        self.requestBody = json.load(file)
      except:
        print("Error while opening/reading requestBody.json file")
    else:
      try:
        file = open('./data/requestBody.xml', encoding='utf8')
        self.requestBody = ET.parse(file)
      except:
        print("Error while opening/reading requestBody.xml file")
    
    file.close()

    try:
      file = open('./data/responses.json', encoding='utf8') 
      self.responses = json.load(file)
      file.close()
    except:
      print("Error while opening/reading responses.json file")