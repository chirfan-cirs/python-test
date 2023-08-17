class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        n = 0

        for i in hours:
            if i >= target:
                n += 1

        return n
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
