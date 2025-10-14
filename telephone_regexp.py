import re
import sys

def extract_phone_numbers(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'[^0-9\/]((?:\(?\d{3}\)?.?)\d{3}.?\d{4})[^0-9\/]'

    match = re.findall(pattern, content)

    with open('telephone_output.txt', 'w', encoding='utf-8') as output_file:
        for phone_number in match:
            output_file.write(str(phone_number).strip() + '\n')


def main():
    extract_phone_numbers(sys.argv[1])

if __name__ == '__main__':
    main()
