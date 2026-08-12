from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        box_map = defaultdict(list)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row_map.get(i, []):
                    #print(f' i: {i} amf j:{j}')
                    return False
                if num in col_map.get(j, []):
                    #print(f' i: {i} amf j:{j}')
                    return False
                if num in box_map.get((i//3, j//3), []):
                    return False
                row_map[i].append(num)
                col_map[j].append(num)
                box_map[(i//3, j//3)].append(num)
        return True