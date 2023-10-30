
# Using Build-in function
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# Not Using Build-in function
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(n):
            # Menghitung jumlah digit 1 dalam representasi biner dari n
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count

        # Menggunakan lambda untuk mengurutkan array berdasarkan jumlah digit 1 dan nilai
        return sorted(arr, key=lambda x: (count_ones(x), x))

"""
Mengurutkan nilai integer bedasarkan nilai binary code nya. Permasalahan ini memanfaatkan build-in Function
bin() dari bahasa pemrograman yang digunakan (Python).

Dan menyelesaikannya tanpa menggunakan Function yang sudah disediakan
"""