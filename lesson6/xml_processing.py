import xml.etree.ElementTree as ET

tree = ET.parse('quiz_xml.xml')

root = tree.getroot()

results = ET.SubElement(root, "results")
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

tree = ET.ElementTree(root)
tree.write("quiz_xml.xml")