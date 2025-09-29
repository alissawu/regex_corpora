# call w/text file as a parameter, output regexp matches in format below (?) like lines?
# output dollar_output.txt

import sys
import re

# sys.argv[0] is the script name
# python dollar_program.py all-OANC.txt 
# add > dollar_output.txt to put the standard output (terminal stream) into the txt
filename = sys.argv[1] 

money = ["dollar", "dollars", "cent", "cents"]
magnitudes = ["hundred", "thousand", "ten-thousand", "million", "billion"]

'''
Branch A = Starting with $
Branch B = Starting with integer
'''

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    #?: = group/include but not only this. ?after means optional
    A = r"\$[0-9.,]+ ?+(?:thousand|million|billion|trillion)s?"
    B = r"\"[0-9.,]+ ?+(?:thousand|million|billion|trillion)+(?:dollar|cent)s?"
    match = re.findall()
    print(match)

    
