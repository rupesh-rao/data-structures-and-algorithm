def lower_bound(nums, target):
    low, high  = 0, len(nums)-1
    ans = len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid] < target:
            low = mid+1
        else:
            ans = mid
            high = mid-1
    return ans


def upper_bound(nums, target):
    low, high  = 0, len(nums)-1
    ans = len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid] <=target:
            low = mid+1
        else:
            ans = mid
            high = mid-1
    return ans


if __name__ == '__main__':
    a = list(range(10))
    print(lower_bound(a, 6))
    print(upper_bound(a, 6))