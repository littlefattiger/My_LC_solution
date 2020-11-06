# Quick sort and merge sort

# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) == 1:
                return nums
            m = len(nums)//2
            left = merge_sort(nums[:m])
            right = merge_sort(nums[m:])
            i = 0 
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left)  :
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1  
            return nums
        return merge_sort(nums)
        
# quick sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, lo, hi):
            def partition(nums, lo, hi):
                if lo == hi:
                    return lo
                random_number = random.randint(lo,hi)
                nums[random_number], nums[hi] = nums[hi], nums[random_number]
                partition = nums[hi]
                i = lo
                for j in range(lo, hi):
                    if nums[j] < partition:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                nums[i], nums[hi] = nums[hi], nums[i]
                return i
 
            if lo < hi:
                partition = partition(nums, lo, hi)
                quick_sort(nums, lo, partition - 1)
                quick_sort(nums, partition + 1, hi)
            
            return nums
                        
                    
            
             
        return quick_sort(nums, 0, len(nums) -1)
