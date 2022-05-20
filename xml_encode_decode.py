# import base64

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

xml_string = xml_responses.xml_data["employee"]

print(xml_string)

root = ET.fromstring(xml_string)
print("type of root")
print(type(root))

print("===")
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag)