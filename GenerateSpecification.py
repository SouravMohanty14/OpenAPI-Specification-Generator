from xmlrpc.client import Boolean
import json
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader
import API

api_dict = {}

#Erase Spec File
open('spec.yaml', 'w').close()

def get_type(value):
    print(type(value))
    if type(value) == str:
        return "string"
    if type(value) == float:
        return "number"
    if type(value) == int:
        return "integer"
    if type(value) == bool:
        return "boolean"
    return type(value)

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
        print ("Exiting.")
        runner = False
