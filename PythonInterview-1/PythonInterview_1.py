import sys

class PythonInterview_1(object):

        '''
        print("isPalindrome")
        print("Is it a palindrome ignoring punctuation and case.")
        print(isPalindrome("A man, a plan, a canal: panama!") == True)
        '''
        def isPalindrome(word):
            sb = ""
            for c in word:
                if c.isdalpha() or c.isdigit():
                    sb += c.lower()
            
            for i in range(0, len(sb)/2):
                if sb[i] != sb[len(sb) - 1 - i]:
                    return False

            return True
        

        '''
        print("countLetters")
        print("Count times each letter appears in string")
        print(countLetters("The quick brown fox jumped over the lazy dogs."))
        '''
        def countLetters(sentence):
            counts = {}

            for ch in sentence:
                if ch.isalpha():
                    c = ch.lower()

                    if counts.ContainsKey(c):
                        counts[c] += 1
                    else:
                        counts.Add(c, 1)
                
            sb = ""

            list = counts.Keys.ToList()
            list.Sort()

            for key in list:
                sb += Line(key + " : " + counts[key])

            return sb
        

        '''
        print("countWords")
        print("Count times each word appears in string")
        print(countWords("This is fun and this is easy"))
        '''
        def countWords(sentence):
            counts = {}
            rawlist = []
            rawlist = sentence.lower().strip().split()

            for word in rawlist:
                if counts.ContainsKey(word):
                    counts[word] += 1
                else:
                    counts.Add(word, 1)

            sb = ""
            list = counts.Keys.ToList()
            list.Sort()

            for key in list:
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
