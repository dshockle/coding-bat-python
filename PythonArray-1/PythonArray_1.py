import sys

class PythonArray_1(object):
        '''
        Start with 2 arrays, a and b, each length 2. 
        Consider the sum of the values in each array. 
        Return the array which has the largest sum. 
        In event of a tie, return a. 

        biggerTwo(<1, 2>, <3, 4>) -> <3, 4>
        biggerTwo(<3, 4>, <1, 2>) -> <3, 4>
        biggerTwo(<1, 1>, <1, 2>) -> <1, 2>
        '''
        def biggerTwo(a, b):
            if (sumArray(a) >= sumArray(b)):
                return a
            else:
                return b
        

        def sumArray(arr):
            sum = 0
            for n in arr:
                sum += n
            return sum
        

        '''
        Start with 2 arrays, a and b, each length 2. 
        Consider the sum of the values in each array. 
        Return the array which has the largest sum. 
        In event of a tie, return a. Use Linq. Do not use loops.

        biggerTwoLinq(<1, 2>, <3, 4>) -> <3, 4>
        biggerTwoLinq(<3, 4>, <1, 2>) -> <3, 4>
        biggerTwoLinq(<1, 1>, <1, 2>) -> <1, 2>
        '''
        def biggerTwoLinq(a, b):
            if (a.Sum() >= b.Sum()):
                return a
            else:
                return b
        

        '''
        Return the two middle elements of the even-length array.

        makeMiddle(<1, 2, 3, 4>) -> <2, 3>
        makeMiddle(<7, 1, 2, 3, 4, 9>) -> <2, 3>
        makeMiddle(<1, 2>) -> <1, 2>
        '''
        def makeMiddle(nums):
            if (len(nums) < 2):
                return nums
            else:
                return new < nums[len(nums)/2-1], nums[len(nums)/2]
        

        '''
        Given 2 arrays, each length 2, return a new array length 4 
        containing all their elements. Use an array. Do not use a list.

        plusTwo(<1, 2>, <3, 4>) -> <1, 2, 3, 4>
        plusTwo(<4, 4>, <2, 2>) -> <4, 4, 2, 2>
        plusTwo(<9, 2>, <3, 4>) -> <9, 2, 3, 4>
        '''
        def plusTwo(a, b):
            result = new int[a.Length + b.Length]
            Array.Copy(a, result, a.Length)
            Array.Copy(b, 0, result, a.Length, b.Length)
            return result
        

        '''
        Given 2 arrays, each length 2, return a new array length 4 
        containing all their elements. Use a list.

        plusTwoList(<1, 2>, <3, 4>) -> <1, 2, 3, 4>
        plusTwoList(<4, 4>, <2, 2>) -> <4, 4, 2, 2>
        plusTwoList(<9, 2>, <3, 4>) -> <9, 2, 3, 4>
        '''
        def plusTwoList(a, b):
            var list = new List<int>()
            list.AddRange(a)
            list.AddRange(b)
            return list.ToArray()
        

        '''
        Given an array of ints, swap the first and last elements in the array. 
        Return the modified array. 

        The array length will be at least 1. 

        swapEnds(<1, 2, 3, 4>) -> <4, 2, 3, 1>
        swapEnds(<1, 2, 3>) -> <3, 2, 1>
        swapEnds(<8, 6, 7, 9, 5>) -> <5, 6, 7, 9, 8>
        '''
        def swapEnds(nums):
            temp = nums[0]
            nums[0] = nums[len(nums) - 1]
            nums[len(nums) - 1] = temp
            return nums
        

        '''
            Given an array of ints of odd length, return a new array length 3 
            containing the elements from the middle of the array. The array 
            length will be at least 3. 

            midThree(<1, 2, 3, 4, 5>) -> <2, 3, 4>
            midThree(<8, 6, 7, 5, 3, 0, 9>) -> <7, 5, 3>
            midThree(<1, 2, 3>) -> <1, 2, 3>
        '''
        def midThree(nums):
            mid = len(nums) / 2
            return new < nums[mid-1], nums[mid], nums[mid+1] 
        

        '''
        Given an array of ints of odd length, return a new array length N 
        containing the elements from the middle of the array. The array 
        length will be at least N. 

        midN(<1, 2, 3, 4, 5>, 3) -> <2, 3, 4>
        midN(<8, 6, 7, 5, 3, 0, 9>, 3) -> <7, 5, 3>
        midN(<1, 2, 3>, 3) -> <1, 2, 3>
        '''
        def midN(nums, n):
            result = new int[n]
            start = len(nums) / 2 - n / 2
            Array.Copy(nums, start, result, 0, n)
            return result
        

        '''
            Given an array of ints of odd length, look at the first, last, 
            and middle values in the array and return the largest. 
            The array length will be a least 1. 

            maxTriple(<1, 2, 3>) -> 3
            maxTriple(<1, 5, 3>) -> 5
            maxTriple(<5, 2, 3>) -> 5        
        '''
        public static maxTriple(nums):
        
            return Math.Max(nums[0], Math.Max(nums[len(nums)/2], nums[len(nums)-1]))
        

        '''
        Given an array of any length, return a new array of its first 2 elements. 
        If the array is smaller than length 2, use whatever elements are present. 

        front2(<1, 2, 3>) -> <1, 2
        front2(<1, 2>) -> <1, 2
        front2(<1>) -> <1        
        '''
        def front2(nums):
            if (len(nums) < 2):
                return nums
            else:
                return new < nums[0], nums[1] 
        

        '''
        Given an array of any length, return a new array of its first N elements. 
        If the array is smaller than length N, use whatever elements are present. 

        frontN(<1, 2, 3>, 2) -> <1, 2
        frontN(<1, 2>, 2) -> <1, 2
        frontN(<1>, 2) -> <1        
        '''
        def frontN(nums, n):
        
            if (len(nums) < n):
                return nums
            else:
                result = new int[n]
                Array.Copy(nums, 0, result, 0, n)
                return result
            
            
        

        '''
        Given an array of any length, return a new array of its first N elements. 
        If the array is smaller than length N, use whatever elements are present. 
        Use Linq. Do not use loops.
        frontN(<1, 2, 3>, 2) -> <1, 2
        frontN(<1, 2>, 2) -> <1, 2
        frontN(<1>, 2) -> <1        
        '''
        def frontNLinq(nums, n):
            return nums.Take(n).ToArray()
        

        '''
        We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. 
        Return true if the given array contains an unlucky 1 in the first 2 or 
        last 2 positions in the array. 

        unlucky1(<1, 3, 4, 5>) -> true
        unlucky1(<2, 1, 3, 4, 5>) -> true
        unlucky1(<1, 1, 1>) -> false        
        '''
        public static bool unlucky1(nums)
            if (len(nums) < 2):
                return false
            else:
                return is13(nums, 0) || is13(nums, 1) || is13(nums, len(nums)-2)
        

        private static bool is13(nums, start)
            return start >= 0 && start < len(nums) - 1 && nums[start] == 1 && nums[start + 1] == 3
        

        '''
        Given 2 arrays, a and b, return a new array length 2 containing, 
        as much as will fit, the elements from a followed by the elements from b. 
        The arrays may be any length, including 0, but there will be 2 or more
        elements available between the 2 arrays. 

        make2(<4, 5>, <1, 2, 3>) -> <4, 5>
        make2(<4>, <1, 2, 3>) -> <4, 1>
        make2(<>, <1, 2>) -> <1, 2>    
        '''
        def make2(a, b)
            result

            if (a.Length >= 2):
                result = new < a[0], a[1] >
            elif (a.Length == 1):
                result = new < a[0], b[0] >
            else:
                result = new < b[0], b[1] >

            return result
        

        '''
        Given 2 arrays, a and b, return a new array length N containing, 
        as much as will fit, the elements from a followed by the elements from b. 
        The arrays may be any length, including 0, but there will be N or more
        elements available between the 2 arrays. 

        makeN(<4, 5>, <1, 2, 3>, 2) -> <4, 5
        makeN(<4>, <1, 2, 3>, 2) -> <4, 1
        makeN(<>, <1, 2>, 2) -> <1, 2        
        '''
        def makeN(a, b, n)
            if (a == null || a.Length == 0):
                result = new int[n]
                Array.Copy(b, result, n)
                return result

            elif (b == null || b.Length == 0):
                result = new int[n]
                Array.Copy(a, result, n)
                return result

            else:
                result = new int[n]
                Array.Copy(a, 0, result, 0, a.Length)
                Array.Copy(b, 0, result, a.Length, n - a.Length)
                return result
            
        

        '''
            Given 2 arrays, a and b, of any length, return a new array with the 
            first element of each array. If either array is length 0, ignore that array. 
            Use an array. Do not use a list.
            front11(<1, 2, 3>, <7, 9, 8>) -> <1, 7>
            front11(<1>, <2>) -> <1, 2>
            front11(<1, 7>, <>) -> <1>       
        '''
        def front11(a, b):
            result = new int[Math.Min(a.Length, 1) + Math.Min(b.Length, 1)]
            rpos = 0
            if a.Length > 0:
                result[rpos++] = a[0]
            if b.Length > 0:
                result[rpos++] = b[0]
            return result
        

        '''
            Given 2 arrays, a and b, of any length, return a new array with the 
            first element of each array. If either array is length 0, ignore that array. 
            Use a list.
            front11List(<1, 2, 3>, <7, 9, 8>) -> <1, 7>
            front11List(<1>, <2>) -> <1, 2>
            front11List(<1, 7>, <>) -> <1>       
        '''
        def front11List(a, b):
            List<int> list = new List<int>()

            if (a != null && a.Length > 0):
                list.Add(a[0])

            if (b != null && b.Length > 0):
                list.Add(b[0])

            return list.ToArray()
        


            print("biggerTwo")
            print(biggerTwo(new < <1, 2>, new < 3, 4>) .SequenceEqual(new   3, 4>))
            print(biggerTwo(new < <3, 4>, new < 1, 2>) .SequenceEqual(new   3, 4>))
            print(biggerTwo(new < <1, 1>, new < 1, 2>) .SequenceEqual(new   1, 2>))

            print("biggerTwo")
            print(biggerTwo(new < <1, 2 >, new < 3, 4 >).SequenceEqual(new < 3, 4 >))
            print(biggerTwo(new < <3, 4 >, new < 1, 2 >).SequenceEqual(new < 3, 4 >))
            print(biggerTwo(new < <1, 1 >, new < 1, 2 >).SequenceEqual(new < 1, 2 >))

            print("makeMiddle")
            print(makeMiddle(new < <1, 2, 3, 4>) .SequenceEqual(new   2, 3>))
            print(makeMiddle(new < <7, 1, 2, 3, 4, 9>) .SequenceEqual(new   2, 3>))
            print(makeMiddle(new < <1, 2>).SequenceEqual(new < 1, 2>))

            print("plusTwo")
            print(plusTwo(new < <1, 2>, new < 3, 4>).SequenceEqual(new < 1, 2, 3, 4>))
            print(plusTwo(new < <4, 4>, new < 2, 2>).SequenceEqual(new < 4, 4, 2, 2>))
            print(plusTwo(new < <9, 2>, new < 3, 4>).SequenceEqual(new < 9, 2, 3, 4>))

            print("plusTwo")
            print(plusTwo(new < <1, 2 >, new < 3, 4 >).SequenceEqual(new < 1, 2, 3, 4 >))
            print(plusTwo(new < <4, 4 >, new < 2, 2 >).SequenceEqual(new < 4, 4, 2, 2 >))
            print(plusTwo(new < <9, 2 >, new < 3, 4 >).SequenceEqual(new < 9, 2, 3, 4 >))

            print("swapEnds")
            print(swapEnds(new < <1, 2, 3, 4>).SequenceEqual(new < 4, 2, 3, 1>))
            print(swapEnds(new < <1, 2, 3>).SequenceEqual(new < 3, 2, 1>))
            print(swapEnds(new < <8, 6, 7, 9, 5>).SequenceEqual(new < 5, 6, 7, 9, 8>))

            print("midN")
            print(midThree(new < <1, 2, 3, 4, 5>).SequenceEqual(new < 2, 3, 4>))
            print(midThree(new < <8, 6, 7, 5, 3, 0, 9>).SequenceEqual(new < 7, 5, 3>))
            print(midThree(new < <1, 2, 3>).SequenceEqual(new < 1, 2, 3>))

            print("midN")
            print(midThree(new < <1, 2, 3, 4, 5 >).SequenceEqual(new < 2, 3, 4 >))
            print(midThree(new < <8, 6, 7, 5, 3, 0, 9 >).SequenceEqual(new < 7, 5, 3 >))
            print(midThree(new < <1, 2, 3 >).SequenceEqual(new < 1, 2, 3 >))


            print("maxTriple")
            print(maxTriple(new < <1, 2, 3>) == 3)
            print(maxTriple(new < <1, 5, 3>) == 5)
            print(maxTriple(new < <5, 2, 3>) == 5)

            print("front2")
            print(front2(new < 1, 2, 3>).SequenceEqual(new < 1, 2>))
            print(front2(new < 1, 2>).SequenceEqual(new < 1, 2>))
            print(front2(new < 1 >).SequenceEqual(new < 1 >))

            print("frontN")
            print(frontN(new < <1, 2, 3 >, 2).SequenceEqual(new < 1, 2 >))
            print(frontN(new < <1, 2 >, 2).SequenceEqual(new < 1, 2 >))
            print(frontN(new < <1 >, 2).SequenceEqual(new < 1 >))

            print("unlucky1")
            print(unlucky1(new < <1, 3, 4, 5>) == true)
            print(unlucky1(new < <2, 1, 3, 4, 5>) == true)
            print(unlucky1(new < <1, 1, 1>) == false)

            print("makeN")
            print(make2(new < <4, 5>, new < 1, 2, 3>).SequenceEqual(new < 4, 5>))
            print(make2(new < <4>, new < 1, 2, 3>).SequenceEqual(new < 4, 1>))
            print(make2(new < <>, new < 1, 2>).SequenceEqual(new < 1, 2>))

            print("front11")
            print(front11(new < <1, 2, 3>, new < 7, 9, 8>).SequenceEqual(new < 1, 7>))
            print(front11(new < <1 >, new < 2 >).SequenceEqual(new < 1, 2>))
            print(front11(new < <1, 7>, new < >).SequenceEqual(new < 1 >))

            print("front11List")
            print(front11List(new < <1, 2, 3 >, new < 7, 9, 8 >).SequenceEqual(new < 1, 7 >))
            print(front11List(new < <1 >, new < 2 >).SequenceEqual(new < 1, 2 >))
            print(front11List(new < <1, 7 >, new < >).SequenceEqual(new < 1 >))

