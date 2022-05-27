# import base64
import re

# with open('./data/requestBody.xml', "rb") as file:
#     encoded = base64.encodebytes(file.read()).decode("utf-8")

# # output base64 content    
# print(encoded)

# decoded = base64.decodebytes(encoded.encode('utf-8'))

# # write decoded base64 content to file
# with open("output.xml", "wb") as file:
#     file.write(decoded)

# # output decoded base64 content
# print(decoded.decode('utf-8'))

import xml.etree.ElementTree as ET
import data.xmlResponses as xml_responses

#xml_string = xml_responses.xml_data["Book"]

# xml_string = '''<smp:book xmlns:smp="http://example.com/schema">
# xml:
#     prefix: 'smp'
#     namespace: 'http://example.com/schema'
# </smp:book>'''

xml_string = '''<book xmlns:smp="http://example.com/schema">
xml:
    prefix: 'smp'
    namespace: 'http://example.com/schema'
</smp:book>'''

#print(xml_string)

#root = ET.fromstring(xml_string)
# print("type of root")
# print(type(root))

# print("===")
# print(root.tag)
# print(root.attrib)
# for child in root:
#     print(child.tag)

#ns = re.match(r'{.*}', root.tag).group(0)

first_line = xml_string.partition('\n')[0]
print(first_line)
# first_line.rstrip('<')
# first_line.rstrip('>')
# print(first_line)
list1 = []
list1 = first_line.split(' ')
# print(type(list1))
# list1[0].translate('<')
# print(list1[0])
list1[0] = list1[0].strip('<')
# print(list1[0])
n = len(list1)
list1[n-1] = list1[n-1].strip('>')
print(list1)

prefix,roottag = list1[0].split(':')

print(prefix)
print(roottag)