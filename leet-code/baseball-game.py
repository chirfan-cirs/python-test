class Solution(object):
    def calPoints(self, operations):
        stack = []
        for ope in operations:
            if ope == 'D':
                stack.append(stack[-1]*2)
            elif ope == 'C':
                stack.pop()
            elif ope == '+':
                stack.append(stack[-1] + stack[-2])
        return sum(stack)


"""
:type operations: List[str]
:rtype: int
"""
