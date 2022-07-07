import sys 
import string

with open('data/2letters.txt', 'w') as f:
    for l1 in string.ascii_lowercase:
        for l2 in string.ascii_lowercase:
            print(l1+l2, file=f)