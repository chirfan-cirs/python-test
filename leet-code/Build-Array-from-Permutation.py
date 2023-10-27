class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
"""
:type nums: List[int]
:rtype: List[int]

Konsep "indexing into an array", di mana menggunakan nilai dari satu elemen array 
sebagai indeks untuk mengakses elemen lainnya. Dalam kasus ini, nums[i] adalah indeks yang digunakan 
untuk mengakses elemen nums lainnya, dan nilai dari indeks ini disimpan di dalam ans.
"""
