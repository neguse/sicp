#!/bin/bash
# Fix translated node references back to English

# Fix chapter references
sed -i 's/第1章/Chapter 1/g; s/第2章/Chapter 2/g; s/第3章/Chapter 3/g; s/第4章/Chapter 4/g; s/第5章/Chapter 5/g' sicp-pocket-ja.texi

# Fix figure references (図 X.Y → Figure X.Y)
sed -i 's/図 \([0-9]\+\.[0-9]\+\)/Figure \1/g' sicp-pocket-ja.texi

# Fix exercise references (練習問題 X.Y → Exercise X.Y)
sed -i 's/練習問題 \([0-9]\+\.[0-9]\+\)/Exercise \1/g' sicp-pocket-ja.texi

echo "Node references fixed"
