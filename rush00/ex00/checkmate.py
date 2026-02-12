#!/usr/bin/env python
def checkmate(board):
    if not isinstance(board, str): 
        return
    try:
        if not board: return 
        rows = board.strip().split('\n')
        if not rows: return
        h = len(rows)
        w = len(rows[0])
        if h == 0 or w == 0: return 
        for r in rows:
            if len(r) != w: return
        if board.count('K') != 1: return 
        k_position = None
        for r in range(h):
            for c in range(w):
                if rows[r][c] == 'K':
                    k_position = (r, c)
                    break
            if k_position: break
        if not k_position: return 
        k_row, k_col = k_position
        #ลูปหา R กับ Q ที่จะกินคิง
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            curr_r, curr_c = k_row + dr, k_col + dc
            while 0 <= curr_r < h and 0 <= curr_c < w:
                p = rows[curr_r][curr_c]
                if p in ['R', 'Q']:
                    print("Success")
                    return
                if p in ['P', 'B']: 
                    break
                curr_r += dr
                curr_c += dc
        #ลูปหา B กับ Q และ P ที่จะกินคิง
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            curr_r, curr_c = k_row + dr, k_col + dc
            dist = 0
            while 0 <= curr_r < h and 0 <= curr_c < w:
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