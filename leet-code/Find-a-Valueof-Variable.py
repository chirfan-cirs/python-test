# Solution 1
class Solution1(object):
    def finalValueAfterOperations1(self, operations):
        x = 0
        for i in operations:
            if '+' in i:
                x += 1
            elif '-' in i:
                x -= 1
        return x

# Solution 2
class Solution2(object):
    def finalValueAfterOperations2(self, operations):
        x = 0
        for ope in operations:
            if ope[1] == '+':
                x += 1
            elif ope[1] == '-':
                x -= 1
"""
:type operations: List[str]
:rtype: int

Dalam Solusion 1, Penyelesaian memanfaatkan kata(value) yang ada didalam list operations
Dalam Solusiont 2, Penyelesaian memanfaatkan kata(value) yang ada dalam indeks list operations
"""
