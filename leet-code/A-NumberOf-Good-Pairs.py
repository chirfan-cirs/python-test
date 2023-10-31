class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
"""
:type nums: List[int]
:rtype: int

Implementasi ini menggunakan dua loop bersarang (nested loops) untuk membandingkan setiap elemen dalam 
daftar dengan elemen-elemen lainnya. Dengan menggunakan dua loop ini, kode membandingkan setiap pasangan 
elemen secara berurutan. Jika dua elemen dalam daftar memiliki nilai yang sama (identik), maka variabel 
count akan bertambah satu. Variabel count awalnya diatur sebagai 0 dan akan menyimpan jumlah pasangan 
angka identik yang ditemukan.

"""
