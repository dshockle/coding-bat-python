import sys

class PythonInterview_1(object):

        /*
        Console.WriteLine("isPalindrome");
        Console.WriteLine("Is it a palindrome ignoring punctuation and case.");
        Console.WriteLine(isPalindrome("A man, a plan, a canal: panama!") == true);
        */
        public static bool isPalindrome(string word)
        {
            StringBuilder sb = new StringBuilder();

            foreach (char c in word)
            {
                if (char.IsLetterOrDigit(c))
                    sb.Append(char.ToLower(c));
            }
            
            for (int i = 0; i < sb.Length / 2; i++)
                if (sb[i] != sb[sb.Length - 1 - i])
                    return false;

            return true;
        }

        /*
        Console.WriteLine("isPalindrome");
        Console.WriteLine("Is it a palindrome ignoring punctuation and case.");
        Console.WriteLine(isPalindromeLinq("A man, a plan, a canal: panama!") == true);
        Use Linq. Do not use loops.
        */
        public static bool isPalindromeLinq(string word)
        {
            char[] chars = word.ToLower().Trim()
                    .Where(c => Char.IsLetterOrDigit(c))
                    .ToArray();

            return chars.SequenceEqual(chars.Reverse());
        }

        /*
        Console.WriteLine("countLetters");
        Console.WriteLine("Count times each letter appears in string");
        Console.WriteLine(countLetters("The quick brown fox jumped over the lazy dogs."));
        */
        public static string countLetters(String sentence)
        {
            Dictionary<char, int> counts  =  new Dictionary<char, int>();

            foreach (char ch in sentence)
            {
                if (char.IsLetterOrDigit(ch))
                {
                    char c = char.ToLower(ch);

                    if (counts.ContainsKey(c))
                        counts[c]++;
                    else
                        counts.Add(c, 1);
                }
            }

            StringBuilder sb = new StringBuilder();

            var list = counts.Keys.ToList();
            list.Sort();

            foreach (var key in list)
                sb.AppendLine(key + " : " + counts[key]);

            return sb.ToString();
        }

        /*
        Console.WriteLine("countWords");
        Console.WriteLine("Count times each word appears in string");
        Console.WriteLine(countWords("This is fun and this is easy"));
        */
        public static string countWords(String sentence)
        {
            Dictionary<string, int> counts = new Dictionary<string, int>();
            string[] rawlist = sentence.ToLower().Trim().Split();
            /*
            var rawlist = sentence
                          .ToLower().Trim().Split()
                          .Select(word => word.Trim())
                          .Where(word => !string.IsNullOrEmpty(word));
            */
            foreach (string word in rawlist)
            {
                if (counts.ContainsKey(word))
                    counts[word]++;
                else
                    counts.Add(word, 1);
            }

            StringBuilder sb = new StringBuilder();

            var list = counts.Keys.ToList();
            list.Sort();

            foreach (var key in list)
                sb.AppendLine(key + " : " + counts[key]);

            return sb.ToString();

        }


            Console.WriteLine("isPalindrome");
            Console.WriteLine(isPalindrome("A man, a plan, a canal: Panama!") == true);

            Console.WriteLine("isPalindromeLinq");
            Console.WriteLine(isPalindromeLinq("A man, a plan, a canal: Panama!") == true);

            Console.WriteLine("countLetters");
            Console.WriteLine(countLetters("The quick brown fox jumped over the lazy dogs."));

            Console.WriteLine("countWords");
            Console.WriteLine(countWords("This is fun and this is easy"));
