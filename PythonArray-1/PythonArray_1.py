import sys

class PythonArray_1(object):
        '''
        Start with 2 arrays, a and b, each length 2. 
        Consider the sum of the values in each array. 
        Return the array which has the largest sum. 
        In event of a tie, return a. 

        biggerTwo([1, 2], [3, 4]) -> [3, 4]
        biggerTwo([3, 4], [1, 2]) -> [3, 4]
        biggerTwo([1, 1], [1, 2]) -> [1, 2]
        '''
        def biggerTwo(a, b):
            return a if sum(a) >= sum(b) else b


        '''
        Return the two middle elements of the even-length array.

        makeMiddle([1, 2, 3, 4]) -> [2, 3]
        makeMiddle([7, 1, 2, 3, 4, 9]) -> [2, 3]
        makeMiddle([1, 2]) -> [1, 2]
        '''
        def makeMiddle(nums):
            return nums[int(len(nums)/2-1):int(len(nums)/2+1)]
        


        '''
        Given 2 arrays, each length 2, return a new array length 4 
        containing all their elements. 

        plusTwo([1, 2], [3, 4]) -> [1, 2, 3, 4]
        plusTwo([4, 4], [2, 2]) -> [4, 4, 2, 2]
        plusTwo([9, 2], [3, 4]) -> [9, 2, 3, 4]
        '''
        def plusTwo(a, b):
            return a + b
        

        '''
        Given an array of ints, swap the first and last elements in the array. 
        Return the modified array. 

        The array length will be at least 1. 

        swapEnds([1, 2, 3, 4]) -> [4, 2, 3, 1]
        swapEnds([1, 2, 3]) -> [3, 2, 1]
        swapEnds([8, 6, 7, 9, 5]) -> [5, 6, 7, 9, 8]
        '''
        def swapEnds(nums):
            temp = nums[0]
            nums[0] = nums[-1]
            nums[-1] = temp
            return nums
        
        '''
        Given an array of ints, swap the first and last elements in the array. 
        Return the modified array. 

        The array length will be at least 1. 

        swapEnds2([1, 2, 3, 4]) -> [4, 2, 3, 1]
        swapEnds2([1, 2, 3]) -> [3, 2, 1]
        swapEnds2([8, 6, 7, 9, 5]) -> [5, 6, 7, 9, 8]
        '''
        def swapEnds2(nums):
            nums[0],nums[-1] = nums[-1],nums[0]
            return nums


        '''
        Given an array of ints of odd length, return a new array length 3 
        containing the elements from the middle of the array. The array 
        length will be at least 3. 

        midThree([1, 2, 3, 4, 5]) -> [2, 3, 4]
        midThree([8, 6, 7, 5, 3, 0, 9]) -> [7, 5, 3]
        midThree([1, 2, 3]) -> [1, 2, 3]
        '''
        def midThree(nums):
            return nums[int(len(nums)/2)-1:int(len(nums)/2)+2]
        


        '''
        Given an array of ints of odd length, look at the first, last, 
        and middle values in the array and return the largest. 
        The array length will be a least 1. 

        maxTriple([1, 2, 3]) -> 3
        maxTriple([1, 5, 3]) -> 5
        maxTriple([5, 2, 3]) -> 5        
        '''
        def maxTriple(nums):
            return max(nums[int(len(nums)/2)-1:int(len(nums)/2)+2])
        

        '''
        Given an array of any length, return a new array of its first 2 elements. 
        If the array is smaller than length 2, use whatever elements are present. 

        front2([1, 2, 3]) -> [1, 2
        front2([1, 2]) -> [1, 2
        front2([1]) -> [1        
        '''
        def front2(nums):
            if (len(nums) < 2):
                return nums
            else:
                return [nums[0], nums[1]]
        

        '''
        Given an array of any length, return a new array of its first N elements. 
        If the array is smaller than length N, use whatever elements are present. 

        frontN([1, 2, 3], 2) -> [1, 2]
        frontN([1, 2], 2) -> [1, 2]
        frontN([1], 2) -> [1] 
        '''
        def frontN(fnArr, fnN):
            return fnArr[:fnN]
            
        

        '''
        Given an array of any length, return a new array of its first N elements. 
        If the array is smaller than length N, use whatever elements are present. 
        Use Linq. Do not use loops.
        frontN([1, 2, 3], 2) -> [1, 2
        frontN([1, 2], 2) -> [1, 2
        frontN([1], 2) -> [1        
        '''
        def frontNLinq(nums, n):
            return nums.Take(n).ToArray()
        

        '''
        We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. 
        Return true if the given array contains an unlucky 1 in the first 2 or 
        last 2 positions in the array. 

        unlucky1([1, 3, 4, 5]) -> true
        unlucky1([2, 1, 3, 4, 5]) -> true
        unlucky1([1, 1, 1]) -> false        
        '''
        def unlucky1(u1nums):
            u1length = len(u1nums)
            if u1length < 2:
                return False
            u1starts = [0, 1, u1length-2]
            for u1pos in u1starts:
                if u1nums[u1pos] == 1 and u1nums[u1pos+1] == 3:
                    return True
            return False
        

        '''
        Given 2 arrays, a and b, return a new array length 2 containing, 
        as much as will fit, the elements from a followed by the elements from b. 
        The arrays may be any length, including 0, but there will be 2 or more
        elements available between the 2 arrays. 

        make2([4, 5], [1, 2, 3]) -> [4, 5]
        make2([4], [1, 2, 3]) -> [4, 1]
        make2([], [1, 2]) -> [1, 2]    
        '''
        def make2(m2a, m2b):
            return (m2a[:2] + m2b[:2])[:2]


        '''
        Given 2 arrays, a and b, of any length, return a new array with the 
        first element of each array. If either array is length 0, ignore that array. 
        front11([1, 2, 3], [7, 9, 8]) -> [1, 7]
        front11([1], [2]) -> [1, 2]
        front11([1, 7], []) -> [1]       
        '''
        def front11(f11arr1, f11arr2):
            return f11arr1[:1] + f11arr2[:1]



        print("biggerTwo")
        print(biggerTwo([1, 2], [3, 4]) == [3, 4])
        print(biggerTwo([3, 4], [1, 2]) == [3, 4])
        print(biggerTwo([1, 1], [1, 2]) == [1, 2])

        print("makeMiddle")
        print(makeMiddle([1, 2, 3, 4]) == [2, 3])
        print(makeMiddle([7, 1, 2, 3, 4, 9]) == [2, 3])
        print(makeMiddle([1, 2]) == [1, 2])

        print("plusTwo")
        print(plusTwo([1, 2], [3, 4]) == [1, 2, 3, 4])
        print(plusTwo([4, 4], [2, 2]) == [4, 4, 2, 2])
        print(plusTwo([9, 2], [3, 4]) == [9, 2, 3, 4])

        print("plusTwo")
        print(plusTwo([1, 2 ], [3, 4 ]) == [1, 2, 3, 4])
        print(plusTwo([4, 4 ], [2, 2 ]) == [4, 4, 2, 2])
        print(plusTwo([9, 2 ], [3, 4 ]) == [9, 2, 3, 4])

        print("swapEnds")
        print(swapEnds([1, 2, 3, 4]) == [4, 2, 3, 1])
        print(swapEnds([1, 2, 3]) == [3, 2, 1])
        print(swapEnds([8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8])

        print("swapEnds2")
        print(swapEnds2([1, 2, 3, 4]) == [4, 2, 3, 1])
        print(swapEnds2([1, 2, 3]) == [3, 2, 1])
        print(swapEnds([8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8])

        print("midN")
        print(midThree([1, 2, 3, 4, 5]) == [2, 3, 4])
        print(midThree([8, 6, 7, 5, 3, 0, 9]) == [7, 5, 3])
        print(midThree([1, 2, 3]) == [1, 2, 3])

        print("midN")
        print(midThree([1, 2, 3, 4, 5 ]) == [2, 3, 4])
        print(midThree([8, 6, 7, 5, 3, 0, 9 ]) == [7, 5, 3])
        print(midThree([1, 2, 3 ]) == [1, 2, 3])

        print("maxTriple")
        print(maxTriple([1, 2, 3]) == 3)
        print(maxTriple([1, 5, 3]) == 5)
        print(maxTriple([5, 2, 3]) == 5)

        print("front2")
        print(front2([1, 2, 3]) == [1, 2])
        print(front2([1, 2]) == [1, 2])
        print(front2([1 ]) == [1 ])

        print("frontN")
        print(frontN([1, 2, 3 ], 2) == [1, 2 ])
        print(frontN([1, 2 ], 2) == [1, 2 ])
        print(frontN([1 ], 2) == [1 ])

        print("unlucky1")
        print(unlucky1([1, 3, 4, 5]) == True)
        print(unlucky1([2, 1, 3, 4, 5]) == True)
        print(unlucky1([1, 1, 1]) == False)

        print("make2")
        print(make2([4, 5], [1, 2, 3]) == [4, 5])
        print(make2([4], [1, 2, 3]) == [4, 1])
        print(make2([], [1, 2]) == [1, 2])

        print("front11")
        print(front11([1, 2, 3], [7, 9, 8]) == [1, 7])
        print(front11([1 ], [2 ]) == [1, 2])
        print(front11([1, 7], []) == [1])

