
# Algorithm
# Initialize two pointers and move them from opposite ends.
# The first pointer starts at the beginning of the string and moves toward the middle, while the second pointer starts at the end and moves toward the middle.
# Compare the elements at each position to detect a nonmatching pair.
# If both pointers reach the middle of the string without encountering a nonmatching pair, the string is a palindrome.

def two_pointers(array):
    left = 0
    right = len(array)
    while left <= right:
        left = left + 1
        right = right - 1


def is_palindrome(s):
    print(f'String to check {s} length of string {len(s)}', sep="")
    left = 0
    right = len(s) - 1
    # i = 1
    while left < right:
        print(f" left ={left}, right={right}",sep="")
        print(f"The current element being pointed to by the left pointer is {s[left]}")
        print(f"The current element being pointed to by the right pointer is {s[right]}")
        # Check if elements are similar if they aren't return false
        if s[left] != s[right]:
            return False
        left = left + 1# Heading towards the right
        right = right - 1# Heading towards the left
        print("-"*100)
    print(f"Loop terminated with left = {left}, right = {right}")
    print("Pointers have reached the same index or crossed each other hence no need to keep looking")
    return True     

is_palindrome('RACECAR')
["RACECAR", "ABBA", "TART"]

# Time complexity 
# O(n) n = the number of characters in the string
# Buuuut since you're checking two elements at at time it becomes  O(n/2)'

# Space complexity
# O(1) since we use constant space to store two indexes



# SUM OF THREE VALUES
# 1. Sort the list 
# 2. loop in a range
# 3.  Loop in range 0 to 2nd last element
# 4. Initialise pointers
# 5. While low < high check if the 3 numbers i, and the 2 pointes add up to the target 
# 6. If so return True
# 7. If not return False

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

# Time complexity = o(n^2)
# Space complexity is between O(log(n)) and O(n) 



