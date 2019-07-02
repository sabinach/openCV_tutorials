import cv2
import argparse
import re

# instantiate the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('function_name', type=str, help='name of function')

# parse
args = parser.parse_args()

def find_function(name, module=None):
    # if module is None, initialize to the root 'cv2' library
    if module is None:
        module = cv2

    # grab all function names that contain 'name' from the module
    matches = '.*{}.*'.format(name)
    filtered = filter(lambda x: re.search(matches, x, re.IGNORECASE), dir(module))

    return filtered

print('search: {}'.format(args.function_name))
print('found: {}'.format(find_function(args.function_name)))
