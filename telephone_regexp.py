#!/usr/bin/env python3
# finds telephone numbers
# outputs one match per line
import sys
import re

filename = sys.argv[1]

# separators between phone chunks (space, dot, dash)
SEP = r"""[\s.\-]"""

# NANP-safe area code and exchange (cannot start with 0 or 1)
AREA_PARENS = r"""\(\s*[2-9]\d{2}\s*\)"""   # (212)
AREA_PLAIN  = r"""[2-9]\d{2}"""             # 212
EXCH        = r"""[2-9]\d{2}"""             # 555
LINE        = r"""\d{4}"""                  # 1234

# optional country code (+1 or 1) with optional separator
CC   = rf"""(?:\+?1(?:{SEP})?)"""

# optional extension ("ext", "ext.", "x", or "\#") + 1–5 digits
EXT  = r"""(?:\s*(?:ext\.?|x|\#)\s*\d{1,5})?"""

# boundaries: avoid eating into longer tokens
LEFT_BOUND  = r"""(?<![A-Za-z0-9])"""
RIGHT_BOUND = r"""(?![A-Za-z0-9])"""

# Branch 1: +1? (AAA) SEP? EXCH SEP? LINE [EXT]
B1 = rf"""{LEFT_BOUND}{CC}?{AREA_PARENS}(?:{SEP})?{EXCH}(?:{SEP})?{LINE}{EXT}{RIGHT_BOUND}"""

# Branch 2: +1? AAA SEP EXCH SEP LINE [EXT]
B2 = rf"""{LEFT_BOUND}{CC}?{AREA_PLAIN}{SEP}{EXCH}{SEP}{LINE}{EXT}{RIGHT_BOUND}"""

# Branch 3: 7-digit locals like 555-1234 / 555 1234 / 555.1234
B3 = rf"""{LEFT_BOUND}\d{{3}}{SEP}\d{{4}}{RIGHT_BOUND}"""

# No vanity branches (to match the key more closely)
ALL = rf"""(?:{B1}|{B2}|{B3})"""

with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

matches = re.findall(ALL, text, re.VERBOSE)

for m in matches:
    print(m.strip())
