class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


"""
Mengurutkan nilai integer bedasarkan nilai binary code nya. Permasalahan ini memanfaatkan build-in Function
bin() dari bahasa pemrograman yang digunakan (Python), dengan menggunakan key nya adalah lambda yang nantinya 
akan mengembalikan nilai tuple.
"""