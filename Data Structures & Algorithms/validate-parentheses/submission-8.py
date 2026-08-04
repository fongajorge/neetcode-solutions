class Solution:
    def isValid(self, s: str) -> bool:
        answer = []

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in brackets:
                answer.append(c)
            else:
                if not answer or brackets[answer[-1]] != c:
                    return False
            
                answer.pop()

        return not answer
        