import sys

class PythonLogic_1(object):

            /*
        Given three ints, a b c, return true if two or more of them have the same 
        rightmost digit. The ints are non-negative.

        lastDigit(23, 19, 13) ? true
        lastDigit(23, 19, 12) ? false
        lastDigit(23, 19, 3) ? true        
        */
        public static bool lastDigit(params int[] values)
        {
            List<int> digits = new List<int>();
            foreach (int val in values)
                if (digits.Contains(val % 10))
                    return true;
                else
                    digits.Add(val % 10);
            return false;
        }

        /*
        Given three ints, a b c, return true if one of them is 10 or more less than 
        one of the others. 

        lessBy10(1, 7, 11) ? true
        lessBy10(1, 7, 10) ? false
        lessBy10(11, 1, 7) ? true        
        */
        public static bool lessBy10(params int[] values)
        {
            foreach (int val in values)
                if (values.Contains(val - 10) || values.Contains(val + 10))
                    return true;
            return false;
        }


        /*
            Return the sum of two 6-sided dice rolls, each in the range 1..6. 
            However, if noDoubles is true, if the two dice show the same value, 
            increment one die to the next value, wrapping around to 1 if its value was 6. 

            withoutDoubles(2, 3, true) ? 5
            withoutDoubles(3, 3, true) ? 7
            withoutDoubles(3, 3, false) ? 6        
        */
        public static int withoutDoubles(int die1, int die2, bool noDoubles)
        {
            if (noDoubles && (die1 == die2))
                if (die1 == 6)
                    die1 = 1;
                else 
                    die1++;

            return die1 + die2;
        }

        /*
        Given two int values, return whichever value is larger. 
        However if the two values have the same remainder when divided by 5, 
        then the return the smaller value. However, in all cases, if the two 
        values are the same, return 0.

        maxMod5(25, 15) ? 15
        maxMod5(6, 2) ? 6
        maxMod5(3, 3) ? 0        
        */
        public static int maxMod5(params int[] values)
        {
            HashSet<int> vals = new HashSet<int>();
            HashSet<int> mods = new HashSet<int>();
 
            foreach (int val in values)
            {
                 vals.Add(val);
                 mods.Add(val % 5);
            }

            if (vals.Count < 2)
                return 0;
            else if (mods.Count < 2)
                return vals.Min();
            else
                return vals.Max();

        }

        /*
        You have a red lottery ticket showing ints a, b, and c, each of which 
        is 0, 1, or 2. If they are all the value 2, the result is 10. Otherwise 
        if they are all the same, the result is 5. Otherwise so long as both 
        b and c are different from a, the result is 1. Otherwise the result is 0. 

        redTicket(2, 2, 2) ? 10
        redTicket(2, 2, 1) ? 0
        redTicket(0, 0, 0) ? 5        
        */
        public static int redTicket(params int[] values)
        {
            HashSet<int> vals = new HashSet<int>(values);
            if (vals.Count == 1)
                if (vals.Contains(2))
                    return 10;
                else
                    return 5;
            else
                return 0;
        
        }

        /*
        You have a green lottery ticket, with ints a, b, and c on it. 
        If the numbers are all different from each other, the result is 0. 
        If all of the numbers are the same, the result is 20. 
        If two of the numbers are the same, the result is 10. 

        greenTicket(1, 2, 3) ? 0
        greenTicket(2, 2, 2) ? 20
        greenTicket(1, 1, 2) ? 10        
        */
        public static int greenTicket(params int[] values)
        {
            bool allSame = true;
            bool allDifferent = true;

            for (int i = 0; i < values.Length; i++)
            {
                for (int j = i + 1; j < values.Length; j++)
                {
                    if (values[i] != values[j])
                        allSame = false;
                    if (values[i] == values[j])
                        allDifferent = false;
                }
            }

            if (allSame)
                return 20;
            else if (allDifferent)
                return 0;
            else
                return 10;
        }

        /*
        You have a blue lottery ticket, with ints a, b, and c on it. 
        This makes three pairs, which we'll call ab, bc, and ac. 
        Consider the sum of the numbers in each pair. 
        If any pair sums to exactly 10, the result is 10. 
        Otherwise if the ab sum is exactly 10 more than either bc or ac sums, 
        the result is 5. Otherwise the result is 0. 

        blueTicket(9, 1, 0) ? 10
        blueTicket(9, 2, 0) ? 0
        blueTicket(14, 1, 4) ? 5        
        */
        public static int blueTicket(params int[] values)
        {
            HashSet<int> pairs = new HashSet<int>();

            for(int i = 0; i < values.Length; i++)
            {
                for(int j = 0; j < values.Length; j++)
                {
                    if (i != j)
                    {
                        int pair = values[i] + values[j];
                        if (pair == 10)
                            return 10;
                        else if (pairs.Contains(pair - 10))
                            return 5;
                        else if (pairs.Contains(pair + 10))
                            return 5;
                        else
                            pairs.Add(pair);
                    }
                }
            }
            return 0;
        }

        /*
        Given two ints, each in the range 10..99, return true if there is 
        a digit that appears in both numbers, such as the 2 in 12 and 23.

        shareDigit(12, 23) ? true
        shareDigit(12, 34) ? false
        shareDigit(12, 44) ? false        
        */
        public static bool shareDigit(params int[] values)
        {
            List<HashSet<int>> list = new List<HashSet<int>>();

            for(int i = 0; i < values.Length; i++)
            {
                HashSet<int> digits = new HashSet<int>();

                if (values[i] == 0)
                    digits.Add(values[i]);
                else
                {
                    while (values[i] != 0)
                    {
                        digits.Add(values[i] % 10);
                        values[i] /= 10;
                    }
                }

                list.Add(digits);
            }

            for (int i = 0; i < list.Count - 1; i++)
                for (int j = i + 1; j < list.Count; j++)
                    foreach(int n in list[i])
                        if (list[j].Contains(n))
                            return true;

            return false;
        }

        /*
        Given two ints, each in the range 10..99, return true if there is 
        a digit that appears in both numbers, such as the 2 in 12 and 23.
        Use Linq. Do not use loops.
        shareDigitLinq(12, 23) ? true
        shareDigitLinq(12, 34) ? false
        shareDigitLinq(12, 44) ? false        
        */
        public static bool shareDigitLinq(params int[] values)
        {
            string[] words = Array.ConvertAll(values, x => x.ToString());

            for (int i = 0; i < words.Length; i++)
                for (int j = 0; j < words.Length; j++)
                    if (i != j && words[i].Intersect(words[j]).Any())
                        return true;
                    
            return false;
        }

        /*
            Calculate the sum and the maximum of the passed-in values. 
            If the sum and maximum have the same number of digits then 
            return the sum, otherwise return the maximum.

            sumLimit(2, 3) ? 5
            sumLimit(8, 3) ? 8
            sumLimit(-12, 3) ? -9       
        */
        public static int sumLimit(params int[] values)
        {
            int sum = values.Sum();
            int max = values.Max();
            int sumDigits = Math.Abs(sum).ToString().Length;
            int maxDigits = Math.Abs(max).ToString().Length;
            return sumDigits == maxDigits ? sum : max;
        }


            Console.WriteLine("lastDigit");
            Console.WriteLine(lastDigit(23, 19, 13) ==  true);
            Console.WriteLine(lastDigit(23, 19, 12) == false);
            Console.WriteLine(lastDigit(23, 19, 3) == true);    

            Console.WriteLine("lessBy10");
            Console.WriteLine(lessBy10(1, 7, 11) == true);
            Console.WriteLine(lessBy10(1, 7, 10) == false);
            Console.WriteLine(lessBy10(11, 1, 7) == true);     

            Console.WriteLine("withoutDoubles");
            Console.WriteLine(withoutDoubles(6, 6, true) == 7);
            Console.WriteLine(withoutDoubles(2, 3, true) == 5);
            Console.WriteLine(withoutDoubles(3, 3, true) == 7);
            Console.WriteLine(withoutDoubles(3, 3, false) == 6);       

            Console.WriteLine("maxMod5");
            Console.WriteLine(maxMod5(25, 15) == 15);
            Console.WriteLine(maxMod5(6, 2) == 6);
            Console.WriteLine(maxMod5(3, 3) == 0);      

            Console.WriteLine("redTicket");
            Console.WriteLine(redTicket(2, 2, 2) == 10);
            Console.WriteLine(redTicket(2, 2, 1) == 0);
            Console.WriteLine(redTicket(0, 0, 0) == 5);      

            Console.WriteLine("greenTicket");
            Console.WriteLine(greenTicket(1, 2, 3) == 0);
            Console.WriteLine(greenTicket(2, 2, 2) == 20);
            Console.WriteLine(greenTicket(1, 1, 2) == 10);      
            
            Console.WriteLine("blueTicket");
            Console.WriteLine(blueTicket(14, 1, 4) == 5);
            Console.WriteLine(blueTicket(9, 1, 0) == 10);
            Console.WriteLine(blueTicket(9, 2, 0) == 0);

            Console.WriteLine("shareDigit");
            Console.WriteLine(shareDigit(12, 34, 56, 78, 90, 0) == true);
            Console.WriteLine(shareDigit(12, 23) == true);
            Console.WriteLine(shareDigit(12, 34) == false);
            Console.WriteLine(shareDigit(12, 44) == false);      
            
            Console.WriteLine("shareDigitLinq");
            Console.WriteLine(shareDigitLinq(12, 34, 56, 78, 90, 0) == true);
            Console.WriteLine(shareDigitLinq(12, 23) == true);
            Console.WriteLine(shareDigitLinq(12, 34) == false);
            Console.WriteLine(shareDigitLinq(12, 44) == false);


            Console.WriteLine("sumLimit");
            Console.WriteLine(sumLimit(-12, 3) == -9);
            Console.WriteLine(sumLimit(2, 3) == 5);
            Console.WriteLine(sumLimit(8, 3) == 8);
