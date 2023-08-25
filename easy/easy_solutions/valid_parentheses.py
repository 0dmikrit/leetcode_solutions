class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        queue = [k for k in s]
        i = 0
        while i < (len(queue) - 1):
            if queue[i] == symbols.get(queue[i+1]):
                queue.pop(i)
                queue.pop(i)
                i = 0
            else:
                i += 1
        return False if queue else True





