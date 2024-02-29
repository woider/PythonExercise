def quick_sort_recursion(nums, start, end):
    if end > start:
        mid = start + (end - start) // 2
        quick_sort_recursion(nums, start, mid)
        quick_sort_recursion(nums, mid + 1, end)
        
def quick_sort(nums):
    quick_sort_recursion(nums, 0, len(nums) - 1)
    return nums