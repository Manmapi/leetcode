class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ["a", "e", "i", "o", "u"]
        l = len(s)
        v_indexes = []
        for i in range(l):
            if s[i].lower() in v:
                v_indexes.append(i)
        l_v = len(v_indexes)
        str_list = list(s)
        for j in range(l_v//2):
            m, n = v_indexes[j], v_indexes[l_v-1-j]
            str_list[m], str_list[n] = str_list[n], str_list[m]
        return "".join(str_list)

