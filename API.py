import json
import xml.etree.ElementTree as ET
import config as cfg

#Getting all file paths
info_path = cfg.info_file_path
descriptions_path = cfg.descriptions_file_path
data_path = cfg.data_file_path
parameters_path = cfg.parameters_file_path
requestBody_path = cfg.requestBody_file_path
responses_path = cfg.responses_file_path
format_path = cfg.format_file_path

class apiObject:
  def __init__(self):

    try:
      file = open(data_path, encoding='utf8')
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
    except Exception as e:
      print(e)
      #print("Error while opening/reading data.json file")

    try:
      file = open(parameters_path, encoding='utf8') 
      self.parameters = json.load(file)
      file.close()
    except Exception as e:
      print(e)
      #print("Error while opening/reading parameters.json file")

    #file = open(requestBody_path,)
    if self.content_type=='application/json':
      try:
        file = open(requestBody_path, encoding='utf8')
        self.requestBody = json.load(file)
      except Exception as e:
        print(e)
        #print("Error while opening/reading requestBody.json file")
    elif self.content_type=='application/x-www-form-urlencoded':
      try:
        file = open(requestBody_path, encoding='utf8')
        self.requestBody = json.load(file)
      except Exception as e:
        print(e)
        #print("Error while opening/reading requestBody.json file")
    else:
      try:
        file = open('./data/requestBody.xml', encoding='utf8')
        self.requestBody = ET.parse(file)
      except Exception as e:
        print(e)
        #print("Error while opening/reading requestBody.xml file")
    
    file.close()

    try:
      file = open(responses_path, encoding='utf8') 
      self.responses = json.load(file)
      file.close()
    except Exception as e:
      print(e)
      #print("Error while opening/reading responses.json file")