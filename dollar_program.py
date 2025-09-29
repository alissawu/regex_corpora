#!/usr/bin/env python3
import sys
import re

filename = sys.argv[1]

# integers - numbers, commas, decimals
INT = r"""
(?:                             # non-capturing
    (?:\d{1,3}(?:,\d{3})+|\d+)  # commas or just digits
    (?:\.\d+)?                  # optional decimal
)
"""

# magnitudes - verbal
MAG_TALL = r"""(?:thousand|million|billion|trillion)s?"""
MAG_ANY  = rf"""(?:hundred|{MAG_TALL})"""

# currency words
CURR_DOLLAR = r"""dollars?"""
CURR_CENT   = r"""cents?"""

# verbal numbers
ONES  = r"one|two|three|four|five|six|seven|eight|nine"
TEENS = r"ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen"
TENS  = r"twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety"

VERBAL_0_99 = rf"(?:{TENS})(?:-(?:{ONES}))?|{TEENS}|{ONES}"

# 0–999 as words
VERBAL_0_999 = rf"""
(?:
    (?:a|one|{ONES}|{TEENS}|{TENS}(?:-(?:{ONES}))?)
    (?:\s+hundred(?:\s+and\s+{VERBAL_0_99})?)?
  | {VERBAL_0_99}
)
"""

# optional "and ... cents" tail
CENTS_TAIL = rf"""
(?:
    \s*(?:and\s+)?                  # optional "and "
    (?:
        \d{{1,2}}                   # 5, 25, 99
      | {VERBAL_0_99}               # five, twenty-five
    )
    \s+{CURR_CENT}                  # cent/cents
)?
"""
with open(filename, 'r', encoding='utf-8') as file: 
    content = file.read()

    # Branch A: $ + INT + [MAG_TALL] + [dollars] + [and ... cents]
    A = rf"""\$\s*{INT}(?:\s+{MAG_TALL})?(?:\s+{CURR_DOLLAR})?{CENTS_TAIL}"""

    # Branch B: INT + [MAG_TALL] + (dollars|cents) + [and ... cents]
    B = rf"""{INT}(?:\s+{MAG_TALL})?\s+(?:{CURR_DOLLAR}|{CURR_CENT}){CENTS_TAIL}"""

    # Branch C: VERBAL(0–999) + [MAG_ANY] + dollars + [and ... cents]
    # (allows "one hundred dollars", "twenty-five million dollars", etc.)
    C = rf"""{VERBAL_0_999}(?:\s+{MAG_ANY})?\s+{CURR_DOLLAR}{CENTS_TAIL}"""

    # Cents-only 
    D = rf"""(?:{INT}\s+{CURR_CENT}|{VERBAL_0_99}\s+{CURR_CENT})"""

    ALL = rf"""(?:{A}|{B}|{C})\b"""   # add |{D} if you keep cents-only
    pattern = re.compile(ALL, re.IGNORECASE | re.VERBOSE)
    match = re.findall(pattern, content)
    print(match)
