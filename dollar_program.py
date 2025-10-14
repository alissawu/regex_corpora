import re
import sys

def extract_dollar_amounts(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'(?:[$][0-9\,]+(?:\.[0-9]+)?(?:\s(?:hundred|thousand|million|billion|trillion|gazillion))?)|(?:(?:(?:[0-9]+(?:[0-9\,]+)?(?:\.[0-9]+)?)|one|two|three|four|five|six|seven|eight|nine|ten|tens|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|half|quarter|a)\s)+(?:(?:(?:(?:[0-9]+(?:[0-9\,]+)?(?:\.[0-9]+)?)|one|two|three|four|five|six|seven|eight|nine|ten|tens|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|half|quarter|a|of|hundred|hundreds|thousand|thousands|million|millions|billion|billions|trillion|trillions|gazillion)\s)+)?\b(?:dollar|dollars|cent|cents)\b'
    match = re.findall(pattern, content, re.IGNORECASE | re.VERBOSE)

    # Write found dollar amounts to output file
    with open('dollar_output.txt', 'w', encoding='utf-8') as output_file:
        for amt in match:
            output_file.write(amt.strip() + '\n')

def main():
    extract_dollar_amounts(sys.argv[1])

if __name__ == '__main__':
    main()
