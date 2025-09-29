# finds telephone numbers
# output telephone_output.txt
#!/usr/bin/env python3
import sys
import re

filename = sys.argv[1]

# separators (space, dot, dash)
SEP = r"""[\s.\-]"""

# area code forms
AREA_PARENS = r"""\(\s*\d{3}\s*\)"""   # (212)
AREA_PLAIN  = r"""\d{3}"""             # 212

# exchange + line
EXCH = r"""\d{3}"""
LINE = r"""\d{4}"""

# optional country code (+1 or 1) with optional separator
CC   = rf"""(?:\+?1(?:{SEP})?)"""

# optional extension ("ext", "ext.", "x", or "#") + 1–5 digits
EXT  = r"""(?:\s*(?:ext\.?|x|#)\s*\d{1,5})?"""

# to avoid grabbing parts of longer digit strings, use digit boundaries
# (lookarounds that assert a non-digit around the match)
LEFT_BOUND  = r"""(?<!\d)"""
RIGHT_BOUND = r"""(?!\d)"""

# Branch 1: +1? (AAA) SEP? EXCH SEP? LINE [EXT]
B1 = rf"""{LEFT_BOUND}{CC}?{AREA_PARENS}(?:{SEP})?{EXCH}(?:{SEP})?{LINE}{EXT}{RIGHT_BOUND}"""

# Branch 2: +1? AAA SEP EXCH SEP LINE [EXT]
B2 = rf"""{LEFT_BOUND}{CC}?{AREA_PLAIN}{SEP}{EXCH}{SEP}{LINE}{EXT}{RIGHT_BOUND}"""

# Branch 3: bare 10 digits (no separators, NANP valid), optional leading country code 1, require non alphanumeric boundaries for no IDs
B3 = rf"""(?<![A-Za-z0-9])(?:1)?[2-9]\d{{2}}[2-9]\d{{2}}\d{{4}}(?![A-Za-z0-9])"""


# Branch 4: 7-digit local numbers like 555-1234 or 555 1234 or 555.1234
B4 = rf"""{LEFT_BOUND}\d{{3}}{SEP}\d{{4}}{RIGHT_BOUND}"""

ALL = rf"""(?:{B1}|{B2}|{B3}|{B4})"""

with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

matches = re.findall(ALL, text, re.IGNORECASE)

for m in matches:
    print(m)
