#!/usr/bin/env python3
"""Remove duplicate @anchor definitions"""

lines_to_delete = {10277, 14541, 28085}

with open('sicp-pocket-ja.texi', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('sicp-pocket-ja.texi', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines, 1):
        if i not in lines_to_delete:
            f.write(line)

print(f"Deleted {len(lines_to_delete)} duplicate anchor lines")
