#!/usr/bin/env python
import sys
if len(sys.argv) == 2:
    input_str = sys.argv[1]
    number_z = input_str.count('z')
    if number_z > 0:
        print("z" * number_z)
    else:
        print("none")
else:
    print("none")