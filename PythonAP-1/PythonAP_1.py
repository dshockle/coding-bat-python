import sys

class PythonAP_1(object):

        '''
        Given an array of scores, return True if each score is equal or greater than the one before. 
        The array will be length 2 or more. 

        scoresIncreasing({1, 3, 4}) -> True
        scoresIncreasing({1, 3, 2}) -> False
        scoresIncreasing({1, 1, 4}) -> True
        '''

        def scoresIncreasing(int[] scores):
        {
            for (i = 1; i < len(scores); i++):
                if (scores[i] < scores[i - 1]):
                    return False
            return True
        }


        '''
        Given an array of scores, return True if there are scores of 100 next to each other in the array. 
        The array length will be at least 2. 

        scores100({1, 100, 100}) -> True
        scores100({1, 100, 99, 100}) -> False
        scores100({100, 1, 100, 100}) -> True
        '''
        def scores100(int[] scores):
        {
            for (i = 1; i < len(scores); i++):
                if (scores[i] == 100 && scores[i - 1] == 100):
                    return True
            return False
        }


        '''
        Given a sorted array, return True if the array contains 3 adjacent scores 
        that differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}. 

        scoresClump({3, 4, 5}) -> True
        scoresClump({3, 4, 6}) -> False
        scoresClump({1, 3, 5, 5}) -> True
        '''
        def scoresClump(int[] scores):
        {
            for (i = 1; i < len(scores) - 1; i++):
                if (Math.Abs(scores[i - 1] - scores[i + 1]) <= 2):
                    return True
            return False
        }


        '''
        Given an array of scores, compute the average of the first half and the second half, and return 
        whichever is larger. We'll say that the second half begins at index length/2. The array length will 
        be at least 2. Normally you would compute averages with doubles, but here we use ints so the expected 
        results are exact. 

        scoresAverage({2, 2, 4, 4}) -> 4
        scoresAverage({4, 4, 4, 2, 2, 2}) -> 4
        scoresAverage({3, 4, 5, 1, 2, 3}) -> 4
        '''
        def scoresAverage(int[] scores):
        {
            leftCount = 0;
            rightCount = 0;
            leftSum = 0;
            rightSum = 0;

            for(i = 0; i < len(scores); i++):
            {
                if (i < len(scores) / 2):
                {
                    leftCount++;
                    leftSum += scores[i];
                }
                else:
                {
                    rightCount++;
                    rightSum += scores[i];
                }
            }

            return Math.Max(leftSum / leftCount, rightSum / rightCount)
        }


        '''
        Given an array of strings, return the count of the number of strings with the given length. 

        wordsCount({"a", "bb", "b", "ccc"}, 1) -> 2
        wordsCount({"a", "bb", "b", "ccc"}, 3) -> 1
        wordsCount({"a", "bb", "b", "ccc"}, 4) -> 0
        '''
        def wordsCount(string[] words, len):
        {
            count = 0;

            foreach (string word in words):
                if (word.Length == len):
                    count++;

            return count;
        }


        '''
        Given an array of strings, return a new array containing the first N strings. 
        N will be in the range 1..length.

        wordsFront({"a", "b", "c", "d"}, 1) -> {"a"}
        wordsFront({"a", "b", "c", "d"}, 2) -> {"a", "b"}
        wordsFront({"a", "b", "c", "d"}, 3) -> {"a", "b", "c"}
        '''
        def wordsFront(string[] words, n)
        {
            string[] result = new string[n];
            Array.Copy(words, result, n)
            return result;
        }


        '''
        Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the 
        given length are omitted. 

        wordsWithoutList({"a", "bb", "b", "ccc"}, 1) -> {"bb", "ccc"}
        wordsWithoutList({"a", "bb", "b", "ccc"}, 3) -> {"a", "bb", "b"}
        wordsWithoutList({"a", "bb", "b", "ccc"}, 4) -> {"a", "bb", "b", "ccc"}
        '''
        def List<string> wordsWithoutList(string[] words, len):
        {
            List<string> result = new List<string>()

            foreach (string word in words):
            {
                if (word.Length != len):
                    result.Add(word)
            }

            return result;
        }



        '''
        Given an n, return True if it contains a 1 digit. Use a loop.
        hasOne(10) -> True
        hasOne(22) -> False
        hasOne(220) -> False
        '''
        def hasOne(n):
        {
            num = Math.Abs(n)

            while (num > 0):
            {
                digit = num % 10;

                if (digit == 1):
                    return True

                num /= 10;
            }

            return False
        }

        '''
        We'll say that a positive divides itself if every digit in the number divides into the 
        number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. 
        We'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself. 

        dividesSelf(128) -> True
        dividesSelf(12) -> True
        dividesSelf(120) -> False
        '''
        def dividesSelf(n):
        {
            if (n == 0):
                return False

            num = Math.Abs(n)

            while (num > 0):
            {
                digit = n % 10;

                if (digit == 0):
                    return False
                elif (n % digit != 0):
                    return False

                num /= 10;
            }

            return True
        }

        '''
        Given an array of positive ints, return a new array of length "count" containing the first even 
        numbers from the original array. The original array will contain at least "count" even numbers. 

        copyEvens({3, 2, 4, 5, 8}, 2) -> {2, 4}
        copyEvens({3, 2, 4, 5, 8}, 3) -> {2, 4, 8}
        copyEvens({6, 1, 2, 4, 5, 8}, 3) -> {6, 2, 4}
        '''
        def[] copyEvens(int[] nums, count)
        {
            int[] result = new int[count];
            rpos = 0;
            npos = 0;

            while (rpos < count):
            {
                if (nums[npos] % 2 == 0):
                {
                    result[rpos] = nums[npos];
                    rpos++;
                }

                npos++;
            }

            return result;
        }


        '''
        We'll say that a positive n is "endy" if it is in the range 0..10 or 90..100 (inclusive). 
        Given an array of positive ints, return a new array of length "count" containing the first endy 
        numbers from the original array. 

        copyEndy({9, 11, 90, 22, 6}, 2) -> {9, 90}
        copyEndy({9, 11, 90, 22, 6}, 3) -> {9, 90, 6}
        copyEndy({12, 1, 1, 13, 0, 20}, 2) -> {1, 1}
        '''
        def[] copyEndy(int[] nums, count):
        {
            int[] result = new int[count];
            rpos = 0;
            npos = 0;

            while (rpos < count):
            {
                if ((nums[npos] >= 0  && nums[npos] <= 10) 
                 || (nums[npos] >= 90 && nums[npos] <= 100)):
                {
                    result[rpos] = nums[npos];
                    rpos++;
                }

                npos++;
            }

            return result;
        }


        '''
        Given 2 arrays that are the same length containing strings, compare the 1st string in one 
        array to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number 
        of times that the 2 strings are non-empty and start with the same char. The strings may be 
        any length, including 0. 

        matchUp({"aa", "bb", "cc"}, {"aaa", "xx", "bb"}) -> 1
        matchUp({"aa", "bb", "cc"}, {"aaa", "b", "bb"}) -> 2
        matchUp({"aa", "bb", "cc"}, {"", "", "ccc"}) -> 1
        '''
        def matchUp(string[] a, string[] b):
        {
            count = 0;
            len = Math.Min(a.Length, b.Length)

            for (i = 0; i < len; i++):
            {
                if (!string.IsNullOrEmpty(a[i]) && !string.IsNullOrEmpty(b[i])):
                    if (a[i][0] == b[i][0])
                        count++;
            }

            return count;
        }


        '''
        The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. 
        The "answers" array contains a student's answers, with "?" representing a question left blank. 
        The two arrays are not empty and are the same length. Return the score for this array of answers, 
        giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer. 

        scoreUp({"a", "a", "b", "b"}, {"a", "c", "b", "c"}) -> 6
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "c"}) -> 11
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "b"}) -> 16
        '''
        def scoreUp(string[] key, string[] answers):
        {
            score = 0;
            for (i = 0; i < Math.Min(key.Length, answers.Length) i++):
            {
                if (!string.IsNullOrEmpty(key[i]) && !string.IsNullOrEmpty(answers[i])):
                    if (key[i] == answers[i]):
                        score += 4;
                    elif (answers[i] != "?"):
                        score -= 1;
            }
            return score;
        }


        '''
        Given an array of strings, return a new array without the strings that are equal to the target 
        string.  

        wordsWithout({"a", "b", "c", "a"}, "a") -> {"b", "c"}
        wordsWithout({"a", "b", "c", "a"}, "b") -> {"a", "c", "a"}
        wordsWithout({"a", "b", "c", "a"}, "c") -> {"a", "b", "a"}
        '''
        def wordsWithout(string[] words, string target):
        {
            List<string> result = new List<string>()

            foreach (string word in words):
            {
                if (word != target):
                    result.Add(word)
            }

            return result.ToArray()
        }


        '''
        Given two arrays, A and B, of non-negative scores. A "special" score is one which is a 
        multiple of 10, such as 40 or 90. Return the sum of largest special score in A and the largest 
        special score in B. 

        scoresSpecial({12, 10, 4}, {2, 20, 30}) -> 40
        scoresSpecial({20, 10, 4}, {2, 20, 10}) -> 40
        scoresSpecial({12, 11, 4}, {2, 20, 31}) -> 20
        '''
        def scoresSpecial(int[] a, int[] b):
        {
            aMod10Max = 0;
            bMod10Max = 0;

            foreach (num in a):
                if (num % 10 == 0 && num > aMod10Max)
                    aMod10Max = num;

            foreach (num in b):
                if (num % 10 == 0 && num > bMod10Max)
                    bMod10Max = num;

            return aMod10Max + bMod10Max;
        }


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
        def sumHeights(int[] heights, start, end):
        {
            sum = 0;

            for (i = start; i < end; i++):
                sum += Math.Abs(heights[i] - heights[i + 1])

            return sum;
        }

 

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
        def sumHeights2(int[] heights, start, end):
        {
            sum = 0;
            for(i = start; i < end; i++):
            {
                if (heights[i + 1] > heights[i]):
                    sum += 2 * (heights[i + 1] - heights[i])
                else:
                    sum += heights[i] - heights[i + 1];
            }
            return sum;
        }

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
        def bigHeights(int[] heights, start, end)
        {
            count = 0;

            for (i = start; i < end; i++):
                if (Math.Abs(heights[i + 1] - heights[i]) >= 5):
                    count++;

            return count;

        }



        '''
        We have data for two users, A and B, each with a String name and an id. The goal is to order 
        the users such as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they 
        are the same. Order first by the string names, and then by the id numbers if the names are the same. 
        
        userCompare("bb", 1, "zz", 2) -> -1
        userCompare("bb", 1, "aa", 2) -> 1
        userCompare("bb", 1, "bb", 1) -> 0
        '''
        def userCompare(string aName, aId, string bName, bId):
        {
            if (aName.CompareTo(bName) < 0):
                return -1;
            elif (aName.CompareTo(bName) > 0):
                return 1;
            elif (aId.CompareTo(bId) < 0):
                return -1;
            elif (aId.CompareTo(bId) > 0):
                return 1;
            else:
                return 0;

        }

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
        def mergeTwo(string[] a, string[] b, n):
        {
            string[] result = new string[n];
            apos = 0;
            bpos = 0;
            for (i = 0; i < result.Length; i++):
            {
                while(apos < a.Length && i > 0 && a[apos].CompareTo(result[i-1]) <= 0):
                    apos++;

                while (bpos < b.Length && i > 0 && b[bpos].CompareTo(result[i-1]) <= 0):
                    bpos++;

                if (a[apos].CompareTo(b[bpos]) <= 0):
                    result[i] = a[apos++];
                else:
                    result[i] = b[bpos++];
            }
            return result;
        }


        '''
        Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. 
        Return the count of the number of strings which appear in both arrays. The best "linear" solution 
        makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical 
        order. 

        commonTwo({"a", "c", "c", "x"}, {"b", "c", "d", "x"}) -> 2
        commonTwo({"a", "c", "x"}, {"a", "b", "c", "x", "z"}) -> 3
        commonTwo({"a", "b", "c"}, {"a", "b", "c"}) -> 3
        '''
        def commonTwo(string[] a, string[] b)
        {
            count = 0;
            apos = 0;
            bpos = 0;

            while (apos < a.Length && bpos < b.Length):
            {
                while (apos > 0 && a[apos - 1] == a[apos]):
                    apos++;

                while (bpos > 0 && b[bpos - 1] == b[bpos]):
                    bpos++;

                if (a[apos].CompareTo(b[bpos]) < 0):
                    apos++;
                elif(a[apos].CompareTo(b[bpos]) > 0):
                     bpos++;
                else:
                {
                    count++;
                    apos++;
                    bpos++;
                }
            }

            return count;
        }



    print("scoresIncreasing")
    print(scoresIncreasing(new int[] { 1, 3, 4 }) == True)
    print(scoresIncreasing(new int[] { 1, 3, 2 }) == False)
    print(scoresIncreasing(new int[] { 1, 1, 4 }) == True)

    print("scores100")
    print(scores100(new int[] { 1, 100, 100 }) == True)
    print(scores100(new int[] { 1, 100, 99, 100 }) == False)
    print(scores100(new int[] { 100, 1, 100, 100 }) == True)

    print("scoresClump")
    print(scoresClump(new int[] { 3, 4, 5 }) == True)
    print(scoresClump(new int[] { 3, 4, 6 }) == False)
    print(scoresClump(new int[] { 1, 3, 5, 5 }) == True)

    print("scoresAverage")
    print(scoresAverage(new int[] { 2, 2, 4, 4 }) == 4)
    print(scoresAverage(new int[] { 4, 4, 4, 2, 2, 2 }) == 4)
    print(scoresAverage(new int[] { 3, 4, 5, 1, 2, 3 }) == 4)

    print("wordsCount")
    print(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 1) == 2)
    print(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 3) == 1)
    print(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 4) == 0)

    print("wordsFront")
    print(wordsFront(new string[] { "a", "b", "c", "d" }, 1).SequenceEqual(new string[] { "a" }))
    print(wordsFront(new string[] { "a", "b", "c", "d" }, 2).SequenceEqual(new string[] { "a", "b" }))
    print(wordsFront(new string[] { "a", "b", "c", "d" }, 3).SequenceEqual(new string[] { "a", "b", "c" }))

    print("wordsWithoutList")
    print(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 1).SequenceEqual(new string[] { "bb", "ccc" }))
    print(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 3).SequenceEqual(new string[] { "a", "bb", "b" }))
    print(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 4).SequenceEqual(new string[] { "a", "bb", "b", "ccc" }))

    print("wordsWithoutListLinq")
    print(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 1).SequenceEqual(new string[] { "bb", "ccc" }))
    print(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 3).SequenceEqual(new string[] { "a", "bb", "b" }))
    print(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 4).SequenceEqual(new string[] { "a", "bb", "b", "ccc" }))

    print("hasOne")
    print(hasOne(10) == True)
    print(hasOne(22) == False)
    print(hasOne(220) == False)
            
    print("dividesSelf")
    print(dividesSelf(128) == True)
    print(dividesSelf(12) == True)
    print(dividesSelf(120) == False)
            
    print("copyEvens")
    print(copyEvens(new int[] { 3, 2, 4, 5, 8 }, 2).SequenceEqual(new int[] { 2, 4 }))
    print(copyEvens(new int[] { 3, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 2, 4, 8 }))
    print(copyEvens(new int[] { 6, 1, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 6, 2, 4 }))
  
    print("copyEndy")
    print(copyEndy(new int[] { 9, 11, 90, 22, 6 }, 2).SequenceEqual(new int[] { 9, 90 }))
    print(copyEndy(new int[] { 9, 11, 90, 22, 6 }, 3).SequenceEqual(new int[] { 9, 90, 6 }))
    print(copyEndy(new int[] { 12, 1, 1, 13, 0, 20 }, 2).SequenceEqual(new int[] { 1, 1 }))

    print("matchUp")
    print(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "xx", "bb" }) == 1)
    print(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "b", "bb" }) == 2)
    print(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "", "", "ccc" }) == 1)

    print("scoreUp")
    print(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "c", "b", "c" }) == 6)
    print(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "c" }) == 11)
    print(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "b" }) == 16)

    print("wordsWithout")
    print(wordsWithout(new string[] { "a", "b", "c", "a" }, "a").SequenceEqual(new string[] { "b", "c" }))
    print(wordsWithout(new string[] { "a", "b", "c", "a" }, "b").SequenceEqual(new string[] { "a", "c", "a" }))
    print(wordsWithout(new string[] { "a", "b", "c", "a" }, "c").SequenceEqual(new string[] { "a", "b", "a" }))

    print("scoresSpecial")
    print(scoresSpecial(new int[] { 12, 10, 4 }, new int[] { 2, 20, 30 }) == 40)
    print(scoresSpecial(new int[] { 20, 10, 4 }, new int[] { 2, 20, 10 }) == 40)
    print(scoresSpecial(new int[] { 12, 11, 4 }, new int[] { 2, 20, 31 }) == 20)

    print("scoresSpecialLinq")
    print(scoresSpecialLinq(new int[] { 12, 10, 4 }, new int[] { 2, 20, 30 }) == 40)
    print(scoresSpecialLinq(new int[] { 20, 10, 4 }, new int[] { 2, 20, 10 }) == 40)
    print(scoresSpecialLinq(new int[] { 12, 11, 4 }, new int[] { 2, 20, 31 }) == 20)
            
    print("sumHeights")
    print(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 6)
    print(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 2)
    print(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 11)

    print("sumHeights2")
    print(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 7)
    print(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 2)
    print(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 15)
            
    print("bigHeights")
    print(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 1)
    print(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 0)
    print(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 1)

    print("userCompare")
    print(userCompare("bb", 1, "zz", 2) == -1)
    print(userCompare("bb", 1, "aa", 2) == 1)
    print(userCompare("bb", 1, "bb", 1) == 0)
            
    print("mergeTwo")
    print(mergeTwo(new string[] { "a", "c", "z" }, new string[] { "b", "f", "z" }, 3).SequenceEqual(new string[] { "a", "b", "c" }))
    print(mergeTwo(new string[] { "a", "c", "z" }, new string[] { "c", "f", "z" }, 3).SequenceEqual(new string[] { "a", "c", "f" }))
    print(mergeTwo(new string[] { "f", "g", "z" }, new string[] { "c", "f", "g" }, 3).SequenceEqual(new string[] { "c", "f", "g" }))

    print("commonTwo")
    print(commonTwo(new string[] { "a", "c", "c", "x" }, new string[] { "b", "c", "d", "x" }) == 2)
    print(commonTwo(new string[] { "a", "c", "x" }, new string[] { "a", "b", "c", "x", "z" }) == 3)
    print(commonTwo(new string[] { "a", "b", "c" }, new string[] { "a", "b", "c" }) == 3)
