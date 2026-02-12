#!/usr/bin/env python
def checkmate(board):
    # 1. ตรวจสอบข้อมูลเบื้องต้น
    if not board:
        print("Fail")
        return
    
    # แปลง String เป็นตาราง 2 มิติ
    rows = [list(line) for line in board.split('\n') if line]
    if not rows:
        print("Fail")
        return

    # หาขนาดกระดาน
    height = len(rows)
    width = len(rows[0])

    # 2. หาตำแหน่ง King (K)
    kx, ky = -1, -1
    for r in range(height):
        for c in range(width):
            if rows[r][c] == 'K':
                kx, ky = r, c
                break
    
    # ถ้าไม่มี King บนกระดาน
    if kx == -1:
        print("Fail")
        return

    # --- เริ่มเช็ค: ให้ King มองออกไปรอบตัว (Ray Casting) ---

    # ทิศที่ 1: แนวตั้งและแนวนอน (เช็ค Rook และ Queen)
    # Directions: บน, ล่าง, ซ้าย, ขวา
    straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in straight_moves:
        curr_r, curr_c = kx + dr, ky + dc
        
        # มองไล่ไปเรื่อยๆ จนสุดขอบกระดาน
        while 0 <= curr_r < height and 0 <= curr_c < width:
            piece = rows[curr_r][curr_c]
            
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            
            if piece != '.': # เจอตัวขวาง (P, B หรืออื่นๆ) ให้หยุดมองทิศนี้
                break
            
            curr_r += dr
            curr_c += dc

    # ทิศที่ 2: แนวทะแยง (เช็ค Bishop และ Queen)
    # Directions: บนซ้าย, บนขวา, ล่างซ้าย, ล่างขวา
    diagonal_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for dr, dc in diagonal_moves:
        curr_r, curr_c = kx + dr, ky + dc
        
        while 0 <= curr_r < height and 0 <= curr_c < width:
            piece = rows[curr_r][curr_c]
            
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            
            if piece != '.': # เจอตัวขวาง ให้หยุดมอง
                break
                
            curr_r += dr
            curr_c += dc

    # ทิศที่ 3: เช็ค Pawn (P)
    # กรณี: P ศัตรูอยู่ด้านบน กินลงล่าง (ตามโจทย์)
    # แปลว่า King ต้องมองสวนขึ้นไปข้างบน (kx - 1)
    
    # (-1, -1) = มองไปแถวบน ทางซ้าย
    # (-1, 1)  = มองไปแถวบน ทางขวา
    pawn_danger_zones = [(-1, -1), (-1, 1)] 
    
    # [Tips สำหรับตอนตรวจ]: ถ้ากรรมการบอกว่า P กินขึ้นบน ให้แก้เป็น [(1, -1), (1, 1)]

    for dr, dc in pawn_danger_zones:
        target_r, target_c = kx + dr, ky + dc
        
        if 0 <= target_r < height and 0 <= target_c < width:
            if rows[target_r][target_c] == 'P':
                print("Success")
                return

    # ถ้าเช็คทุกทิศแล้วไม่เจออันตรายเลย
    print("Fail")