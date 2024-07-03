class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
              return False
        stack = []   
        min_arr = [0] * len(nums)
        min_arr[0] = nums [0]

        for i in range(1, len(nums)):
            min_arr[i] = min(min_arr[i-1], nums[i])

        for j in range(len(nums)-1,-1,-1):
            if nums[j] > min_arr[j]:
                while stack and stack[-1] <= min_arr[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False

# Example usage
sol = Solution()
nums = [3, 1, 4, 2]
result = sol.find132pattern(nums)
print(f"The array has a 132 pattern: {result}")   
         

