N, M = map(int, input().split())
board = [[0] * 50 for i in range(50)]
rst = 64
whiteboard = [["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"]]
blackboard = [["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"],
              ["BWBWBWBW"],
              ["WBWBWBWB"]]

def white(x, y): #왼쪽 상단이 흰색일때
    cnt = 0
    for RPT in range(y, y+8):
        for rpt in range(x, x+8):
            if whiteboard[RPT - y][0][rpt - x] != board[RPT][rpt]:
                cnt += 1
    return cnt

def black(x, y): #왼쪽 상단이 검은색일때
    cnt = 0
    for RPT in range(y, y+8):
        for rpt in range(x, x+8):
            if blackboard[RPT - y][0][rpt - x] != board[RPT][rpt]:
                cnt += 1
    return cnt

for RPT in range(0,N): #입력 받은 체스판을 보드에 입력
    line = input()
    for rpt in range(0,M):
        board[RPT][rpt] = line[rpt]

for RPT in range(0,N-7): #입력 받은 체스판과 기존의 체스판을 비교
    for rpt in range(0,M-7):
        rst = min(rst,white(rpt,RPT),black(rpt,RPT))
print(rst)