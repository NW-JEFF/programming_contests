"""Test."""

import os

n = 2
for i in range(1, n+1):
    os.system(f'cat 19C_test{i}.txt | python 19C.py')