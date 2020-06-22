import sys

class PythonAP_1(object):

        '''
        Given an array of scores, return True if each score is equal or greater than the one before. 
        The array will be length 2 or more. 

        scoresIncreasing({1, 3, 4}) -> True
        scoresIncreasing({1, 3, 2}) -> False
        scoresIncreasing({1, 1, 4}) -> True
        '''
        def scoresIncreasing(scores):
            result = True
            for i in range (1, len(scores)):
                if scores[i] < scores[i - 1]:
                    result = False
                    break
            return result


        '''
        Given an array of scores, return True if each score is equal or greater than the one before. 
        The array will be length 2 or more. 

        scoresIncreasing2({1, 3, 4}) -> True
        scoresIncreasing2({1, 3, 2}) -> False
        scoresIncreasing2({1, 1, 4}) -> True
        '''
        def scoresIncreasing2(scores):
            return all(scores[i] <= scores[i+1] for i in range(len(scores)-1))

        '''
        Given an array of scores, return True if there are scores of 100 next to each other in the array. 
        The array length will be at least 2. 

        scores100({1, 100, 100}) -> True
        scores100({1, 100, 99, 100}) -> False
        scores100({100, 1, 100, 100}) -> True
        '''
        def scores100(scores):
            for i in range(1, len(scores)):
                if (scores[i] == 100 and scores[i - 1] == 100):
                    return True
            return False


        '''
        Given an array of scores, return True if there are scores of 100 next to each other in the array. 
        The array length will be at least 2. 

        scores1002({1, 100, 100}) -> True
        scores1002({1, 100, 99, 100}) -> False
        scores1002({100, 1, 100, 100}) -> True
        '''
        def scores1002(scores):
            return any(100 == scores[i] == scores[i+1] for i in range(len(scores)-1))

        '''
        Given a sorted array, return True if the array contains 3 adjacent scores 
        that differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}. 

        scoresClump({3, 4, 5}) -> True
        scoresClump({3, 4, 6}) -> False
        scoresClump({1, 3, 5, 5}) -> True
        '''
        def scoresClump(scores):
            for i in range(1, len(scores) - 1):
                if (abs(scores[i - 1] - scores[i + 1]) <= 2):
                    return True
            return False

        '''
        Given a sorted array, return True if the array contains 3 adjacent scores 
        that differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}. 

        scoresClump2({3, 4, 5}) -> True
        scoresClump2({3, 4, 6}) -> False
        scoresClump2({1, 3, 5, 5}) -> True
        '''
        def scoresClump2(scores):
            return any(scores[i+1] - scores[i-1] <= 2 for i in range(1, len(scores)-1))


        '''
        Given an array of scores, compute the average of the first half and the second half, and return 
        whichever is larger. We'll say that the second half begins at index length/2. The array length will 
        be at least 2. Normally you would compute averages with doubles, but here we use ints so the expected 
        results are exact. 

        scoresAverage({2, 2, 4, 4}) -> 4
        scoresAverage({4, 4, 4, 2, 2, 2}) -> 4
        scoresAverage({3, 4, 5, 1, 2, 3}) -> 4
        '''
        def scoresAverage(scores):
            mid = int(len(scores)/2)
            avg1 = sum(scores[:mid])/mid
            avg2 = sum(scores[mid:])/mid
            return max(avg1, avg2)


        '''
        Given an array of strings, return the count of the number of strings with the given length. 

        wordsCount({"a", "bb", "b", "ccc"}, 1) -> 2
        wordsCount({"a", "bb", "b", "ccc"}, 3) -> 1
        wordsCount({"a", "bb", "b", "ccc"}, 4) -> 0
        '''
        def wordsCount(words, n):
            return sum(1 for word in words if len(word) == n)


        '''
        Given an array of strings, return a new array containing the first N strings. 
        N will be in the range 1..length.

        wordsFront({"a", "b", "c", "d"}, 1) -> {"a"}
        wordsFront({"a", "b", "c", "d"}, 2) -> {"a", "b"}
        wordsFront({"a", "b", "c", "d"}, 3) -> {"a", "b", "c"}
        '''
        def wordsFront(words, n):
            return words[:n]


        '''
        Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the 
        given length are omitted. 

        wordsWithout({"a", "bb", "b", "ccc"}, 1) -> {"bb", "ccc"}
        wordsWithout({"a", "bb", "b", "ccc"}, 3) -> {"a", "bb", "b"}
        wordsWithout({"a", "bb", "b", "ccc"}, 4) -> {"a", "bb", "b", "ccc"}
        '''
        def wordsWithout(words, n):
            result = []
            for word in words:
                if (len(word) != n):
                    result.append(word)
            return result;


        '''
        Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the 
        given length are omitted. 

        wordsWithout2({"a", "bb", "b", "ccc"}, 1) -> {"bb", "ccc"}
        wordsWithout2({"a", "bb", "b", "ccc"}, 3) -> {"a", "bb", "b"}
        wordsWithout2({"a", "bb", "b", "ccc"}, 4) -> {"a", "bb", "b", "ccc"}
        '''
        def wordsWithout2(words, n):
            return [word for word in words if len(word) != n]


        '''
        Given an n, return True if it contains a 1 digit. Use a loop.
        hasOne(10) -> True
        hasOne(22) -> False
        hasOne(220) -> False
        '''
        def hasOne(n):
            num = abs(n)
            while num > 0:
                digit = num % 10;
                if digit == 1:
                    return True
                num /= 10;
            return False

        '''
        Given an n, return True if it contains a 1 digit. Use a string.
        hasOne2(10) -> True
        hasOne2(22) -> False
        hasOne2(220) -> False
        '''
        def hasOne2(n):
            return "1" in str(n)


        '''
        We'll say that a positive divides itself if every digit in the number divides into the 
        number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. 
        We'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself. 

        dividesSelf(128) -> True
        dividesSelf(12) -> True
        dividesSelf(120) -> False
        '''
        def dividesSelf(n):
            if n == 0:
                return False
            num = abs(n)
            while num > 0:
                digit = n % 10;
                if digit == 0:
                    return False
                elif n % digit != 0:
                    return False
                num /= 10;
            return True


        '''
        Given an array of positive ints, return a new array of length "count" containing the first even 
        numbers from the original array. The original array will contain at least "count" even numbers. 

        copyEvens({3, 2, 4, 5, 8}, 2) -> {2, 4}
        copyEvens({3, 2, 4, 5, 8}, 3) -> {2, 4, 8}
        copyEvens({6, 1, 2, 4, 5, 8}, 3) -> {6, 2, 4}
        '''
        def copyEvens(nums, count):
            result = [0] * count
            rpos = 0
            npos = 0
            while rpos < count:
                if nums[npos] % 2 == 0:
                    result[rpos] = nums[npos]
                    rpos += 1
                npos += 1
            return result


        '''
        Given an array of positive ints, return a new array of length "count" containing the first even 
        numbers from the original array. The original array will contain at least "count" even numbers. 

        copyEvens2({3, 2, 4, 5, 8}, 2) -> {2, 4}
        copyEvens2({3, 2, 4, 5, 8}, 3) -> {2, 4, 8}
        copyEvens2({6, 1, 2, 4, 5, 8}, 3) -> {6, 2, 4}
        '''
        def copyEvens2(nums, count):
            evens = [x for x in nums if x % 2 == 0]
            return evens[:count]

        '''
        We'll say that a positive n is "endy" if it is in the range 0..10 or 90..100 (inclusive). 
        Given an array of positive ints, return a new array of length "count" containing the first endy 
        numbers from the original array. 

        copyEndy({9, 11, 90, 22, 6}, 2) -> {9, 90}
        copyEndy({9, 11, 90, 22, 6}, 3) -> {9, 90, 6}
        copyEndy({12, 1, 1, 13, 0, 20}, 2) -> {1, 1}
        '''
        def copyEndy(nums, count):
            result = []
            rpos = 0
            npos = 0
            while rpos < count:
                if (nums[npos] >= 0 and nums[npos] <= 10) or (nums[npos] >= 90 and nums[npos] <= 100):
                    result.append(nums[npos])
                    rpos += 1
                npos += 1
            return result


        '''
        Given 2 arrays that are the same length containing strings, compare the 1st string in one 
        array to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number 
        of times that the 2 strings are non-empty and start with the same char. The strings may be 
        any length, including 0. 

        matchUp({"aa", "bb", "cc"}, {"aaa", "xx", "bb"}) -> 1
        matchUp({"aa", "bb", "cc"}, {"aaa", "b", "bb"}) -> 2
        matchUp({"aa", "bb", "cc"}, {"", "", "ccc"}) -> 1
        '''
        def matchUp(a, b):
            count = 0
            end = min(len(a), len(b))
            for i in range (0,end):
                if (len(a[i]) > 0 and len(b[i])):
                    if (a[i][0] == b[i][0]):
                        count += 1
            return count



        '''
        The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. 
        The "answers" array contains a student's answers, with "?" representing a question left blank. 
        The two arrays are not empty and are the same length. Return the score for this array of answers, 
        giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer. 

        scoreUp({"a", "a", "b", "b"}, {"a", "c", "b", "c"}) -> 6
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "c"}) -> 11
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "b"}) -> 16
        '''
        def scoreUp(key, answers):
            score = 0;
            end = min(len(key), len(answers))
            for i in range(end):
                if len(key[i]) > 0 and len(answers[i]) > 0:
                    if (key[i] == answers[i]):
                        score += 4
                    elif (answers[i] != "?"):
                        score -= 1
            return score



        '''
        Given an array of strings, return a new array without the strings that are equal to the target 
        string.  

        wordsWithout({"a", "b", "c", "a"}, "a") -> {"b", "c"}
        wordsWithout({"a", "b", "c", "a"}, "b") -> {"a", "c", "a"}
        wordsWithout({"a", "b", "c", "a"}, "c") -> {"a", "b", "a"}
        '''
        def wordsWithout(words, target):
            return [word for word in words if word != target]


        '''
        Given two arrays, A and B, of non-negative scores. A "special" score is one which is a 
        multiple of 10, such as 40 or 90. Return the sum of largest special score in A and the largest 
        special score in B. 

        scoresSpecial({12, 10, 4}, {2, 20, 30}) -> 40
        scoresSpecial({20, 10, 4}, {2, 20, 10}) -> 40
        scoresSpecial({12, 11, 4}, {2, 20, 31}) -> 20
        '''
        def scoresSpecial(a, b):
            aMod = [x for x in a if x % 10 == 0]
            bMod = [x for x in b if x % 10 == 0]
            aMax = 0 if len(aMod) == 0 else max(aMod)
            bMax = 0 if len(bMod) == 0 else max(bMod)
            return aMax + bMax


        '''
        We have an array of heights, representing the altitude along a walking trail. Given start/end 
        indexes into the array, return the sum of the changes for a walk beginning at the start index 
        and ending at the end index. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 
        yields a sum of 1 + 5 = 6. The start end end index will both be valid indexes into the array 
        with start <= end. 

        sumHeights({5, 3, 6, 7, 2}, 2, 4) -> 6
        sumHeights({5, 3, 6, 7, 2}, 0, 1) -> 2
        sumHeights({5, 3, 6, 7, 2}, 0, 4) -> 11
        '''
        def sumHeights(heights, start, end):
            return sum([abs(heights[i] - heights[i+1]) for i in range(start, end)])

 

        '''
        (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
        along a walking trail. Given start/end indexes into the array, return the sum of the changes 
        for a walk beginning at the start index and ending at the end index, however increases in height 
        count double. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum 
        of 1*2 + 5 = 7. The start end end index will both be valid indexes into the array with start <= end. 

        sumHeights2({5, 3, 6, 7, 2}, 2, 4) -> 7
        sumHeights2({5, 3, 6, 7, 2}, 0, 1) -> 2
        sumHeights2({5, 3, 6, 7, 2}, 0, 4) -> 15
        '''
        def sumHeights2(heights, start, end):
            sum = 0
            for i in range(start, end):
                if (heights[i + 1] > heights[i]):
                    sum += 2 * (heights[i + 1] - heights[i])
                else:
                    sum += heights[i] - heights[i + 1]
            return sum


        '''
        (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
        along a walking trail. Given start/end indexes into the array, return the number of "big" steps 
        for a walk starting at the start index and ending at the end index. We'll say that step is big 
        if it is 5 or more up or down. The start end end index will both be valid indexes into the array 
        with start <= end. 

        bigHeights({5, 3, 6, 7, 2}, 2, 4) -> 1
        bigHeights({5, 3, 6, 7, 2}, 0, 1) -> 0
        bigHeights({5, 3, 6, 7, 2}, 0, 4) -> 1
        '''
        def bigHeights(heights, start, end):
            count = 0
            for i in range(start, end):
                if abs(heights[i + 1] - heights[i]) >= 5:
                    count += 1
            return count



        '''
        We have data for two users, A and B, each with a String name and an id. The goal is to order 
        the users such as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they 
        are the same. Order first by the string names, and then by the id numbers if the names are the same. 
        
        userCompare("bb", 1, "zz", 2) -> -1
        userCompare("bb", 1, "aa", 2) -> 1
        userCompare("bb", 1, "bb", 1) -> 0
        '''
        def userCompare(aName, aId, bName, bId):
            if aName < bName:
                return -1
            elif aName > bName:
                return 1
            elif aId < bId:
                return -1
            elif  aId > bId:
                return 1
            else:
                return 0



        '''
        Start with two arrays of strings, A and B, each with its elements in alphabetical order and 
        without duplicates. Return a new array containing the first N elements from the two arrays. 
        The result array should be in alphabetical order and without duplicates. A and B will both 
        have a length which is N or more. The best "linear" solution makes a single pass over A and B, 
        taking advantage of the fact that they are in alphabetical order, copying elements directly 
        to the new array. 

        mergeTwo({"a", "c", "z"}, {"b", "f", "z"}, 3) -> {"a", "b", "c"}
        mergeTwo({"a", "c", "z"}, {"c", "f", "z"}, 3) -> {"a", "c", "f"}
        mergeTwo({"f", "g", "z"}, {"c", "f", "g"}, 3) -> {"c", "f", "g"}
        '''
        def mergeTwo(a, b, n):
            result = [''] * n;
            apos = 0;
            bpos = 0;
            for i in range(n):
                while(apos < len(a) and i > 0 and a[apos] <= result[i-1]):
                    apos += 1
                while (bpos < len(b) and i > 0 and b[bpos] <= result[i-1]):
                    bpos += 1
                if (a[apos] <= b[bpos]):
                    result[i] = a[apos]
                    apos += 1
                else:
                    result[i] = b[bpos]
                    bpos += 1
            return result



        '''
        Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. 
        Return the count of the number of strings which appear in both arrays. The best "linear" solution 
        makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical 
        order. 

        commonTwo({"a", "c", "c", "x"}, {"b", "c", "d", "x"}) -> 2
        commonTwo({"a", "c", "x"}, {"a", "b", "c", "x", "z"}) -> 3
        commonTwo({"a", "b", "c"}, {"a", "b", "c"}) -> 3
        '''
        def commonTwo(a, b):
            count = 0
            apos = 0
            bpos = 0
            while (apos < len(a) and bpos < len(b)):
                while (apos > 0 and a[apos - 1] == a[apos]):
                    apos += 1
                while (bpos > 0 and b[bpos - 1] == b[bpos]):
                    bpos += 1
                if a[apos] < b[bpos]:
                    apos += 1
                elif a[apos] > b[bpos]:
                     bpos += 1
                else:
                    count += 1
                    apos += 1
                    bpos += 1
            return count




        print("scoresIncreasing")
        print(scoresIncreasing([ 1, 3, 4 ]) == True)
        print(scoresIncreasing([ 1, 3, 2 ]) == False)
        print(scoresIncreasing([ 1, 1, 4 ]) == True)

        print("scoresIncreasing2")
        print(scoresIncreasing2([ 1, 3, 4 ]) == True)
        print(scoresIncreasing2([ 1, 3, 2 ]) == False)
        print(scoresIncreasing2([ 1, 1, 4 ]) == True)

        print("scores100")
        print(scores100([ 1, 100, 100 ]) == True)
        print(scores100([ 1, 100, 99, 100 ]) == False)
        print(scores100([ 100, 1, 100, 100 ]) == True)

        print("scores1002")
        print(scores1002([ 1, 100, 100 ]) == True)
        print(scores1002([ 1, 100, 99, 100 ]) == False)
        print(scores1002([ 100, 1, 100, 100 ]) == True)

        print("scoresClump")
        print(scoresClump([ 3, 4, 5 ]) == True)
        print(scoresClump([ 3, 4, 6 ]) == False)
        print(scoresClump([ 1, 3, 5, 5 ]) == True)

        print("scoresClump2")
        print(scoresClump2([ 3, 4, 5 ]) == True)
        print(scoresClump2([ 3, 4, 6 ]) == False)
        print(scoresClump2([ 1, 3, 5, 5 ]) == True)

        print("scoresAverage")
        print(scoresAverage([ 2, 2, 4, 4 ]) == 4)
        print(scoresAverage([ 4, 4, 4, 2, 2, 2 ]) == 4)
        print(scoresAverage([ 3, 4, 5, 1, 2, 3 ]) == 4)

        print("wordsCount")
        print(wordsCount(["a", "bb", "b", "ccc" ], 1) == 2)
        print(wordsCount(["a", "bb", "b", "ccc" ], 3) == 1)
        print(wordsCount(["a", "bb", "b", "ccc" ], 4) == 0)

        print("wordsFront")
        print(wordsFront(["a", "b", "c", "d" ], 1) == ["a" ])
        print(wordsFront(["a", "b", "c", "d" ], 2) == ["a", "b" ])
        print(wordsFront(["a", "b", "c", "d" ], 3) == ["a", "b", "c" ])

        print("wordsWithout")
        print(wordsWithout(["a", "bb", "b", "ccc" ], 1) == ["bb", "ccc" ])
        print(wordsWithout(["a", "bb", "b", "ccc" ], 3) == ["a", "bb", "b" ])
        print(wordsWithout(["a", "bb", "b", "ccc" ], 4) == ["a", "bb", "b", "ccc" ])

        print("wordsWithout2")
        print(wordsWithout2(["a", "bb", "b", "ccc" ], 1) == ["bb", "ccc" ])
        print(wordsWithout2(["a", "bb", "b", "ccc" ], 3) == ["a", "bb", "b" ])
        print(wordsWithout2(["a", "bb", "b", "ccc" ], 4) == ["a", "bb", "b", "ccc" ])

        print("hasOne")
        print(hasOne(10) == True)
        print(hasOne(22) == False)
        print(hasOne(220) == False)

        print("hasOne2")
        print(hasOne2(10) == True)
        print(hasOne2(22) == False)
        print(hasOne2(220) == False)
            
        print("dividesSelf")
        print(dividesSelf(128) == True)
        print(dividesSelf(12) == True)
        print(dividesSelf(120) == False)
            
        print("copyEvens")
        print(copyEvens([ 3, 2, 4, 5, 8 ], 2) == [ 2, 4 ])
        print(copyEvens([ 3, 2, 4, 5, 8 ], 3) == [ 2, 4, 8 ])
        print(copyEvens([ 6, 1, 2, 4, 5, 8 ], 3) == [ 6, 2, 4 ])

        print("copyEvens2")
        print(copyEvens2([ 3, 2, 4, 5, 8 ], 2) == [ 2, 4 ])
        print(copyEvens2([ 3, 2, 4, 5, 8 ], 3) == [ 2, 4, 8 ])
        print(copyEvens2([ 6, 1, 2, 4, 5, 8 ], 3) == [ 6, 2, 4 ])
    
        print("copyEndy")
        print(copyEndy([ 9, 11, 90, 22, 6 ], 2) == [ 9, 90 ])
        print(copyEndy([ 9, 11, 90, 22, 6 ], 3) == [ 9, 90, 6 ])
        print(copyEndy([ 12, 1, 1, 13, 0, 20 ], 2) == [ 1, 1 ])

        print("matchUp")
        print(matchUp(["aa", "bb", "cc" ], ["aaa", "xx", "bb" ]) == 1)
        print(matchUp(["aa", "bb", "cc" ], ["aaa", "b", "bb" ]) == 2)
        print(matchUp(["aa", "bb", "cc" ], ["", "", "ccc" ]) == 1)

        print("scoreUp")
        print(scoreUp(["a", "a", "b", "b" ], ["a", "c", "b", "c" ]) == 6)
        print(scoreUp(["a", "a", "b", "b" ], ["a", "a", "b", "c" ]) == 11)
        print(scoreUp(["a", "a", "b", "b" ], ["a", "a", "b", "b" ]) == 16)

        print("wordsWithout")
        print(wordsWithout(["a", "b", "c", "a" ], "a") == ["b", "c" ])
        print(wordsWithout(["a", "b", "c", "a" ], "b") == ["a", "c", "a" ])
        print(wordsWithout(["a", "b", "c", "a" ], "c") == ["a", "b", "a" ])

        print("scoresSpecial")
        print(scoresSpecial([ 12, 10, 4 ], [ 2, 20, 30 ]) == 40)
        print(scoresSpecial([ 20, 10, 4 ], [ 2, 20, 10 ]) == 40)
        print(scoresSpecial([ 12, 11, 4 ], [ 2, 20, 31 ]) == 20)
            
        print("sumHeights")
        print(sumHeights([ 5, 3, 6, 7, 2 ], 2, 4) == 6)
        print(sumHeights([ 5, 3, 6, 7, 2 ], 0, 1) == 2)
        print(sumHeights([ 5, 3, 6, 7, 2 ], 0, 4) == 11)

        print("sumHeights2")
        print(sumHeights2([ 5, 3, 6, 7, 2 ], 2, 4) == 7)
        print(sumHeights2([ 5, 3, 6, 7, 2 ], 0, 1) == 2)
        print(sumHeights2([ 5, 3, 6, 7, 2 ], 0, 4) == 15)
            
        print("bigHeights")
        print(bigHeights([ 5, 3, 6, 7, 2 ], 2, 4) == 1)
        print(bigHeights([ 5, 3, 6, 7, 2 ], 0, 1) == 0)
        print(bigHeights([ 5, 3, 6, 7, 2 ], 0, 4) == 1)

        print("userCompare")
        print(userCompare("bb", 1, "zz", 2) == -1)
        print(userCompare("bb", 1, "aa", 2) == 1)
        print(userCompare("bb", 1, "bb", 1) == 0)
            
        print("mergeTwo")
        print(mergeTwo(["a", "c", "z" ], ["b", "f", "z" ], 3) == ["a", "b", "c" ])
        print(mergeTwo(["a", "c", "z" ], ["c", "f", "z" ], 3) == ["a", "c", "f" ])
        print(mergeTwo(["f", "g", "z" ], ["c", "f", "g" ], 3) == ["c", "f", "g" ])

        print("commonTwo")
        print(commonTwo(["a", "c", "c", "x" ], ["b", "c", "d", "x" ]) == 2)
        print(commonTwo(["a", "c", "x" ], ["a", "b", "c", "x", "z" ]) == 3)
        print(commonTwo(["a", "b", "c" ], ["a", "b", "c" ]) == 3)
