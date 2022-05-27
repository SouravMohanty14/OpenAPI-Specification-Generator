'''Author : Sourav Mohanty, Sukhpreet Kaur
   Code Review : Moorchanna Pattnaik
   Description: It's a Jinja App to generate Open API Specification using JSON data.
   Last Modified On:  17/05/2022 
'''
#Import libraries
from glob import glob
from xmlrpc.client import Boolean
import json
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader
import API
import data.xmlResponses as xml_responses
import xml.etree.ElementTree as ET
import os

#Dictionary to store all the API Objects
api_dict = {}

security_schemes = { "bearerAuth": False, "cookieAuth": False, "oauthsecurity": False, "oauthAuthorizeCode": False, "basicAuth": False }

#A dict to keep track of all xml tags
xml_tags = {}

#Info about API [openapiVersion, title, description, termsOfService, contactName, contactUrl, infoVersion, servers]
try:
    info_file = open('./data/info.json', encoding='utf8') 
    info = json.load(info_file) #Dictionary data of info_file
    info_file.close()
except:
    print("info.json not found")
    exit()

#Specifying yaml file name
filename = "spec.yaml"
try:
  filename = info["title"] + ".yaml"
except:
  filename = "spec.yaml"

#Loading schema & xml files
schema_file = "schema.yaml"
xml_file = "xml_schema.yaml"

#Erase Spec File
try:
    open(filename, 'w', encoding='utf8').close()
    open(schema_file, 'w', encoding='utf8').close()
    open(xml_file, 'w', encoding='utf8').close()
except:
    print("Error occurred while erasing spec files")

#Get Description data from Json File
try:
    descriptions_file = open('./data/descriptions.json', encoding='utf8') 
    descriptions = json.load(descriptions_file)
    descriptions_file.close()
except:
    print("descriptions.json not found")
    exit()

#Get Format data from Json File
try:
    format_file = open('./data/format.json', encoding='utf8') 
    format = json.load(format_file)
    format_file.close()
except:
    print("format.json not found")
    exit()

#Functions for Security Schemes
def get_security(key):
    if key not in security_schemes.keys():
        return False
    return security_schemes[key]

def set_security(key):
    security_schemes.update({key: True})
    return True

def security_not_empty(value):
    res = all(x == False for x in security_schemes.values())
    return not res

#Function to check datatype of parameter using value
def get_type(value):
    #print(type(value))
    if type(value) == str:
        return "string"
    if type(value) == float:
        return "number"
    if type(value) == int:
        return "integer"
    if type(value) == bool:
        return "boolean"
    if type(value) == list:
        return "array"
    if type(value) == dict:
        return "object"
    else:
        return type(value)
    

#Function to check datatype of parameter using value in a nested array
def get_nestedarray_type(value):
    #print(type(value))
    if type(value) == str:
        return "string"
    if type(value) == float:
        return "number"
    if type(value) == int:
        return "integer"
    if type(value) == bool:
        return "boolean"
    if type(value) == list:
        return "object"
    if type(value) == dict:
        return "object"
    return type(value)

#Function to get description for parameter
def get_description(value):
    if value in descriptions:
        return descriptions[value]
    else:
        return ""

def get_format(value):
    if value in format:
        return format[value]
    else:
        return ""

#Function to get xml data from responses.py using param
def get_xml_data(param):
    if param in xml_responses.xml_data.keys():
        return xml_responses.xml_data[param]
    else:
        print("xml data not found, param {}".format(param))

#Function to convert string to XML
def string_to_xml(param):
    #Get xml data as string from responses.py
    xml_string = get_xml_data(param)

    #Initialise xml_tags
    xml_tags = {}

    #Convert xml string to xml
    return ET.fromstring(xml_string)

#Function to get Tags within a xml response
def get_child_name(child_node):
    if(child_node not in xml_tags.keys()):
        xml_tags[child_node] = 1
    else:
        xml_tags[child_node] += 1
    # print("Tag DICT")
    # print(xml_tags)
    # print()
    return "{}{}".format(child_node,xml_tags[child_node])

#Function to reset xml_tags
def reset_xml_tags(value):
    global xml_tags
    xml_tags = {}

#Fuction to check child node present in xml_tags
def child_not_present(child_node):
    #print(child_node.tag)
    global xml_tags
    if(child_node.tag in xml_tags):
        #print("not present")
        return False
    else:
        #print("present")
        return True

#Function to check if Parent node has any children nodes
def child_exists(parent_node):
    count = 0
    for child in parent_node:
        count += 1
    if count>0:
        return True #has children
    else:
        return False #no children

#
def generate_api_object():
    #Creating API Object
    obj = API.apiObject()

    if obj.path in api_dict: #Key Exists, Add to Value
        print("adding to value")
        api_list = api_dict[obj.path]
        api_list.append(obj)
    else:
        print("new pair")
        api_list = [] 
        api_list.append(obj)
        api_dict.update({obj.path: api_list})

    print("Object created for {}".format(obj.path))

def generate_api_spec():

    #Registering Filters
    jinja2.filters.FILTERS['get_type'] = get_type
    jinja2.filters.FILTERS['get_description'] = get_description
    jinja2.filters.FILTERS['get_nestedarray_type'] = get_nestedarray_type
    jinja2.filters.FILTERS['get_format'] = get_format
    jinja2.filters.FILTERS['get_security'] = get_security
    jinja2.filters.FILTERS['set_security'] = set_security
    jinja2.filters.FILTERS['security_not_empty'] = security_not_empty
    jinja2.filters.FILTERS['get_xml_data'] = get_xml_data
    jinja2.filters.FILTERS['string_to_xml'] = string_to_xml
    jinja2.filters.FILTERS['get_child_name'] = get_child_name
    jinja2.filters.FILTERS['reset_xml_tags'] = reset_xml_tags
    jinja2.filters.FILTERS['child_not_present'] = child_not_present
    jinja2.filters.FILTERS['child_exists'] = child_exists

    #try:
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

    # Opening info template file
    info_template = env.get_template('info-template.yaml')
    print ("Info Template loaded successfully...")
    try:
        with open(filename, "a", encoding='utf8') as spec_file:
            print("Writing Info")
            info_temp = info_template.render(info=info)
            spec_file.write(info_temp)
            spec_file.close()
    except:
        print("Error while writing Info template")

    # Opening template file
    template = env.get_template('openapi-template.yaml')
    print ("Template loaded successfully...")

    for path in api_dict:
        api_list = api_dict[path]
        #for api in api_list:
        api = api_list[0]
        try:
            with open(filename, "a", encoding='utf8') as spec_file:
                print("Creating specification for " + api.path)
                spec = template.render(api=api,total_apis=len(api_list))
                spec_file.write(spec)
                spec_file.close()
        except:
            print("Error while writing path for api:{},path:{}".format(api,path))
        #xml schema
        #if api.content_type == 'application/xml':
        xml_template = env.get_template('xml-schema.yaml')
        try:
            with open(xml_file, "a", encoding='utf8') as xml_schemas:
                print("Writing Schemas")
                xml_schema = xml_template.render(api=api,api_list=api_list,total_apis=len(api_list))
                xml_schemas.write(xml_schema)
                xml_schemas.close()
        except:
            print("Error while writing schemas for api:{},path:{}".format(api,path))
        #AnyOf schema
        if len(api_list) > 1:
            schema_template = env.get_template('components-schema.yaml')
            try:
                with open(schema_file, "a", encoding='utf8') as schemas:
                    print("Writing Components Schema")
                    schema = schema_template.render(api_list=api_list,total_apis=len(api_list))
                    schemas.write(schema)
                    schemas.close()
            except:
                print("Error while writing Components for api:{},path:{}".format(api,path))

    # Opening security template file
    component_template = env.get_template('components-template.yaml')
    print ("Security Template loaded successfully...")
    try:
        with open(filename, "a", encoding='utf8') as spec_file:
            print("Writing Security")
            components = component_template.render()
            spec_file.write(components)
            spec_file.close()
    except:
        print("Error while writing Security for api:{},path:{}".format(api,path))

    data = data2 = data3 = ""
    try:
        with open(filename, encoding='utf8') as fp:
            data = fp.read()
        with open(schema_file, encoding='utf8') as fp:
            data2 = fp.read()
        with open(xml_file, encoding='utf8') as fp:
            data3 = fp.read()
        data += "\n"
        if((data2 + data3) != ""):
            data += "\n  schemas:"
        data += data2
        data += data3
        open(filename, 'w', encoding='utf8').close()
        with open (filename, 'a', encoding='utf8') as fp:
            fp.write(data)
    except:
        print("Error while writing Specification")

    print("Specification created successfully")
    # except Exception as e:
    #     print("Error while generating Specification")
    #     exc_type, exc_obj, exc_traceback = sys.exc_info()
    #     fname = os.path.split(exc_traceback.tb_frame.f_code.co_filename)
    #     print(exc_type) #Exception
    #     print(fname) #Exception occured in which file
    #     print(exc_traceback.tb_lineno) #Exception lineno

if __name__ == "__main__":

  print ("Enter: ")
  print ("  [1] to add API Object")
  print ("  [2] to generate Open API Specification")
  print (" 0 to exit ")
  
  runner = True

  while runner:
    # input
    choice = str(input())
    
    if choice == '1':
        try:
            generate_api_object()
        except:
            print("Error occured while adding API Object")
    elif choice == '2':
        print ("Generating Open API Specification")
        try:
            generate_api_spec()
        except Exception as e:
            print("Error occured while Generating Specification")
            # except Exception as e:
    #     print("Error while generating Specification")
            exc_type, exc_obj, exc_traceback = sys.exc_info()
            fname = os.path.split(exc_traceback.tb_frame.f_code.co_filename)
            print(exc_type) #Exception
            print(fname) #Exception occured in which file
            print(exc_traceback.tb_lineno) #Exception lineno
    else:
        print ("Generating Open API Specification")
        generate_api_spec()
        print ("Exiting.")
        runner = False
