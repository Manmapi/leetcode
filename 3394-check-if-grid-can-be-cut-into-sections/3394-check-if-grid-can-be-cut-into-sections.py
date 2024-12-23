class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Similar to meeting room
        ver = []
        hor = []
        n = len(rectangles)
        for x_start, y_start, x_end, y_end in rectangles:
            ver.append((x_start, x_end))
            hor.append((y_start, y_end))
        ver.sort()
        hor.sort()
        # Now, loop over and check
        count_ver = 0
        count_hor = 0
        curr_ver = ver[0][1]
        curr_hor = hor[0][1]
        for i in range(1, n):
            if curr_ver <= ver[i][0]:
                count_ver += 1
            if curr_hor <= hor[i][0]:
                count_hor += 1
            curr_ver = max(curr_ver, ver[i][1])
            curr_hor = max(curr_hor, hor[i][1])
        return count_ver >= 2 or count_hor >= 2