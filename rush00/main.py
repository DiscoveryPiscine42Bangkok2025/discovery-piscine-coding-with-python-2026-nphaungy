#!/usr/bin/env python
from checkmate import checkmate
"""def run_test(name, input_data):
    print(f"Testing: {name}")
    print(f"Input type: {type(input_data)}")
    print("Result: ", end="")
    try:
        checkmate(input_data)
        print("(No Crash)") # บรรทัดนี้ต้องขึ้นเสมอ
    except Exception as e:
        print(f"CRASHED! Error: {e}")
    print("-" * 30)"""
def main():
    board = ""   
    checkmate(board)
    board = """\
.K..
.R..
..K.
....\
"""
    checkmate(board)
    board = """\
....
...
....\
"""
    checkmate(board)
    board = """\
....
.P..
....\
"""
    checkmate(board)
    board = """\
....
.P..
..K.\
"""
    checkmate(board)
    board = """\
....
.K..
..P.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()