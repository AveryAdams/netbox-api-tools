import yaml
import json


def open_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            j_print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


def j_print(jsn, indent=2):
    print(json.dumps(jsn, indent=indent))


def main():
    fn = 'sites.yml'
    j_print(open_yaml_file(fn))


main()

