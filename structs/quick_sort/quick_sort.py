# lb - lower bound
# ub - upper bound

def partition(nums, lb, ub):
    pivot = nums[lb]
    start = lb
    end = ub

    while start < end:
        while nums[start] <= pivot:
            start += 1
        while nums[end] > pivot:
            end -= 1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]
    
    nums[lb], nums[end] = nums[end], nums[lb]
    return end


def quick_sort(nums, lb, ub):
    if lb < ub:
        loc = partition(nums, lb, ub)
        quick_sort(nums, lb, loc - 1)
        quick_sort(nums, loc + 1, ub)