class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Characters used by target prefix
        used = [0] * 26

        for i in range(len(target) - 1, -1, -1):

            # Try to make target[0:i] equal to the target
            # We reconstruct the availability for this prefix.
            temp = freq[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if temp[x] == 0:
                    possible = False
                    break

                temp[x] -= 1

            if not possible:
                continue

            # At position i, find the smallest character
            # greater than target[i].
            current = ord(target[i]) - ord('a')

            for c in range(current + 1, 26):
                if temp[c] > 0:

                    temp[c] -= 1

                    # Remaining characters in sorted order
                    ans = target[:i] + chr(c + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * temp[k]

                    return ans

        return ""