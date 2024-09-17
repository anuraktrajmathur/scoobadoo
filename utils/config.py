
import yaml
from dotmap import DotMap

def extract_from_yml(yml_file):
    with open(yml_file, 'r') as file:
        yml_content = yaml.safe_load(file)
    return DotMap(yml_content)