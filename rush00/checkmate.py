#!/usr/bin/env python
def checkmate(board):
    if not isinstance(board, str):
        return
    try:
        if not board: return 
        rows = board.strip().split('\n')
        if not rows: return
        height = len(rows)
        width = len(rows[0])
        if height == 0 or width == 0: return
        for r in rows:
            if len(r) != width: return
        if board.count('K') != 1: return
        king_pos = None
        for r in range(height):
            for c in range(width):
                if rows[r][c] == 'K':
                    king_pos = (r, c)
                    break
            if king_pos: break
        if not king_pos: return 
        k_row, k_col = king_pos
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in straight_dirs:
            curr_r, curr_c = k_row + dr, k_col + dc
            while 0 <= curr_r < height and 0 <= curr_c < width:
                p = rows[curr_r][curr_c]
                if p in ['R', 'Q']:
                    print("Success")
                    return
                if p in ['P', 'B']: 
                    break
                curr_r += dr
                curr_c += dc
        for dr, dc in diag_dirs:
            curr_r, curr_c = k_row + dr, k_col + dc
            dist = 0
            while 0 <= curr_r < height and 0 <= curr_c < width:
                dist += 1
                p = rows[curr_r][curr_c]  
                if p in ['B', 'Q']:
                    print("Success")
                    return          
                elif p == 'P':
                    if dr == -1 and dist == 1:
                        print("Success")
                        return
                    else:
                        break 
                elif p == 'R': 
                    break
                curr_r += dr
                curr_c += dc
        print("Fail")
    except Exception:
        return 