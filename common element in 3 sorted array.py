class Solution:
    def commonElements(self, a, b, c):
        ans = []

        for i in a:
            for j in b:
                for k in c:
                    if i == j and j == k:
                        if i not in ans:
                            ans.append(i)

        return ans