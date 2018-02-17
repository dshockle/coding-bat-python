import sys

class PythonString_1(object):

            /*
        Given a string, if the string begins with "red" or "blue" return that color string, 
        otherwise return the empty string. 

        seeColor("redxx") ? "red"
        seeColor("xxred") ? ""
        seeColor("blueTimes") ? "blue"
        */
        public static string seeColor(string str)
        {
            var values = Enum.GetNames(typeof(Colors));
            foreach (string color in values)
            {
                if (str.Trim().ToLower().StartsWith(color))
                    return color;
            }
            return "";
        }
        private enum Colors { red, green, blue, yellow };

        /*
        Given a string, if the string begins with "red" or "blue" return that color string, 
        otherwise return the empty string. Use Linq. Do not use loops.

        seeColorLinq("redxx") ? "red"
        seeColorLinq("xxred") ? ""
        seeColorLinq("blueTimes") ? "blue"
        */
        public static string seeColorLinq(string str)
        {
            var values = Enum.GetNames(typeof(Colors));
            return values.Where(value => str.Trim().ToLower().StartsWith(value))
                         .DefaultIfEmpty(string.Empty).First();
        }

        /*
        Given a string, return true if the first 2 chars in the string also appear at 
        the end of the string, such as with "edited". 

        frontAgain("edited") ? true
        frontAgain("edit") ? false
        frontAgain("ed") ? true
        */
        public static Boolean frontAgain(string str)
        {
            return str.Substring(0, 2)
                .Equals(str.Substring(str.Length - 2), 
                StringComparison.CurrentCultureIgnoreCase);
        }

        /*
            Given two strings, append them together and return the result. 
            However, if the strings are different lengths, omit chars 
            from the longer string so it is the same length as the 
            shorter string. So "Hello" and "Hi" yield "loHi". 
            The strings may be any length including empty. 

            minCat("Hello", "Hi") ? "loHi"
            minCat("Hello", "java") ? "ellojava"
            minCat("java", "Hello") ? "javaello"        
        */
        public static string minCat(string a, string b)
        {
            if (a.Length > b.Length)
                return a.Substring(a.Length - b.Length) + b;
            else if (a.Length < b.Length)
                return a + b.Substring(b.Length - a.Length);
            else
                return a + b;
        }

        /*
        Given a string, return a new string made of n copies of the first n chars. 
        If there are fewer than n chars, use whatever is there. 

        extraFront("Hello", 3) ? "HelHelHel"
        extraFront("ab", 2) ? "abab"
        extraFront("H", 3) ? "HHH"        
        */
        public static string extraFront(string str, int n)
        {
            string item = str.Substring(0, Math.Min(n, str.Length));
            return string.Concat(Enumerable.Repeat(item, n));
        }

        /*

        Given a string, if a length 2 substring appears at both its beginning 
        and end, return a string without the substring at the beginning, 
        so "HelloHe" yields "lloHe". The substring may overlap with itself, 
        so "Hi" yields "". Otherwise, return the original string unchanged. 

        without2("HelloHe") ? "lloHe"
        without2("HelloHi") ? "HelloHi"
        without2("Hi") ? ""        
        */
        public static string without2(string str)
        {
            if (string.IsNullOrEmpty(str))
                return "";
            else if (str.Length < 2)
                return str;
            else if (str.Substring(0, 2).Equals(str.Substring(str.Length - 2),
                StringComparison.CurrentCultureIgnoreCase))
                return str.Substring(2);
            else
                return str;
        }

        /*
            Given a string, return a version without the first 2 chars. 
            Except keep the first char if it is 'a' and keep the second 
            char if it is 'b'. The string may be any length. Harder than it looks. 

            deFront("Hello") ? "llo"
            deFront("java") ? "va"
            deFront("away") ? "aay"        
        */
        public static string deFront(string str)
        {
            StringBuilder sb = new StringBuilder();
            if (str.Length > 0 && str[0] == 'a')
                sb.Append(str[0]);
            if (str.Length > 1 && str[1] == 'b')
                sb.Append(str[1]);
            if (str.Length > 2)
                sb.Append(str.Substring(2));
            return sb.ToString();
        }

        /*
            Given a string and a second "word" string, we'll say that the word matches 
            the string if it appears at the front of the string, except its first char 
            does not need to match exactly. On a match, return the front of the string, 
            or otherwise return the empty string. So, so with the string "hippo" 
            the word "hi" returns "hi" and "xip" returns "hip". The word will be at 
            least length 1. 

            startWord("hippo", "hi") ? "hi"
            startWord("hippo", "xip") ? "hip"
            startWord("hippo", "z") ? "h"        
        */
        public static string startWord(string str, string word)
        {
            if (str.Substring(1, word.Length - 1).Equals(word.Substring(1)))
                return str.Substring(0, word.Length);
            else
                return "";
        }

        /*
            Given a string, if the first or last chars are 'x', return the string 
            without those 'x' chars, and otherwise return the string unchanged. 

            withoutX("xHix") ? "Hi"
            withoutX("xHi") ? "Hi"
            withoutX("Hxix") ? "Hxi"        
        */
        public static string withoutX(string str)
        {
            StringBuilder sb = new StringBuilder();

            if (str.Length > 0 && str[0] != 'x')
                sb.Append(str[0]);

            if (str.Length > 2)
                sb.Append(str.Substring(1, str.Length - 2));

            if (str.Length > 1 && str[str.Length - 1] != 'x')
                sb.Append(str[str.Length - 1]);

            return sb.ToString();
        }

        /*
            Given a string, if one or both of the first 2 chars is 'x', return 
            the string without those 'x' chars, and otherwise return the string 
            unchanged. This is a little harder than it looks. 

            withoutX2("xHi") ? "Hi"
            withoutX2("Hxi") ? "Hi"
            withoutX2("Hi") ? "Hi"        
        */
        public static string withoutX2(string str)
        {
            StringBuilder sb = new StringBuilder();

            if (str.Length > 0 && str[0] != 'x')
                sb.Append(str[0]);

            if (str.Length > 1 && str[1] != 'x')
                sb.Append(str[1]);

            if (str.Length > 2)
                sb.Append(str.Substring(2));

            return sb.ToString();
        }


                Console.WriteLine("seeColor");
            Console.WriteLine(seeColor("redxx") == "red");
            Console.WriteLine(seeColor("xxred") == "");
            Console.WriteLine(seeColor("blueTimes") == "blue");

            Console.WriteLine("seeColorLinq");
            Console.WriteLine(seeColorLinq("redxx") == "red");
            Console.WriteLine(seeColorLinq("xxred") == "");
            Console.WriteLine(seeColorLinq("blueTimes") == "blue");
    
            Console.WriteLine("frontAgain");
            Console.WriteLine(frontAgain("edited") == true);
            Console.WriteLine(frontAgain("edit") == false);
            Console.WriteLine(frontAgain("ed") == true);

            Console.WriteLine("minCat");
            Console.WriteLine(minCat("Hello", "Hi") == "loHi");
            Console.WriteLine(minCat("Hello", "java") == "ellojava");
            Console.WriteLine(minCat("java", "Hello") == "javaello");

            Console.WriteLine("extraFront");
            Console.WriteLine(extraFront("Hello", 3) == "HelHelHel");
            Console.WriteLine(extraFront("ab", 2) == "abab");
            Console.WriteLine(extraFront("H", 3) == "HHH");

            Console.WriteLine("without2");
            Console.WriteLine(without2("HelloHe") == "lloHe");
            Console.WriteLine(without2("HelloHi") == "HelloHi");
            Console.WriteLine(without2("") == "");
            Console.WriteLine(without2(null) == "");
            Console.WriteLine(without2("H") == "H");
            Console.WriteLine(without2("Hi") == "");

            Console.WriteLine("deFront");
            Console.WriteLine(deFront("Hello") == "llo");
            Console.WriteLine(deFront("java") == "va");
            Console.WriteLine(deFront("away") == "aay");

            Console.WriteLine("startWord");
            Console.WriteLine(startWord("hippo", "hi") == "hi");
            Console.WriteLine(startWord("hippo", "xip") == "hip");
            Console.WriteLine(startWord("hippo", "z") == "h");

            Console.WriteLine("withoutX");
            Console.WriteLine(withoutX("xHix") == "Hi");
            Console.WriteLine(withoutX("xHi") == "Hi");
            Console.WriteLine(withoutX("Hxix") == "Hxi");

            Console.WriteLine("withoutX2");
            Console.WriteLine(withoutX2("xHi") == "Hi");
            Console.WriteLine(withoutX2("Hxi") == "Hi");
            Console.WriteLine(withoutX2("Hi") == "Hi");

