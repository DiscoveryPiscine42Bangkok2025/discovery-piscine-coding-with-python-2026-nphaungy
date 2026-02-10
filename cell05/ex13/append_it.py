#!/usr/bin/env python
import sys
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
            print(arg + "ism")
else:
    print("none")