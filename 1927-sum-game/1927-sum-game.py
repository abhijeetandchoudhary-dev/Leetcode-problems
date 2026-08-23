class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        diff = 0
        qL = 0
        qR = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    qL += 1
                else:
                    qR += 1
            else:
                if i < half:
                    diff += int(ch)
                else:
                    diff -= int(ch)

        if (qL + qR) % 2 == 1:
            return True

        return 2 * diff != 9 * (qR - qL)