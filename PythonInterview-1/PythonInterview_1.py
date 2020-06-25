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
                if c.isalpha() or c.isdigit():
                    sb += c.lower()
            
            mid = int(len(sb)/2)
            for i in range(mid):
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

                    if c in counts:
                        counts[c] += 1
                    else:
                        counts[c] = 1
            
            sb = ""
            for key, value in sorted(counts.items()):
                sb += key + ' : ' + str(value) + '\n'

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
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

            sb = ""
            for key, value in sorted(counts.items()):
                sb += key + ' : ' + str(value) + '\n'

            return sb
        


        print("isPalindrome")
        print("A man, a plan, a canal: Panama!")
        print(isPalindrome("A man, a plan, a canal: Panama!") == True)

        print("countLetters")
        print("The quick brown fox jumped over the lazy dogs.")
        print(countLetters("The quick brown fox jumped over the lazy dogs."))

        print("countWords")
        print("This is fun and this is easy")
        print(countWords("This is fun and this is easy"))
