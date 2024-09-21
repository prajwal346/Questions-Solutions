def three_sum(nums):
    nums.sort()  # Sort the array
    triplets = []  # To store the result
    
    for i in range(len(nums) - 2):  # Iterate through the array
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1  # Two pointers
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1  # Move left pointer to the right to increase the sum
            elif total > 0:
                right -= 1  # Move right pointer to the left to decrease the sum
            else:
                # Found a triplet
                triplets.append((nums[i], nums[left], nums[right]))
                
                # Skip duplicate values for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
    
    return triplets

# Example usage:
if __name__ == "__main__":
    nums = [-1,-2,3,4,5,-9]
    result = three_sum(nums)
    print("Unique triplets that sum to zero:", result)
