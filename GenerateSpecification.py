from xmlrpc.client import Boolean
import json
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader
import API

api_dict = {}

securitySchemes = { "bearerAuth": False, "cookieAuth": False, "oauthsecurity": False, "oauthAuthorizeCode": False, "basicAuth": False }

#Info
file = open('./data/info.json',) 
info = json.load(file)
file.close()

filename = "spec.yaml"
try:
  filename = info["title"] + ".yaml"
except:
  filename = "spec.yaml"

schema_file = "schema.yaml"
xml_file = "xml_schema.yaml"

#Erase Spec File
open(filename, 'w').close()
open(schema_file, 'w').close()
open(xml_file, 'w').close()

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

    # Opening info template file
    info_template = env.get_template('info-template.yaml')
    print ("Info Template loaded successfully...")
    with open(filename, "a") as spec_file:
        print("Writing Info")
        info_temp = info_template.render(info=info)
        spec_file.write(info_temp)
        spec_file.close()

    # Opening template file
    template = env.get_template('openapi-template.yaml')
    print ("Template loaded successfully...")

    for path in api_dict:
        api_list = api_dict[path]
        #for api in api_list:
        api = api_list[0]
        with open(filename, "a") as spec_file:
            print("Creating specification for " + api.path)
            spec = template.render(api=api,total_apis=len(api_list))
            spec_file.write(spec)
            spec_file.close()
        #xml schema
        if api.content_type == 'application/xml':
            xml_template = env.get_template('xml-schema.yaml')
            with open(xml_file, "a") as xml_schemas:
                print("Writing Components Schema")
                xml_schema = xml_template.render(api=api,api_list=api_list,total_apis=len(api_list))
                xml_schemas.write(xml_schema)
                xml_schemas.close()
        #AnyOf schema
        if len(api_list) > 1:
            schema_template = env.get_template('components-schema.yaml')
            with open(schema_file, "a") as schemas:
                print("Writing Components Schema")
                schema = schema_template.render(api_list=api_list,total_apis=len(api_list))
                schemas.write(schema)
                schemas.close()

    # Opening components template file
    component_template = env.get_template('components-template.yaml')
    print ("Component Template loaded successfully...")
    with open(filename, "a") as spec_file:
        print("Writing Components")
        components = component_template.render()
        spec_file.write(components)
        spec_file.close()

    data = data2 = data3 = ""
    with open(filename) as fp:
        data = fp.read()
    with open(schema_file) as fp:
        data2 = fp.read()
    with open(xml_file) as fp:
        data3 = fp.read()
    data += "\n"
    data += data2
    data += data3
    open(filename, 'w').close()
    with open (filename, 'a') as fp:
        fp.write(data)

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
