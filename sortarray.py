class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, l, r):
            i = l - 1  # index of smaller element
            pivot = r  # pivot index

            for j in range(l, r):
                # If current elemnt is smaller element than or equal to pivot value
                if arr[j] <= arr[pivot]:
                    i += 1  # In crement index of smaller element to make a room to place it
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
            return i + 1

        def quick_sort(arr, l, r):
            if l < r:
                pi = partition(arr, l, r)
                quick_sort(arr, l, pi - 1)
                quick_sort(arr, pi + 1, r)

        quick_sort(nums, 0, len(nums) - 1)
        return nums