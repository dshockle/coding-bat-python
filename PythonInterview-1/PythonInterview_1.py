import sys

class PythonInterview_1(object):

        '''
        print("isPalindrome")
        print("Is it a palindrome ignoring punctuation and case.")
        print(isPalindrome("A man, a plan, a canal: panama!") == True)
        '''
        def isPalindrome(string word):
            sb = ""
            for char c in word:
                if char.IsLetterOrDigit(c):
                    sb += (char.ToLower(c))
            
            for (int i = 0 i < len(sb) / 2 i++):
                if sb[i] != sb[len(sb) - 1 - i]:
                    return False

            return True
        

        '''
        print("isPalindrome")
        print("Is it a palindrome ignoring punctuation and case.")
        print(isPalindromeLinq("A man, a plan, a canal: panama!") == True)
        Use Linq. Do not use loops.
        '''
        def isPalindromeLinq(string word)
            char[] chars = word.ToLower().Trim()
                    .Where(c => Char.IsLetterOrDigit(c))
                    .ToArray()

            return chars.SequenceEqual(chars.Reverse())
        

        '''
        print("countLetters")
        print("Count times each letter appears in string")
        print(countLetters("The quick brown fox jumped over the lazy dogs."))
        '''
        def countLetters(String sentence):
            Dictionary<char, int> counts  =  new Dictionary<char, int>()

            for char ch in sentence:
                if char.IsLetterOrDigit(ch):
                
                    char c = char.ToLower(ch)

                    if counts.ContainsKey(c):
                        counts[c]++
                    else:
                        counts.Add(c, 1)
                
            

            sb = ""

            var list = counts.Keys.ToList()
            list.Sort()

            for var key in list)
                sb += Line(key + " : " + counts[key])

            return sb
        

        '''
        print("countWords")
        print("Count times each word appears in string")
        print(countWords("This is fun and this is easy"))
        '''
        def countWords(String sentence):
        
            Dictionary<string, int> counts = new Dictionary<string, int>()
            string[] rawlist = sentence.ToLower().Trim().Split()
            '''
            var rawlist = sentence
                          .ToLower().Trim().Split()
                          .Select(word => word.Trim())
                          .Where(word => !string.IsNullOrEmpty(word))
            '''
            for string word in rawlist:
            
                if counts.ContainsKey(word):
                    counts[word]++
                else:
                    counts.Add(word, 1)
            

            sb = ""

            var list = counts.Keys.ToList()
            list.Sort()

            for var key in list:
                sb += Line(key + " : " + counts[key])

            return sb

        


            print("isPalindrome")
            print(isPalindrome("A man, a plan, a canal: Panama!") == True)

            print("isPalindromeLinq")
            print(isPalindromeLinq("A man, a plan, a canal: Panama!") == True)

            print("countLetters")
            print(countLetters("The quick brown fox jumped over the lazy dogs."))

            print("countWords")
            print(countWords("This is fun and this is easy"))
