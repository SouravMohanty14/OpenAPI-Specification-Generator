from xmlrpc.client import Boolean
import json
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader
import API

api_dict = {}

securitySchemes = { "bearerAuth": False, "cookieAuth": False, "oauthsecurity": False, "oauthAuthorizeCode": False, "basicAuth": False }

#Erase Spec File
open('spec.yaml', 'w').close()

#Get Description data from Json File
file = open('./data/descriptions.json',) 
descriptions = json.load(file)
file.close()

#Format
file = open('./data/format.json',) 
format = json.load(file)
file.close()

def get_security(key):
    if key not in securitySchemes.keys():
        return False
    return securitySchemes[key]

def set_security(key):
    securitySchemes.update({key: True})
    return True

def security_not_empty(value):
    res = all(x == False for x in securitySchemes.values())
    return not res

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
    return type(value)

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

def generate_api_object():
    obj = API.API_Obj()

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

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

    # Opening template file
    template = env.get_template('openapi-template.yaml')
    print ("Template loaded successfully...")

    for path in api_dict:
        api_list = api_dict[path]
        for api in api_list:
            with open("spec.yaml", "a") as spec_file:
                print("Creating specification for " + api.path)
                spec = template.render(api=api)
                spec_file.write(spec)
                spec_file.close()

    # Opening template file
    component_template = env.get_template('components-template.yaml')
    print ("Component Template loaded successfully...")
    with open("spec.yaml", "a") as spec_file:
        print("Writing Components")
        components = component_template.render()
        spec_file.write(components)
        spec_file.close()

    print("Specification created successfully")

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
        generate_api_object()
    elif choice == '2':
        print ("Generating Open API Specification")
        generate_api_spec()
    else:
        print ("Generating Open API Specification")
        generate_api_spec()
        print ("Exiting.")
        runner = False
