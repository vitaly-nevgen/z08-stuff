import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('quiz_xml.xml')
root = tree.getroot()

# Structure description of the new feed
root_feed = ET.Element("root")
results = ET.SubElement(root_feed, "results")
sport = ET.SubElement(results, "sport")
sport_q1 = ET.SubElement(sport, "q1")
ET.SubElement(sport_q1, "result1").text = 'True'
ET.SubElement(sport_q1, "result2").text = 'False'
ET.SubElement(sport_q1, "result3").text = 'True'

math = ET.SubElement(results, "math")
math_q1 = ET.SubElement(math, "q1")
ET.SubElement(math_q1, "result1").text = 'False'

math_q2 = ET.SubElement(math, "q2")
ET.SubElement(math_q2, "result1").text = 'False'

# Realization of the pretty xml form
str_feed_data = minidom.parseString(ET.tostring(root_feed)).toprettyxml(indent="   ")
elem_feed_data = ET.fromstring(str_feed_data)

# Appending of the created feed xml to the existed data
root.extend(elem_feed_data)

# Transform data to the ElementTree type for the following processing
tree = ET.ElementTree(root)
tree.write("quiz_xml.xml")