import sys

class PythonWarmup_2(object):

            /*
        Given a string and a non-negative int n, return a larger string 
        that is n copies of the original string. 
        stringTimes("Hi", 2) ? "HiHi"
        stringTimes("Hi", 3) ? "HiHiHi"
        stringTimes("Hi", 1) ? "Hi"
        */
        public static String stringTimes(string str, int n)
        {
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < n; i++)
                sb.Append(str);

            return sb.ToString();
        }

        /*
        Given a string and a non-negative int n, return a larger string 
        that is n copies of the original string. Use Linq. Do not use loops.
        stringTimesLinq("Hi", 2) ? "HiHi"
        stringTimesLinq("Hi", 3) ? "HiHiHi"
        stringTimesLinq("Hi", 1) ? "Hi"
        */
        public static String stringTimesLinq(string str, int n)
        {
            return String.Concat(Enumerable.Repeat(str, n));
        }

        /*
        Given a string and a non-negative int n, 
        we'll say that the front of the string is the first 3 chars, 
        or whatever is there if the string is less than length 3. 
        Return n copies of the front; 

        frontTimes("Chocolate", 2) ? "ChoCho"
        frontTimes("Chocolate", 3) ? "ChoChoCho"
        frontTimes("Abc", 3) ? "AbcAbcAbc"
        */
        public static String frontTimes(string str, int n)
        {
            StringBuilder sb = new StringBuilder();
            string front = str.Substring(0, Math.Min(str.Length, 3));

            for (int i = 0; i < n; i++)
                sb.Append(front);

            return sb.ToString();
        }

        /*
        Given a string and a non-negative int n, 
        we'll say that the front of the string is the first 3 chars, 
        or whatever is there if the string is less than length 3. 
        Return n copies of the front. Use Linq. Do not use loops.

        frontTimesLinq("Chocolate", 2) ? "ChoCho"
        frontTimesLinq("Chocolate", 3) ? "ChoChoCho"
        frontTimesLinq("Abc", 3) ? "AbcAbcAbc"
        */
        public static String frontTimesLinq(string str, int n)
        {
            return String.Concat(Enumerable.Repeat(str.Substring(0, 3), n));
        }

        /*
        Count the number of "xx" in the given string. 
        We'll say that overlapping is allowed, so "xxx" contains 2. 
        countXX("abcxx") ? 1
        countXX("xxx") ? 2
        countXX("xxxx") ? 3
        */
        public static int countXX(String str)
        {
            int count = 0;

            for (int i = 1; i < str.Length; i++)
                if (str[i] == 'x' && str[i - 1] == 'x')
                    count++;

            return count;
        }

        /*
        Count the number of "xx" in the given string. 
        We'll say that overlapping is allowed, so "xxx" contains 2. 
        Use Linq. Do not use loops.
        countXXLinq("abcxx") ? 1
        countXXLinq("xxx") ? 2
        countXXLinq("xxxx") ? 3
        */
        public static int countXXLinq(String str)
        {
            return str.Skip(1)
                .Where((value, index) => value == 'x' && str[index] == 'x')
                .Count();
        }

        /*
        Given a string, return true if the first instance of "x" in the string 
        is immediately followed by another "x". 
        doubleX("axxbb") ? true
        doubleX("axaxx") ? false
        doubleX("xxxxx") ? true
        */
        public static bool doubleX(string str)
        {
            string lowerCaseStr = str.ToLower();
            int pos = lowerCaseStr.IndexOf('x');
            return pos > -1 && pos < str.Length - 1 && lowerCaseStr[pos + 1] == 'x';
        }

        /*
        Given a string, return a new string made of every other char starting 
        with the first, so "Hello" yields "Hlo". 

        stringBits("Hello") ? "Hlo"
        stringBits("Hi") ? "H"
        stringBits("Heeololeo") ? "Hello"
        */

        public static string stringBits(string str)
        {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < str.Length; i += 2)
                sb.Append(str[i]);
            return sb.ToString();
        }

        /*
            Given a non-empty string like "Code" return a string like "CCoCodCode". 

            stringSplosion("Code") ? "CCoCodCode"
            stringSplosion("abc") ? "aababc"
            stringSplosion("ab") ? "aab"
        */
        public static string stringSplosion(string str)
        {
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < str.Length; i++)
            {
                sb.Append(str.Substring(0, i+1));
            }
            return sb.ToString();
        }
        /*

           Given a string, return a version where all the "x" have been removed. 
           Except an "x" at the very start or end should not be removed. 

           stringX("xxHxix") ? "xHix"
           stringX("abxxxcd") ? "abcd"
           stringX("xabxxxcdx") ? "xabcdx"
        */
        public static string stringX(string str)
        {
            string noX = Regex.Replace(str.Substring(1, str.Length - 2), "x", "", RegexOptions.IgnoreCase);
            return str[0] + noX + str[str.Length - 1];
        }

        /*
            Given a string, return a string made of the chars at 
            indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien". 

            altPairs("kitten") ? "kien"
            altPairs("Chocolate") ? "Chole"
            altPairs("CodingHorror") ? "Congrr
        */
        public static string altPairs(string str)
        {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < str.Length; i += 4)
            {
                sb.Append(str[i]);
                if (i < str.Length - 1)
                    sb.Append(str[i + 1]);
            }
            return sb.ToString();
        }

        /*
        Suppose the string "yak" is unlucky. 
        Given a string, return a version where all the "yak" are removed, 
        but the "a" can be any char. The "yak" strings will not overlap. 

        stringYak("yakpak") ? "pak"
        stringYak("pakyak") ? "pak"
        stringYak("yak123ya") ? "123ya"
        */
        public static string stringYak(string str)
        {
            return System.Text.RegularExpressions.Regex.Replace(str, "y.k", "");
        }

        /*
        
        Given an array of ints, we'll say that a triple is a value appearing 3 times 
        in a row in the array. Return true if the array does not contain any triples. 

        noTriples({1, 1, 2, 2, 1}) ? true
        noTriples({1, 1, 2, 2, 2, 1}) ? false
        noTriples({1, 1, 1, 2, 2, 2, 1}) ? false
        */
        public static Boolean noTriples(int[] nums)
        {
            for (int i = 2; i < nums.Length; i++)
                if (nums[i] == nums[i - 1] && nums[i] == nums[i - 2])
                    return false;

            return true;
        }

        /*
        
        Given an array of ints, we'll say that a triple is a value appearing 3 times 
        in a row in the array. Return true if the array does not contain any triples. 
        Use Linq. Do not use loops.
        noTriplesLinq({1, 1, 2, 2, 1}) ? true
        noTriplesLinq({1, 1, 2, 2, 2, 1}) ? false
        noTriplesLinq({1, 1, 1, 2, 2, 2, 1}) ? false
        */
        public static Boolean noTriplesLinq(int[] nums)
        {
            return nums
                .Where((value, index) => index > 1
                && value == nums[index - 1]
                && value == nums[index - 2])
                .Count() == 0;
        }




                Console.WriteLine("stringTimes");
            Console.WriteLine(stringTimes("Hi", 2) == "HiHi");
            Console.WriteLine(stringTimes("Hi", 3) == "HiHiHi");
            Console.WriteLine(stringTimes("Hi", 1) == "Hi");

            Console.WriteLine("stringTimesLinq");
            Console.WriteLine(stringTimesLinq("Hi", 2) == "HiHi");
            Console.WriteLine(stringTimesLinq("Hi", 3) == "HiHiHi");
            Console.WriteLine(stringTimesLinq("Hi", 1) == "Hi");

            Console.WriteLine("frontTimes");
            Console.WriteLine(frontTimes("Chocolate", 2) == "ChoCho");
            Console.WriteLine(frontTimes("Chocolate", 3) == "ChoChoCho");
            Console.WriteLine(frontTimes("Abc", 3) == "AbcAbcAbc");

            Console.WriteLine("frontTimesLinq");
            Console.WriteLine(frontTimesLinq("Chocolate", 2) == "ChoCho");
            Console.WriteLine(frontTimesLinq("Chocolate", 3) == "ChoChoCho");
            Console.WriteLine(frontTimesLinq("Abc", 3) == "AbcAbcAbc");

            Console.WriteLine("countXX");
            Console.WriteLine(countXX("abcxx") == 1);
            Console.WriteLine(countXX("xxx") == 2);
            Console.WriteLine(countXX("xxxx") == 3);

            Console.WriteLine("countXXLinq");
            Console.WriteLine(countXXLinq("abcxx") == 1);
            Console.WriteLine(countXXLinq("xxx") == 2);
            Console.WriteLine(countXXLinq("xxxx") == 3);

            Console.WriteLine("doubleX");
            Console.WriteLine(doubleX("axXbb") == true);
            Console.WriteLine(doubleX("axaxx") == false);
            Console.WriteLine(doubleX("Xxxxx") == true);

            Console.WriteLine("stringBits");
            Console.WriteLine(stringBits("Hello") == "Hlo");
            Console.WriteLine(stringBits("Hi") == "H");
            Console.WriteLine(stringBits("Heeololeo") == "Hello");

            Console.WriteLine("stringSplosion");
            Console.WriteLine(stringSplosion("Code") == "CCoCodCode");
            Console.WriteLine(stringSplosion("abc") == "aababc");
            Console.WriteLine(stringSplosion("ab") == "aab");

            Console.WriteLine("stringX");
            Console.WriteLine(stringX("xxHxix") == "xHix");
            Console.WriteLine(stringX("abxxxcd") == "abcd");
            Console.WriteLine(stringX("xabxxxcdx") == "xabcdx");

            Console.WriteLine("altPairs");
            Console.WriteLine(altPairs("kitten") == "kien");
            Console.WriteLine(altPairs("Chocolate") == "Chole");
            Console.WriteLine(altPairs("CodingHorror") == "Congrr");

            Console.WriteLine("stringYak");
            Console.WriteLine(stringYak("yakpak") == "pak");
            Console.WriteLine(stringYak("pakyak") == "pak");
            Console.WriteLine(stringYak("yak123ya") == "123ya");

            Console.WriteLine("noTriples");
            Console.WriteLine(noTriples(new int[] { 1, 1, 2, 2, 1}) == true);
            Console.WriteLine(noTriples(new int[] { 1, 1, 2, 2, 2, 1}) == false);
            Console.WriteLine(noTriples(new int[] { 1, 1, 1, 2, 2, 2, 1}) == false);

            Console.WriteLine("noTriplesLinq");
            Console.WriteLine(noTriplesLinq(new int[] { 1, 1, 2, 2, 1 }) == true);
            Console.WriteLine(noTriplesLinq(new int[] { 1, 1, 2, 2, 2, 1 }) == false);
            Console.WriteLine(noTriplesLinq(new int[] { 1, 1, 1, 2, 2, 2, 1 }) == false);
