import re
def check(pattern, string):
    return bool(re.match(pattern, string))