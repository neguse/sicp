#!/usr/bin/env python3
"""Remove duplicate @node and @anchor definitions from sicp-pocket-ja.texi"""

# Lines to delete (second occurrences of duplicates)
lines_to_delete = {
    679, 713, 1809, 1847, 1860, 1886, 3389, 3435, 3597, 3609, 3628, 3638,
    3682, 3778, 3788, 3982, 3987, 4027, 4043, 4052, 4067, 4095, 4103, 4855,
    4885, 4900, 4946, 4975, 4996, 5278, 6172, 6183, 6191, 6200, 6211, 6215,
    6220, 10811, 10877, 20054, 20069, 20171, 24780, 24842, 24888, 24950,
    27019, 27026, 27033, 27071, 28111, 28183
}

with open('sicp-pocket-ja.texi', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('sicp-pocket-ja.texi', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines, 1):
        if i not in lines_to_delete:
            f.write(line)

print(f"Deleted {len(lines_to_delete)} duplicate lines")
