class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        data = [0] * 6
        for i in range(2):
            for j in range(3):
                val = board[i][j]
                data[3 * i + j] = val 
        q = [tuple(data)]
        visited = set()
        count = 0
        while q:
            q_new = []
            for val in q:
                if val == (1, 2, 3, 4, 5, 0):
                    return count
                zero_index = val.index(0)
                next_idxes = []
                if zero_index != 0 and zero_index != 3:
                    next_idxes.append(zero_index - 1)
                if zero_index != 2 and zero_index != 5:
                    next_idxes.append(zero_index + 1)
                if zero_index >= 3:
                    next_idxes.append(zero_index - 3)
                else:                    
                    next_idxes.append(zero_index + 3)
                for next_idx in next_idxes:
                    new_val = list(val)
                    new_val[zero_index] = new_val[next_idx]
                    new_val[next_idx] = 0
                    new_val = tuple(new_val)
                    if new_val not in visited:
                        visited.add(new_val)
                        q_new.append(new_val)
            count += 1
            q = q_new
        return -1