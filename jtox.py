import json
import xml.etree.ElementTree as ET
import argparse

# Функція для перетворення JSON у XML
def json_to_xml(json_data):
    root = ET.Element('data')
    for key, value in json_data.items():
        if isinstance(value, dict):
            sub = ET.SubElement(root, key)
            sub.extend(json_to_xml(value))
        elif isinstance(value, list):
            for item in value:
                sub = ET.SubElement(root, key)
                sub.extend(json_to_xml(item))
        else:
            sub = ET.SubElement(root, key)
            sub.text = str(value)
    return root

# Функція для перетворення XML у JSON
def xml_to_json(xml_data):
    if len(xml_data) == 0:
        return xml_data.text
    result = {}
    for child in xml_data:
        child_result = xml_to_json(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_result)
            else:
                result[child.tag] = [result[child.tag], child_result]
        else:
            result[child.tag] = child_result
    return result

# Опції командного рядка
parser = argparse.ArgumentParser(description='Convert JSON to XML or vice versa.')
parser.add_argument('input_file', metavar='input_file', type=str, help='Input file name')
parser.add_argument('input_format', metavar='input_format', type=str, help='Input file format (JSON or XML)')
parser.add_argument('output_file', metavar='output_file', type=str, help='Output file name')
parser.add_argument('output_format', metavar='output_format', type=str, help='Output file format (JSON or XML)')

# Зчитуємо опції командного рядка
args = parser.parse_args()

# Зчитуємо дані з вхідного файлу
with open(args.input_file, 'r') as f:
    if args.input_format.lower() == 'json':
        data = json.load(f)
    elif args.input_format.lower() == 'xml':
        tree = ET.parse(f)
        data = xml_to_json(tree.getroot())

# Записуємо дані до вихідного файлу
with open(args.output_file, 'w') as f:
    if args.output_format.lower() == 'json':
        json.dump(data, f, indent=4)
    elif args.output_format.lower() == 'xml':
        root = json_to_xml(data)
        tree = ET.ElementTree(root)
        tree.write(f, encoding='unicode', xml_declaration=True)
