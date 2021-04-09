"""
Split number by dots and commas
"""
regex_pattern = r"[.,]" # pattern for splitting 

import re
print("\n".join(re.split(regex_pattern, input())))

