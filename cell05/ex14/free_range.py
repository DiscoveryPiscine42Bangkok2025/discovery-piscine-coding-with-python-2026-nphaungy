#!/usr/bin/env python
import sys
if len(sys.argv) == 3:
    my_range = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
    print(my_range)
else:
    print("none")