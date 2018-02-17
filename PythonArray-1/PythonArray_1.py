import sys

class PythonArray_1(object):
            /*
        Start with 2 int arrays, a and b, each length 2. 
        Consider the sum of the values in each array. 
        Return the array which has the largest sum. 
        In event of a tie, return a. 

        biggerTwo({1, 2}, {3, 4}) ? {3, 4}
        biggerTwo({3, 4}, {1, 2}) ? {3, 4}
        biggerTwo({1, 1}, {1, 2}) ? {1, 2}
        */
        public static int[] biggerTwo(int[] a, int[] b)
        {
            if (sumArray(a) >= sumArray(b))
                return a;
            else
                return b;
        }

        private static int sumArray(int[] arr)
        {
            int sum = 0;
            foreach (int n in arr)
            {
                sum += n;
            }
            return sum;
        }

        /*
        Start with 2 int arrays, a and b, each length 2. 
        Consider the sum of the values in each array. 
        Return the array which has the largest sum. 
        In event of a tie, return a. Use Linq. Do not use loops.

        biggerTwoLinq({1, 2}, {3, 4}) ? {3, 4}
        biggerTwoLinq({3, 4}, {1, 2}) ? {3, 4}
        biggerTwoLinq({1, 1}, {1, 2}) ? {1, 2}
        */
        public static int[] biggerTwoLinq(int[] a, int[] b)
        {
            if (a.Sum() >= b.Sum())
                return a;
            else
                return b;
        }

        /*
        Return the two middle elements of the even-length array.

        makeMiddle({1, 2, 3, 4}) ? {2, 3}
        makeMiddle({7, 1, 2, 3, 4, 9}) ? {2, 3}
        makeMiddle({1, 2}) ? {1, 2}
        */
        public static int[] makeMiddle(int[] nums)
        {
            if (nums.Length < 2)
                return nums;
            else
                return new int[] { nums[nums.Length/2-1], nums[nums.Length/2]};
        }

        /*
        Given 2 int arrays, each length 2, return a new array length 4 
        containing all their elements. Use an array. Do not use a list.

        plusTwo({1, 2}, {3, 4}) ? {1, 2, 3, 4}
        plusTwo({4, 4}, {2, 2}) ? {4, 4, 2, 2}
        plusTwo({9, 2}, {3, 4}) ? {9, 2, 3, 4}
        */
        public static int[] plusTwo(int[] a, int[] b)
        {
            int[] result = new int[a.Length + b.Length];
            Array.Copy(a, result, a.Length);
            Array.Copy(b, 0, result, a.Length, b.Length);
            return result;
        }

        /*
        Given 2 int arrays, each length 2, return a new array length 4 
        containing all their elements. Use a list.

        plusTwoList({1, 2}, {3, 4}) ? {1, 2, 3, 4}
        plusTwoList({4, 4}, {2, 2}) ? {4, 4, 2, 2}
        plusTwoList({9, 2}, {3, 4}) ? {9, 2, 3, 4}
        */
        public static int[] plusTwoList(int[] a, int[] b)
        {
            var list = new List<int>();
            list.AddRange(a);
            list.AddRange(b);
            return list.ToArray();
        }

        /*
        Given an array of ints, swap the first and last elements in the array. 
        Return the modified array. 

        The array length will be at least 1. 

        swapEnds({1, 2, 3, 4}) ? {4, 2, 3, 1}
        swapEnds({1, 2, 3}) ? {3, 2, 1}
        swapEnds({8, 6, 7, 9, 5}) ? {5, 6, 7, 9, 8}
        */
        public static int[] swapEnds(int[] nums)
        {
            int temp = nums[0];
            nums[0] = nums[nums.Length - 1];
            nums[nums.Length - 1] = temp;
            return nums;
        }

        /*
            Given an array of ints of odd length, return a new array length 3 
            containing the elements from the middle of the array. The array 
            length will be at least 3. 

            midThree({1, 2, 3, 4, 5}) ? {2, 3, 4}
            midThree({8, 6, 7, 5, 3, 0, 9}) ? {7, 5, 3}
            midThree({1, 2, 3}) ? {1, 2, 3}        
        */
        public static int[] midThree(int[] nums)
        {
            int mid = nums.Length / 2;
            return new int[] { nums[mid-1], nums[mid], nums[mid+1] };
        }

        /*
            Given an array of ints of odd length, return a new array length N 
            containing the elements from the middle of the array. The array 
            length will be at least N. 

            midN({1, 2, 3, 4, 5}, 3) ? {2, 3, 4}
            midN({8, 6, 7, 5, 3, 0, 9}, 3) ? {7, 5, 3}
            midN({1, 2, 3}, 3) ? {1, 2, 3}        
        */
        public static int[] midN(int[] nums, int n)
        {
            int[] result = new int[n];
            int start = nums.Length / 2 - n / 2;
            Array.Copy(nums, start, result, 0, n);
            return result;
        }

        /*
            Given an array of ints of odd length, look at the first, last, 
            and middle values in the array and return the largest. 
            The array length will be a least 1. 

            maxTriple({1, 2, 3}) ? 3
            maxTriple({1, 5, 3}) ? 5
            maxTriple({5, 2, 3}) ? 5        
        */
        public static int maxTriple(int[] nums)
        {
            return Math.Max(nums[0], Math.Max(nums[nums.Length/2], nums[nums.Length-1]));
        }

        /*
            Given an int array of any length, return a new array of its first 2 elements. 
            If the array is smaller than length 2, use whatever elements are present. 

            front2({1, 2, 3}) ? {1, 2}
            front2({1, 2}) ? {1, 2}
            front2({1}) ? {1}        
        */
        public static int[] front2(int[] nums)
        {
            if (nums.Length < 2)
                return nums;
            else
                return new int[] { nums[0], nums[1] };
        }

        /*
            Given an int array of any length, return a new array of its first N elements. 
            If the array is smaller than length N, use whatever elements are present. 

            frontN({1, 2, 3}, 2) ? {1, 2}
            frontN({1, 2}, 2) ? {1, 2}
            frontN({1}, 2) ? {1}        
        */
        public static int[] frontN(int[] nums, int n)
        {
            if (nums.Length < n)
                return nums;
            else
            {
                int[] result = new int[n];
                Array.Copy(nums, 0, result, 0, n);
                return result;
            }
            
        }

        /*
            Given an int array of any length, return a new array of its first N elements. 
            If the array is smaller than length N, use whatever elements are present. 
            Use Linq. Do not use loops.
            frontN({1, 2, 3}, 2) ? {1, 2}
            frontN({1, 2}, 2) ? {1, 2}
            frontN({1}, 2) ? {1}        
        */
        public static int[] frontNLinq(int[] nums, int n)
        {
            return nums.Take(n).ToArray();
        }

        /*
        We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. 
        Return true if the given array contains an unlucky 1 in the first 2 or 
        last 2 positions in the array. 

        unlucky1({1, 3, 4, 5}) ? true
        unlucky1({2, 1, 3, 4, 5}) ? true
        unlucky1({1, 1, 1}) ? false        
        */
        public static bool unlucky1(int[] nums)
        {
            if (nums.Length < 2)
                return false;
            else
                return is13(nums, 0) || is13(nums, 1) || is13(nums, nums.Length-2);
        }

        private static bool is13(int[] nums, int start)
        {
            return start >= 0 && start < nums.Length - 1 && nums[start] == 1 && nums[start + 1] == 3;
        }

        /*
        We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. 
        Return true if the given array contains an unlucky 1 in the first 2 or 
        last 2 positions in the array. Use Linq. Do not use loops.

        unlucky1Linq({1, 3, 4, 5}) ? true
        unlucky1Linq({2, 1, 3, 4, 5}) ? true
        unlucky1Linq({1, 1, 1}) ? false        
        */
        public static bool unlucky1Linq(int[] nums)
        {
            if (nums == null || nums.Length < 2)
                return false;

            return nums.Skip(1)
                       .Where((value, index) => nums[index] == 1 && value == 3)
                       .Any();
        }


        /*
            Given 2 int arrays, a and b, return a new array length 2 containing, 
            as much as will fit, the elements from a followed by the elements from b. 
            The arrays may be any length, including 0, but there will be 2 or more
            elements available between the 2 arrays. 

            make2({4, 5}, {1, 2, 3}) ? {4, 5}
            make2({4}, {1, 2, 3}) ? {4, 1}
            make2({}, {1, 2}) ? {1, 2}        
        */
        public static int[] make2(int[] a, int[] b)
        {
            int[] result;

            if (a.Length >= 2)
                result = new int[] { a[0], a[1] };
            else if (a.Length == 1)
                result = new int[] { a[0], b[0] };
            else
                result = new int[] { b[0], b[1] };

            return result;
        }

        /*
            Given 2 int arrays, a and b, return a new array length N containing, 
            as much as will fit, the elements from a followed by the elements from b. 
            The arrays may be any length, including 0, but there will be N or more
            elements available between the 2 arrays. 

            makeN({4, 5}, {1, 2, 3}, 2) ? {4, 5}
            makeN({4}, {1, 2, 3}, 2) ? {4, 1}
            makeN({}, {1, 2}, 2) ? {1, 2}        
        */
        public static int[] makeN(int[] a, int[] b, int n)
        {
            if (a == null || a.Length == 0)
            {
                int[] result = new int[n];
                Array.Copy(b, result, n);
                return result;
            }

            else if (b == null || b.Length == 0)
            {
                int[] result = new int[n];
                Array.Copy(a, result, n);
                return result;
            }

            else
            {
                int[] result = new int[n];
                Array.Copy(a, 0, result, 0, a.Length);
                Array.Copy(b, 0, result, a.Length, n - a.Length);
                return result;
            }
        }

        /*
            Given 2 int arrays, a and b, of any length, return a new array with the 
            first element of each array. If either array is length 0, ignore that array. 
            Use an array. Do not use a list.
            front11({1, 2, 3}, {7, 9, 8}) ? {1, 7}
            front11({1}, {2}) ? {1, 2}
            front11({1, 7}, {}) ? {1}        
        */
        public static int[] front11(int[] a, int[] b)
        {
            int[] result = new int[Math.Min(a.Length, 1) + Math.Min(b.Length, 1)];
            int rpos = 0;
            if (a.Length > 0)
                result[rpos++] = a[0];
            if (b.Length > 0)
                result[rpos++] = b[0];
            return result;
        }

        /*
            Given 2 int arrays, a and b, of any length, return a new array with the 
            first element of each array. If either array is length 0, ignore that array. 
            Use a list.
            front11List({1, 2, 3}, {7, 9, 8}) ? {1, 7}
            front11List({1}, {2}) ? {1, 2}
            front11List({1, 7}, {}) ? {1}        
        */
        public static int[] front11List(int[] a, int[] b)
        {
            List<int> list = new List<int>();

            if (a != null && a.Length > 0)
                list.Add(a[0]);

            if (b != null && b.Length > 0)
                list.Add(b[0]);

            return list.ToArray();
        }


            Console.WriteLine("biggerTwo");
            Console.WriteLine(biggerTwo(new int[] { 1, 2}, new int[] { 3, 4}) .SequenceEqual(new int[]  { 3, 4}));
            Console.WriteLine(biggerTwo(new int[] { 3, 4}, new int[] { 1, 2}) .SequenceEqual(new int[]  { 3, 4}));
            Console.WriteLine(biggerTwo(new int[] { 1, 1}, new int[] { 1, 2}) .SequenceEqual(new int[]  { 1, 2}));

            Console.WriteLine("biggerTwo");
            Console.WriteLine(biggerTwo(new int[] { 1, 2 }, new int[] { 3, 4 }).SequenceEqual(new int[] { 3, 4 }));
            Console.WriteLine(biggerTwo(new int[] { 3, 4 }, new int[] { 1, 2 }).SequenceEqual(new int[] { 3, 4 }));
            Console.WriteLine(biggerTwo(new int[] { 1, 1 }, new int[] { 1, 2 }).SequenceEqual(new int[] { 1, 2 }));

            Console.WriteLine("makeMiddle");
            Console.WriteLine(makeMiddle(new int[] { 1, 2, 3, 4}) .SequenceEqual(new int[]  { 2, 3}));
            Console.WriteLine(makeMiddle(new int[] { 7, 1, 2, 3, 4, 9}) .SequenceEqual(new int[]  { 2, 3}));
            Console.WriteLine(makeMiddle(new int[] { 1, 2}).SequenceEqual(new int[] { 1, 2}));

            Console.WriteLine("plusTwo");
            Console.WriteLine(plusTwo(new int[] { 1, 2}, new int[] { 3, 4}).SequenceEqual(new int[] { 1, 2, 3, 4}));
            Console.WriteLine(plusTwo(new int[] { 4, 4}, new int[] { 2, 2}).SequenceEqual(new int[] { 4, 4, 2, 2}));
            Console.WriteLine(plusTwo(new int[] { 9, 2}, new int[] { 3, 4}).SequenceEqual(new int[] { 9, 2, 3, 4}));

            Console.WriteLine("plusTwo");
            Console.WriteLine(plusTwo(new int[] { 1, 2 }, new int[] { 3, 4 }).SequenceEqual(new int[] { 1, 2, 3, 4 }));
            Console.WriteLine(plusTwo(new int[] { 4, 4 }, new int[] { 2, 2 }).SequenceEqual(new int[] { 4, 4, 2, 2 }));
            Console.WriteLine(plusTwo(new int[] { 9, 2 }, new int[] { 3, 4 }).SequenceEqual(new int[] { 9, 2, 3, 4 }));

            Console.WriteLine("swapEnds");
            Console.WriteLine(swapEnds(new int[] { 1, 2, 3, 4}).SequenceEqual(new int[] { 4, 2, 3, 1}));
            Console.WriteLine(swapEnds(new int[] { 1, 2, 3}).SequenceEqual(new int[] { 3, 2, 1}));
            Console.WriteLine(swapEnds(new int[] { 8, 6, 7, 9, 5}).SequenceEqual(new int[] { 5, 6, 7, 9, 8}));

            Console.WriteLine("midN");
            Console.WriteLine(midThree(new int[] { 1, 2, 3, 4, 5}).SequenceEqual(new int[] { 2, 3, 4}));
            Console.WriteLine(midThree(new int[] { 8, 6, 7, 5, 3, 0, 9}).SequenceEqual(new int[] { 7, 5, 3}));
            Console.WriteLine(midThree(new int[] { 1, 2, 3}).SequenceEqual(new int[] { 1, 2, 3}));

            Console.WriteLine("midN");
            Console.WriteLine(midThree(new int[] { 1, 2, 3, 4, 5 }).SequenceEqual(new int[] { 2, 3, 4 }));
            Console.WriteLine(midThree(new int[] { 8, 6, 7, 5, 3, 0, 9 }).SequenceEqual(new int[] { 7, 5, 3 }));
            Console.WriteLine(midThree(new int[] { 1, 2, 3 }).SequenceEqual(new int[] { 1, 2, 3 }));


            Console.WriteLine("maxTriple");
            Console.WriteLine(maxTriple(new int[] { 1, 2, 3}) == 3);
            Console.WriteLine(maxTriple(new int[] { 1, 5, 3}) == 5);
            Console.WriteLine(maxTriple(new int[] { 5, 2, 3}) == 5);

            Console.WriteLine("front2");
            Console.WriteLine(front2(new int[] { 1, 2, 3}).SequenceEqual(new int[] { 1, 2}));
            Console.WriteLine(front2(new int[] { 1, 2}).SequenceEqual(new int[] { 1, 2}));
            Console.WriteLine(front2(new int[] { 1 }).SequenceEqual(new int[] { 1 }));

            Console.WriteLine("frontN");
            Console.WriteLine(frontN(new int[] { 1, 2, 3 }, 2).SequenceEqual(new int[] { 1, 2 }));
            Console.WriteLine(frontN(new int[] { 1, 2 }, 2).SequenceEqual(new int[] { 1, 2 }));
            Console.WriteLine(frontN(new int[] { 1 }, 2).SequenceEqual(new int[] { 1 }));

            Console.WriteLine("frontNLinq");
            Console.WriteLine(frontNLinq(new int[] { 1, 2, 3 }, 2).SequenceEqual(new int[] { 1, 2 }));
            Console.WriteLine(frontNLinq(new int[] { 1, 2 }, 2).SequenceEqual(new int[] { 1, 2 }));
            Console.WriteLine(frontNLinq(new int[] { 1 }, 2).SequenceEqual(new int[] { 1 }));

            Console.WriteLine("unlucky1");
            Console.WriteLine(unlucky1(new int[] { 1, 3, 4, 5}) == true);
            Console.WriteLine(unlucky1(new int[] { 2, 1, 3, 4, 5}) == true);
            Console.WriteLine(unlucky1(new int[] { 1, 1, 1}) == false);

            Console.WriteLine("makeN");
            Console.WriteLine(make2(new int[] { 4, 5}, new int[] { 1, 2, 3}).SequenceEqual(new int[] { 4, 5}));
            Console.WriteLine(make2(new int[] { 4}, new int[] { 1, 2, 3}).SequenceEqual(new int[] { 4, 1}));
            Console.WriteLine(make2(new int[] { }, new int[] { 1, 2}).SequenceEqual(new int[] { 1, 2}));

            Console.WriteLine("front11");
            Console.WriteLine(front11(new int[] { 1, 2, 3}, new int[] { 7, 9, 8}).SequenceEqual(new int[] { 1, 7}));
            Console.WriteLine(front11(new int[] { 1 }, new int[] { 2 }).SequenceEqual(new int[] { 1, 2}));
            Console.WriteLine(front11(new int[] { 1, 7}, new int[] { }).SequenceEqual(new int[] { 1 }));

            Console.WriteLine("front11List");
            Console.WriteLine(front11List(new int[] { 1, 2, 3 }, new int[] { 7, 9, 8 }).SequenceEqual(new int[] { 1, 7 }));
            Console.WriteLine(front11List(new int[] { 1 }, new int[] { 2 }).SequenceEqual(new int[] { 1, 2 }));
            Console.WriteLine(front11List(new int[] { 1, 7 }, new int[] { }).SequenceEqual(new int[] { 1 }));

