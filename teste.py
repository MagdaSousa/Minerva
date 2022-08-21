magda = '5%'
import re

number_pattern = re.compile('^[0-9]+$')
string_pattern = re.compile('^[a-zA-Z]+$')
if re.search(number_pattern, magda):
    print("tem")

