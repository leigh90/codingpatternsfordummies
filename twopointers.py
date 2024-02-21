# def two_pointers(array):
#     left = 0
#     right = len(array)
#     while left <= right:
#         left = left + 1
#         right = right - 1


# def is_palindrome(s):
#     print(f'String to check {s} length of string {len(s)}', sep="")
#     left = 0
#     right = len(s) - 1
#     # i = 1
#     while left < right:
#         print(f" left ={left}, right={right}",sep="")
#         print(f"The current element being pointed to by the left pointer is {s[left]}")
#         print(f"The current element being pointed to by the right pointer is {s[right]}")
#         # Check if elements are similar if they aren't return false
#         if s[left] != s[right]:
#             return False
#         left = left + 1# Heading towards the right
#         right = right - 1# Heading towards the left
#         print("-"*100)
#     print(f"Loop terminated with left = {left}, right = {right}")
#     print("Pointers have reached the same index or crossed each other hence no need to keep looking")
#     return True     

# is_palindrome('RACECAR')
# ["RACECAR", "ABBA", "TART"]

# Algorithm
# Initialize two pointers and move them from opposite ends.
# The first pointer starts at the beginning of the string and moves toward the middle, while the second pointer starts at the end and moves toward the middle.
# Compare the elements at each position to detect a nonmatching pair.
# If both pointers reach the middle of the string without encountering a nonmatching pair, the string is a palindrome.

# Time complexity 
# O(n) n = the number of characters in the string
# Buuuut since you're checking two elements at at time it becomes  O(n/2)'

# Space complexity
# O(1) since we use constant space to store two indexes



# def hidenseek(nums):
#     target = 20
#     left = 0
#     right = len(nums) - 1 
#     while left < right:
#         print(f"left - {nums[left], right - nums[right]}")
#         two_sam = nums[left] + nums[left]
#         to_twenty = target - two_sam
#         print(f"To_twenty {to_twenty}")
#         print("-" * 100)
#         if to_twenty in nums:
#             print(nums[left], nums[right], nums[to_twenty])

#         left = left + 1
#         right = right - 1


# def hidenseek(nums, target):
#     target = 20
#     f_pointer = 0
#     s_pointer = 1
#     max_num = max(nums)
#     nums.remove(max_num)
#     i = 0

#     while i <= len(nums):
#         two_sam = nums[f_pointer] + nums[s_pointer]
#         print(f"max number is {max_num}")
#         print(f"two sam {two_sam}, num one{nums[f_pointer]}, numtwo{nums[s_pointer]}")
#         if two_sam + max_num == target:
#             print(max_num, nums[f_pointer], nums[s_pointer])
#             return True
#         else:
#             print(False)
        
#         i += 1
    
#     print(f"the first pointer is now at {nums[f_pointer]}")
#     s_pointer += 1
#     if nums[s_pointer] == nums[-1]:
#         print("We reached the end")
#         f_pointer +=1
#     print(f"the second pointer is now at {nums[s_pointer]}")
#     print(f"i is now {i}")
#     print("-"*100)
#     print(f"Loop terminated with left = {nums[f_pointer]}, right = {nums[s_pointer]}")

# hidenseek([3,7,1,2,8,4,5], 20)


def find_sum_of_three(nums, target):
    nums.sort()
    print(nums)
    for i in range(0,len(nums)-2):
        low = i + 1
        high = len(nums) -1
        
        while low < high:
            print(f"i is {i}")
            print(f"low {low}, high{high}")
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                print(nums[i], nums[low],nums[high])
                return True
            
            elif triplet < target:
                low += 1

            else:
                high -= 1

        return False


find_sum_of_three([3, 7, 1, 2, 8, 4, 5], 10)

