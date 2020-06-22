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
        def frontN(nums, n):
        
            if (len(nums) < n):
                return nums
            else:
                result = [n]
                Array.Copy(nums, 0, result, 0, n)
                return result
            
            
        

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
        def unlucky1(nums):
            if (len(nums) < 2):
                return false
            else:
                return is13(nums, 0) or is13(nums, 1) or is13(nums, len(nums)-2)
        

        def is13(nums, start):
            return start >= 0 and start < len(nums) - 1 and nums[start] == 1 and nums[start + 1] == 3
        

        '''
        Given 2 arrays, a and b, return a new array length 2 containing, 
        as much as will fit, the elements from a followed by the elements from b. 
        The arrays may be any length, including 0, but there will be 2 or more
        elements available between the 2 arrays. 

        make2([4, 5], [1, 2, 3]) -> [4, 5]
        make2([4], [1, 2, 3]) -> [4, 1]
        make2([], [1, 2]) -> [1, 2]    
        '''
        def make2(a, b):
            result

            if (len(a) >= 2):
                result = [a[0], a[1] ]
            elif (len(a) == 1):
                result = [a[0], b[0] ]
            else:
                result = [b[0], b[1] ]

            return result
        

        '''
        Given 2 arrays, a and b, return a new array length N containing, 
        as much as will fit, the elements from a followed by the elements from b. 
        The arrays may be any length, including 0, but there will be N or more
        elements available between the 2 arrays. 

        makeN([4, 5], [1, 2, 3], 2) -> [4, 5
        makeN([4], [1, 2, 3], 2) -> [4, 1
        makeN([], [1, 2], 2) -> [1, 2        
        '''
        def makeN(a, b, n):
            if (a == null or len(a) == 0):
                result = [n]
                Array.Copy(b, result, n)
                return result

            elif (b == null or len(b) == 0):
                result = [n]
                Array.Copy(a, result, n)
                return result

            else:
                result = [n]
                Array.Copy(a, 0, result, 0, len(a))
                Array.Copy(b, 0, result, len(a), n - len(a))
                return result
            
        

        '''
        Given 2 arrays, a and b, of any length, return a new array with the 
        first element of each array. If either array is length 0, ignore that array. 
        Use an array. Do not use a list.
        front11([1, 2, 3], [7, 9, 8]) -> [1, 7]
        front11([1], [2]) -> [1, 2]
        front11([1, 7], []) -> [1]       
        '''
        def front11(a, b):
            result = [min(len(a), 1) + min(len(b), 1)]
            rpos = 0
            if len(a) > 0:
                result[rpos] = a[0]
                rpos += 1
            if len(b) > 0:
                result[rpos] = b[0]
                rpos += 1
            return result
        

        '''
        Given 2 arrays, a and b, of any length, return a new array with the 
        first element of each array. If either array is length 0, ignore that array. 
        Use a list.
        front11List([1, 2, 3], [7, 9, 8]) -> [1, 7]
        front11List([1], [2]) -> [1, 2]
        front11List([1, 7], []) -> [1]       
        '''
        def front11List(a, b):
            list = []

            if len(a) > 0:
                list.append(a[0])

            if len(b) > 0:
                list.append(b[0])

            return list
        


            print("biggerTwo")
            print(biggerTwo([[1, 2], [3, 4])  == [3, 4])
            print(biggerTwo([[3, 4], [1, 2])  == [3, 4])
            print(biggerTwo([[1, 1], [1, 2])  == [1, 2])

            print("biggerTwo")
            print(biggerTwo([[1, 2 ], [3, 4 ]) == [3, 4 ]
            print(biggerTwo([[3, 4 ], [1, 2 ]) == [3, 4 ]
            print(biggerTwo([[1, 1 ], [1, 2 ]) == [1, 2 ]

            print("makeMiddle")
            print(makeMiddle([[1, 2, 3, 4])  == [2, 3])
            print(makeMiddle([[7, 1, 2, 3, 4, 9])  == [2, 3])
            print(makeMiddle([[1, 2]) == [1, 2]))

            print("plusTwo")
            print(plusTwo([[1, 2], [3, 4]) == [1, 2, 3, 4]
            print(plusTwo([[4, 4], [2, 2]) == [4, 4, 2, 2]
            print(plusTwo([[9, 2], [3, 4]) == [9, 2, 3, 4]

            print("plusTwo")
            print(plusTwo([[1, 2 ], [3, 4 ]) == [1, 2, 3, 4 ]
            print(plusTwo([[4, 4 ], [2, 2 ]) == [4, 4, 2, 2 ]
            print(plusTwo([[9, 2 ], [3, 4 ]) == [9, 2, 3, 4 ]

            print("swapEnds")
            print(swapEnds([[1, 2, 3, 4]) == [4, 2, 3, 1]
            print(swapEnds([[1, 2, 3]) == [3, 2, 1]
            print(swapEnds([[8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8]

            print("swapEnds2")
            print(swapEnds2([[1, 2, 3, 4]) == [4, 2, 3, 1]
            print(swapEnds2([[1, 2, 3]) == [3, 2, 1]
            print(swapEnds([[8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8]

            print("midN")
            print(midThree([[1, 2, 3, 4, 5]) == [2, 3, 4]
            print(midThree([[8, 6, 7, 5, 3, 0, 9]) == [7, 5, 3]
            print(midThree([[1, 2, 3]) == [1, 2, 3]))

            print("midN")
            print(midThree([[1, 2, 3, 4, 5 ]) == [2, 3, 4 ]
            print(midThree([[8, 6, 7, 5, 3, 0, 9 ]) == [7, 5, 3 ]
            print(midThree([[1, 2, 3 ]) == [1, 2, 3 ]


            print("maxTriple")
            print(maxTriple([[1, 2, 3]) == 3)
            print(maxTriple([[1, 5, 3]) == 5)
            print(maxTriple([[5, 2, 3]) == 5)

            print("front2")
            print(front2([1, 2, 3]) == [1, 2]
            print(front2([1, 2]) == [1, 2]
            print(front2([1 ]) == [1 ]

            print("frontN")
            print(frontN([[1, 2, 3 ], 2) == [1, 2 ]
            print(frontN([[1, 2 ], 2) == [1, 2 ]
            print(frontN([[1 ], 2) == [1 ]

            print("unlucky1")
            print(unlucky1([[1, 3, 4, 5]) == true)
            print(unlucky1([[2, 1, 3, 4, 5]) == true)
            print(unlucky1([[1, 1, 1]) == false)

            print("makeN")
            print(make2([[4, 5], [1, 2, 3]) == [4, 5]
            print(make2([[4], [1, 2, 3]) == [4, 1]
            print(make2([[], [1, 2]) == [1, 2]

            print("front11")
            print(front11([[1, 2, 3], [7, 9, 8]) == [1, 7]
            print(front11([[1 ], [2 ]) == [1, 2]
            print(front11([[1, 7], []) == [1 ]

            print("front11List")
            print(front11List([[1, 2, 3 ], [7, 9, 8 ]) == [1, 7 ]
            print(front11List([[1 ], [2 ]) == [1, 2 ]
            print(front11List([[1, 7 ], []) == [1 ]

