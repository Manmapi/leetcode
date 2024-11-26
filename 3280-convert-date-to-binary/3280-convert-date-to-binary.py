class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d, m, y = date.split("-")
        d, m, y = str(bin(int(d)))[2:], str(bin(int(m)))[2:], str(bin(int(y)))[2:]
        return f"{d}-{m}-{y}"