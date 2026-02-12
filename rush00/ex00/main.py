#!/usr/bin/env python3
from checkmate import checkmate
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
.....
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
.....
..K..
...R.
....Q\
"""
    checkmate(board)
    
    board = """\
P...
....
..K.
....\
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