import sys

class PythonAP_1(object):

            /*
        Given an array of scores, return true if each score is equal or greater than the one before. 
        The array will be length 2 or more. 

        scoresIncreasing({1, 3, 4}) ? true
        scoresIncreasing({1, 3, 2}) ? false
        scoresIncreasing({1, 1, 4}) ? true
        */

        public static bool scoresIncreasing(int[] scores)
        {
            for (int i = 1; i < scores.Length; i++)
                if (scores[i] < scores[i - 1])
                    return false;
            return true;
        }


        /*
        Given an array of scores, return true if each score is equal or greater than the one before.
        The array will be length 2 or more. Use Linq. Do not use loops.

        scoresIncreasingLinq({ 1, 3, 4}) ? true
        scoresIncreasingLinq({ 1, 3, 2}) ? false
        scoresIncreasingLinq({ 1, 1, 4}) ? true
        */
        public static bool scoresIncreasingLinq(int[] scores)
        {
            return !scores.Skip(1)
                          .Where((value, index) => value < scores[index])
                          .Any();

        }

        /*
        Given an array of scores, return true if there are scores of 100 next to each other in the array. 
        The array length will be at least 2. 

        scores100({1, 100, 100}) ? true
        scores100({1, 100, 99, 100}) ? false
        scores100({100, 1, 100, 100}) ? true
        */
        public static bool scores100(int[] scores)
        {
            for (int i = 1; i < scores.Length; i++)
                if (scores[i] == 100 && scores[i - 1] == 100)
                    return true;
            return false;
        }


        /*
            Given an array of scores, return true if there are scores of 100 next to each other in the array. 
            The array length will be at least 2. Use Linq. Do not use loops.

            scores100Linq({1, 100, 100}) ? true
            scores100Linq({1, 100, 99, 100}) ? false
            scores100Linq({100, 1, 100, 100}) ? true
        */
        public static bool scores100Linq(int[] scores)
        {
            return scores.Skip(1).Where((val, index) => val == 100 && scores[index] == 100).Any();
        }

        /*
        Given a sorted array, return true if the array contains 3 adjacent scores 
        that differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}. 

        scoresClump({3, 4, 5}) ? true
        scoresClump({3, 4, 6}) ? false
        scoresClump({1, 3, 5, 5}) ? true
        */
        public static bool scoresClump(int[] scores)
        {
            for (int i = 1; i < scores.Length - 1; i++)
                if (Math.Abs(scores[i - 1] - scores[i + 1]) <= 2)
                    return true;
            return false;
        }

        /*
        Given a sorted array, return true if the array contains 3 adjacent scores 
        that differ from each other by at most 2, such as with {3, 4, 5} or {3, 5, 5}. 
        Use Linq. Do not use loops.
        scoresClump({3, 4, 5}) ? true
        scoresClump({3, 4, 6}) ? false
        scoresClump({1, 3, 5, 5}) ? true
        */
        public static bool scoresClumpLinq(int[] scores)
        {
            return scores.Skip(2).Where((val, index) => Math.Abs(val - scores[index]) <= 2).Any();
        }

        /*
        Given an array of scores, compute the int average of the first half and the second half, and return 
        whichever is larger. We'll say that the second half begins at index length/2. The array length will 
        be at least 2. Normally you would compute averages with doubles, but here we use ints so the expected 
        results are exact. 

        scoresAverage({2, 2, 4, 4}) ? 4
        scoresAverage({4, 4, 4, 2, 2, 2}) ? 4
        scoresAverage({3, 4, 5, 1, 2, 3}) ? 4
        */
        public static int scoresAverage(int[] scores)
        {
            int leftCount = 0;
            int rightCount = 0;
            int leftSum = 0;
            int rightSum = 0;

            for(int i = 0; i < scores.Length; i++)
            {
                if (i < scores.Length / 2)
                {
                    leftCount++;
                    leftSum += scores[i];
                }
                else
                {
                    rightCount++;
                    rightSum += scores[i];
                }
            }

            return Math.Max(leftSum / leftCount, rightSum / rightCount);
        }

        /*
        Given an array of scores, compute the int average of the first half and the second half, and return 
        whichever is larger. We'll say that the second half begins at index length/2. The array length will 
        be at least 2. Normally you would compute averages with doubles, but here we use ints so the expected 
        results are exact. Use Linq. Do not use loops.

        scoresAverage({2, 2, 4, 4}) ? 4
        scoresAverage({4, 4, 4, 2, 2, 2}) ? 4
        scoresAverage({3, 4, 5, 1, 2, 3}) ? 4
        */
        public static int scoresAverageLinq(int[] scores)
        {
            return (int)Math.Max(scores.Take(scores.Length / 2).Average(),
                                 scores.Skip(scores.Length / 2).Average());
        }

        /*
        Given an array of strings, return the count of the number of strings with the given length. 

        wordsCount({"a", "bb", "b", "ccc"}, 1) ? 2
        wordsCount({"a", "bb", "b", "ccc"}, 3) ? 1
        wordsCount({"a", "bb", "b", "ccc"}, 4) ? 0
        */
        public static int wordsCount(string[] words, int len)
        {
            int count = 0;

            foreach (string word in words)
                if (word.Length == len)
                    count++;

            return count;
        }

        /*
        Given an array of strings, return the count of the number of strings with the given length. 
        Use Linq. Do not use loops.
        wordsCountLinq({"a", "bb", "b", "ccc"}, 1) ? 2
        wordsCountLinq({"a", "bb", "b", "ccc"}, 3) ? 1
        wordsCountLinq({"a", "bb", "b", "ccc"}, 4) ? 0
        */
        public static int wordsCountLinq(string[] words, int len)
        {
            return words.Where(word => word.Length == len).Count();
        }

        /*
        Given an array of strings, return a new array containing the first N strings. 
        N will be in the range 1..length.

        wordsFront({"a", "b", "c", "d"}, 1) ? {"a"}
        wordsFront({"a", "b", "c", "d"}, 2) ? {"a", "b"}
        wordsFront({"a", "b", "c", "d"}, 3) ? {"a", "b", "c"}
        */
        public static string[] wordsFront(string[] words, int n)
        {
            string[] result = new string[n];
            Array.Copy(words, result, n);
            return result;
        }

        /*
        Given an array of strings, return a new array containing the first N strings. 
        N will be in the range 1..length. Use Linq. Do not use loops.

        wordsFrontLinq({"a", "b", "c", "d"}, 1) ? {"a"}
        wordsFrontLinq({"a", "b", "c", "d"}, 2) ? {"a", "b"}
        wordsFrontLinq({"a", "b", "c", "d"}, 3) ? {"a", "b", "c"}
        */
        public static string[] wordsFrontLinq(string[] words, int n)
        {
            return words.Take(n).ToArray();
        }

        /*
        Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the 
        given length are omitted. 

        wordsWithoutList({"a", "bb", "b", "ccc"}, 1) ? {"bb", "ccc"}
        wordsWithoutList({"a", "bb", "b", "ccc"}, 3) ? {"a", "bb", "b"}
        wordsWithoutList({"a", "bb", "b", "ccc"}, 4) ? {"a", "bb", "b", "ccc"}
        */
        public static List<string> wordsWithoutList(string[] words, int len)
        {
            List<string> result = new List<string>();

            foreach (string word in words)
            {
                if (word.Length != len)
                    result.Add(word);
            }

            return result;
        }

        /*
        Given an array of strings, return a new List(e.g.an ArrayList) where all the strings of the
        given length are omitted. Use Linq. Do not use loops.

        wordsWithoutListLinq({ "a", "bb", "b", "ccc"}, 1) ? {"bb", "ccc"}
        wordsWithoutListLinq({ "a", "bb", "b", "ccc"}, 3) ? {"a", "bb", "b"}
        wordsWithoutListLinq({ "a", "bb", "b", "ccc"}, 4) ? {"a", "bb", "b", "ccc"}
        */
        public static List<string> wordsWithoutListLinq(string[] words, int len)
        {
            return words.Where(word => word.Length != len).ToList<string>();
        }

        /*
        Given an int n, return true if it contains a 1 digit. Use Linq. Do not use loops.
        hasOneLinq(10) ? true
        hasOneLinq(22) ? false
        hasOneLinq(220) ? false
        */
        public static bool hasOneLinq(int n)
        {
            return n.ToString().Contains("1");
        }

        /*
        Given an int n, return true if it contains a 1 digit. Use a loop.
        hasOne(10) ? true
        hasOne(22) ? false
        hasOne(220) ? false
        */
        public static bool hasOne(int n)
        {
            int num = Math.Abs(n);

            while (num > 0)
            {
                int digit = num % 10;

                if (digit == 1)
                    return true;

                num /= 10;
            }

            return false;
        }

        /*
        We'll say that a positive int divides itself if every digit in the number divides into the 
        number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. 
        We'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself. 

        dividesSelf(128) ? true
        dividesSelf(12) ? true
        dividesSelf(120) ? false
        */
        public static bool dividesSelf(int n)
        {
            if (n == 0)
                return false;

            int num = Math.Abs(n);

            while (num > 0)
            {
                int digit = n % 10;

                if (digit == 0)
                    return false;
                else if (n % digit != 0)
                    return false;

                num /= 10;
            }

            return true;
        }

        /*
        Given an array of positive ints, return a new array of length "count" containing the first even 
        numbers from the original array. The original array will contain at least "count" even numbers. 

        copyEvens({3, 2, 4, 5, 8}, 2) ? {2, 4}
        copyEvens({3, 2, 4, 5, 8}, 3) ? {2, 4, 8}
        copyEvens({6, 1, 2, 4, 5, 8}, 3) ? {6, 2, 4}
        */
        public static int[] copyEvens(int[] nums, int count)
        {
            int[] result = new int[count];
            int rpos = 0;
            int npos = 0;

            while (rpos < count)
            {
                if (nums[npos] % 2 == 0)
                {
                    result[rpos] = nums[npos];
                    rpos++;
                }

                npos++;
            }

            return result;
        }

        /*
        Given an array of positive ints, return a new array of length "count" containing the first even 
        numbers from the original array. The original array will contain at least "count" even numbers. 
        Use Linq. Do not use loops.
        copyEvens({3, 2, 4, 5, 8}, 2) ? {2, 4}
        copyEvens({3, 2, 4, 5, 8}, 3) ? {2, 4, 8}
        copyEvens({6, 1, 2, 4, 5, 8}, 3) ? {6, 2, 4}
        */
        public static int[] copyEvensLinq(int[] nums, int count)
        {
            return nums.Where(num => num % 2 == 0).Take(count).ToArray();
        }

        /*
        We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). 
        Given an array of positive ints, return a new array of length "count" containing the first endy 
        numbers from the original array. 

        copyEndy({9, 11, 90, 22, 6}, 2) ? {9, 90}
        copyEndy({9, 11, 90, 22, 6}, 3) ? {9, 90, 6}
        copyEndy({12, 1, 1, 13, 0, 20}, 2) ? {1, 1}
        */
        public static int[] copyEndy(int[] nums, int count)
        {
            int[] result = new int[count];
            int rpos = 0;
            int npos = 0;

            while (rpos < count)
            {
                if ((nums[npos] >= 0  && nums[npos] <= 10) 
                 || (nums[npos] >= 90 && nums[npos] <= 100))
                {
                    result[rpos] = nums[npos];
                    rpos++;
                }

                npos++;
            }

            return result;
        }

        /*
        We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). 
        Given an array of positive ints, return a new array of length "count" containing the first endy 
        numbers from the original array. Use Linq. Do not use loops.

        copyEndyLinq({9, 11, 90, 22, 6}, 2) ? {9, 90}
        copyEndyLinq({9, 11, 90, 22, 6}, 3) ? {9, 90, 6}
        copyEndyLinq({12, 1, 1, 13, 0, 20}, 2) ? {1, 1}
        */
        public static int[] copyEndyLinq(int[] nums, int count)
        {
            return nums
                .Where(num => (num >= 0 && num <= 10) || (num >= 90 && num <= 100))
                .Take(count).ToArray();
        }

        /*
        Given 2 arrays that are the same length containing strings, compare the 1st string in one 
        array to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number 
        of times that the 2 strings are non-empty and start with the same char. The strings may be 
        any length, including 0. 

        matchUp({"aa", "bb", "cc"}, {"aaa", "xx", "bb"}) ? 1
        matchUp({"aa", "bb", "cc"}, {"aaa", "b", "bb"}) ? 2
        matchUp({"aa", "bb", "cc"}, {"", "", "ccc"}) ? 1
        */
        public static int matchUp(string[] a, string[] b)
        {
            int count = 0;
            int len = Math.Min(a.Length, b.Length);

            for (int i = 0; i < len; i++)
            {
                if (!string.IsNullOrEmpty(a[i]) && !string.IsNullOrEmpty(b[i]))
                    if (a[i][0] == b[i][0])
                        count++;
            }

            return count;
        }

        /*
        Given 2 arrays that are the same length containing strings, compare the 1st string in one 
        array to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number 
        of times that the 2 strings are non-empty and start with the same char. The strings may be 
        any length, including 0. Use Linq. Do not use loops.

        matchUpLinq({"aa", "bb", "cc"}, {"aaa", "xx", "bb"}) ? 1
        matchUpLinq({"aa", "bb", "cc"}, {"aaa", "b", "bb"}) ? 2
        matchUpLinq({"aa", "bb", "cc"}, {"", "", "ccc"}) ? 1
        */
        public static int matchUpLinq(string[] a, string[] b)
        {
            var matches = a.Zip(b, (x, y) => !string.IsNullOrEmpty(x) 
                                          && !string.IsNullOrEmpty(y) 
                                          && x[0] == y[0]);

            return matches.Where(element => element == true).Count();
        }

        /*
        The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. 
        The "answers" array contains a student's answers, with "?" representing a question left blank. 
        The two arrays are not empty and are the same length. Return the score for this array of answers, 
        giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer. 

        scoreUp({"a", "a", "b", "b"}, {"a", "c", "b", "c"}) ? 6
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "c"}) ? 11
        scoreUp({"a", "a", "b", "b"}, {"a", "a", "b", "b"}) ? 16
        */
        public static int scoreUp(string[] key, string[] answers)
        {
            int score = 0;
            for (int i = 0; i < Math.Min(key.Length, answers.Length); i++)
            {
                if (!string.IsNullOrEmpty(key[i]) && !string.IsNullOrEmpty(answers[i]))
                    if (key[i] == answers[i])
                        score += 4;
                    else if (answers[i] != "?")
                        score -= 1;
            }
            return score;
        }

        /*
        The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. 
        The "answers" array contains a student's answers, with "?" representing a question left blank. 
        The two arrays are not empty and are the same length. Return the score for this array of answers, 
        giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer. 

        scoreUpLinq({"a", "a", "b", "b"}, {"a", "c", "b", "c"}) ? 6
        scoreUpLinq({"a", "a", "b", "b"}, {"a", "a", "b", "c"}) ? 11
        scoreUpLinq({"a", "a", "b", "b"}, {"a", "a", "b", "b"}) ? 16
        */
        public static int scoreUpLinq(string[] key, string[] answers)
        {
            const int pointsPerCorrect = 4;
            const int wrongPenalty = 1;
            const int blankPenalty = 0;

            var results = key.Zip(answers, (x, y) => x == y);
            int corrects = results.Where(element => element == true).Count();
            int blanks = answers.Where(x => x == "?").Count();
            int incorrects = answers.Length - corrects - blanks;

            return corrects * pointsPerCorrect - incorrects * wrongPenalty - blanks * blankPenalty;
        }

        /*
        Given an array of strings, return a new array without the strings that are equal to the target 
        string.  

        wordsWithout({"a", "b", "c", "a"}, "a") ? {"b", "c"}
        wordsWithout({"a", "b", "c", "a"}, "b") ? {"a", "c", "a"}
        wordsWithout({"a", "b", "c", "a"}, "c") ? {"a", "b", "a"}
        */
        public static string[] wordsWithout(string[] words, string target)
        {
            List<string> result = new List<string>();

            foreach (string word in words)
            {
                if (word != target)
                    result.Add(word);
            }

            return result.ToArray();
        }

        /*
        Given an array of strings, return a new array without the strings that are equal to the target 
        string. Use Linq. Do not use loops.

        wordsWithoutLinq({"a", "b", "c", "a"}, "a") ? {"b", "c"}
        wordsWithoutLinq({"a", "b", "c", "a"}, "b") ? {"a", "c", "a"}
        wordsWithoutLinq({"a", "b", "c", "a"}, "c") ? {"a", "b", "a"}
        */
        public static string[] wordsWithoutLinq(string[] words, string target)
        {
            return words.Where(word => word != target).ToArray();
        }

        /*
        Given two arrays, A and B, of non-negative int scores. A "special" score is one which is a 
        multiple of 10, such as 40 or 90. Return the sum of largest special score in A and the largest 
        special score in B. 

        scoresSpecial({12, 10, 4}, {2, 20, 30}) ? 40
        scoresSpecial({20, 10, 4}, {2, 20, 10}) ? 40
        scoresSpecial({12, 11, 4}, {2, 20, 31}) ? 20
        */
        public static int scoresSpecial(int[] a, int[] b)
        {
            int aMod10Max = 0;
            int bMod10Max = 0;

            foreach (int num in a)
                if (num % 10 == 0 && num > aMod10Max)
                    aMod10Max = num;

            foreach (int num in b)
                if (num % 10 == 0 && num > bMod10Max)
                    bMod10Max = num;

            return aMod10Max + bMod10Max;
        }

        /*
        Given two arrays, A and B, of non-negative int scores. A "special" score is one which is a 
        multiple of 10, such as 40 or 90. Return the sum of largest special score in A and the largest 
        special score in B. Use Linq. Do not use loops.

        scoresSpecialLinq({12, 10, 4}, {2, 20, 30}) ? 40
        scoresSpecialLinq({20, 10, 4}, {2, 20, 10}) ? 40
        scoresSpecialLinq({12, 11, 4}, {2, 20, 31}) ? 20
        */
        public static int scoresSpecialLinq(int[] a, int[] b)
        {
            int aMod10Max = a.Where(value => value % 10 == 0).DefaultIfEmpty(0).Max();
            int bMod10Max = b.Where(value => value % 10 == 0).DefaultIfEmpty(0).Max();
            return aMod10Max + bMod10Max;
        }

        /*
        We have an array of heights, representing the altitude along a walking trail. Given start/end 
        indexes into the array, return the sum of the changes for a walk beginning at the start index 
        and ending at the end index. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 
        yields a sum of 1 + 5 = 6. The start end end index will both be valid indexes into the array 
        with start <= end. 

        sumHeights({5, 3, 6, 7, 2}, 2, 4) ? 6
        sumHeights({5, 3, 6, 7, 2}, 0, 1) ? 2
        sumHeights({5, 3, 6, 7, 2}, 0, 4) ? 11
        */
        public static int sumHeights(int[] heights, int start, int end)
        {
            int sum = 0;

            for (int i = start; i < end; i++)
                sum += Math.Abs(heights[i] - heights[i + 1]);

            return sum;
        }

        /*
        We have an array of heights, representing the altitude along a walking trail. Given start/end 
        indexes into the array, return the sum of the changes for a walk beginning at the start index 
        and ending at the end index. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 
        yields a sum of 1 + 5 = 6. The start end end index will both be valid indexes into the array 
        with start <= end. Use Linq. Do not use loops.

        sumHeightsLinq({5, 3, 6, 7, 2}, 2, 4) ? 6
        sumHeightsLinq({5, 3, 6, 7, 2}, 0, 1) ? 2
        sumHeightsLinq({5, 3, 6, 7, 2}, 0, 4) ? 11
        */
        public static int sumHeightsLinq(int[] heights, int start, int end)
        {
            var steps = heights.Skip(start).Take(1 + end - start);

            return steps
                .Zip(steps
                .Skip(1), (x, y) => Math.Abs(y - x))
                .Sum();
        }

        /*
        (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
        along a walking trail. Given start/end indexes into the array, return the sum of the changes 
        for a walk beginning at the start index and ending at the end index, however increases in height 
        count double. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum 
        of 1*2 + 5 = 7. The start end end index will both be valid indexes into the array with start <= end. 

        sumHeights2({5, 3, 6, 7, 2}, 2, 4) ? 7
        sumHeights2({5, 3, 6, 7, 2}, 0, 1) ? 2
        sumHeights2({5, 3, 6, 7, 2}, 0, 4) ? 15
        */
        public static int sumHeights2(int[] heights, int start, int end)
        {
            int sum = 0;
            for(int i = start; i < end; i++)
            {
                if (heights[i + 1] > heights[i])
                    sum += 2 * (heights[i + 1] - heights[i]);
                else
                    sum += heights[i] - heights[i + 1];
            }
            return sum;
        }

        /*
        (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
        along a walking trail. Given start/end indexes into the array, return the number of "big" steps 
        for a walk starting at the start index and ending at the end index. We'll say that step is big 
        if it is 5 or more up or down. The start end end index will both be valid indexes into the array 
        with start <= end. 

        bigHeights({5, 3, 6, 7, 2}, 2, 4) ? 1
        bigHeights({5, 3, 6, 7, 2}, 0, 1) ? 0
        bigHeights({5, 3, 6, 7, 2}, 0, 4) ? 1
        */
        public static int bigHeights(int[] heights, int start, int end)
        {
            int count = 0;

            for (int i = start; i < end; i++)
                if (Math.Abs(heights[i + 1] - heights[i]) >= 5)
                    count++;

            return count;

        }

        /*
        (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
        along a walking trail. Given start/end indexes into the array, return the number of "big" steps 
        for a walk starting at the start index and ending at the end index. We'll say that step is big 
        if it is 5 or more up or down. The start end end index will both be valid indexes into the array 
        with start <= end. Use Linq. Do not use loops.

        bigHeightsLinq({5, 3, 6, 7, 2}, 2, 4) ? 1
        bigHeightsLinq({5, 3, 6, 7, 2}, 0, 1) ? 0
        bigHeightsLinq({5, 3, 6, 7, 2}, 0, 4) ? 1
        */
        public static int bigHeightsLinq(int[] heights, int start, int end)
        {
            var steps = heights.Skip(start).Take(1 + end - start);

            return steps
                .Zip(steps.Skip(1), (x, y) => Math.Abs(y - x))
                .Where(value => value >= 5).Count();
        }

        /*
        We have data for two users, A and B, each with a String name and an int id. The goal is to order 
        the users such as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they 
        are the same. Order first by the string names, and then by the id numbers if the names are the same. 
        
        userCompare("bb", 1, "zz", 2) ? -1
        userCompare("bb", 1, "aa", 2) ? 1
        userCompare("bb", 1, "bb", 1) ? 0
        */
        public static int userCompare(string aName, int aId, string bName, int bId)
        {
            if (aName.CompareTo(bName) < 0)
                return -1;
            else if (aName.CompareTo(bName) > 0)
                return 1;
            else if (aId.CompareTo(bId) < 0)
                return -1;
            else if (aId.CompareTo(bId) > 0)
                return 1;
            else
                return 0;

        }

        /*
        Start with two arrays of strings, A and B, each with its elements in alphabetical order and 
        without duplicates. Return a new array containing the first N elements from the two arrays. 
        The result array should be in alphabetical order and without duplicates. A and B will both 
        have a length which is N or more. The best "linear" solution makes a single pass over A and B, 
        taking advantage of the fact that they are in alphabetical order, copying elements directly 
        to the new array. 

        mergeTwo({"a", "c", "z"}, {"b", "f", "z"}, 3) ? {"a", "b", "c"}
        mergeTwo({"a", "c", "z"}, {"c", "f", "z"}, 3) ? {"a", "c", "f"}
        mergeTwo({"f", "g", "z"}, {"c", "f", "g"}, 3) ? {"c", "f", "g"}
        */
        public static string[] mergeTwo(string[] a, string[] b, int n)
        {
            string[] result = new string[n];
            int apos = 0;
            int bpos = 0;
            for (int i = 0; i < result.Length; i++)
            {
                while(apos < a.Length && i > 0 && a[apos].CompareTo(result[i-1]) <= 0)
                    apos++;

                while (bpos < b.Length && i > 0 && b[bpos].CompareTo(result[i-1]) <= 0)
                    bpos++;

                if (a[apos].CompareTo(b[bpos]) <= 0)
                    result[i] = a[apos++];
                else
                    result[i] = b[bpos++];
            }
            return result;
        }

        /*
        Start with two arrays of strings, A and B, each with its elements in alphabetical order and 
        without duplicates. Return a new array containing the first N elements from the two arrays. 
        The result array should be in alphabetical order and without duplicates. A and B will both 
        have a length which is N or more. Use Linq. Do not use loops.

        mergeTwoLinq({"a", "c", "z"}, {"b", "f", "z"}, 3) ? {"a", "b", "c"}
        mergeTwoLinq({"a", "c", "z"}, {"c", "f", "z"}, 3) ? {"a", "c", "f"}
        mergeTwoLinq({"f", "g", "z"}, {"c", "f", "g"}, 3) ? {"c", "f", "g"}
        */
        public static string[] mergeTwoLinq(string[] a, string[] b, int n)
        {
            return a.Concat(b).OrderBy(v => v).Distinct().Take(n).ToArray();
        }

        /*
        Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. 
        Return the count of the number of strings which appear in both arrays. The best "linear" solution 
        makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical 
        order. 

        commonTwo({"a", "c", "c", "x"}, {"b", "c", "d", "x"}) ? 2
        commonTwo({"a", "c", "x"}, {"a", "b", "c", "x", "z"}) ? 3
        commonTwo({"a", "b", "c"}, {"a", "b", "c"}) ? 3
        */
        public static int commonTwo(string[] a, string[] b)
        {
            int count = 0;
            int apos = 0;
            int bpos = 0;

            while (apos < a.Length && bpos < b.Length)
            {
                while (apos > 0 && a[apos - 1] == a[apos])
                    apos++;

                while (bpos > 0 && b[bpos - 1] == b[bpos])
                    bpos++;

                if (a[apos].CompareTo(b[bpos]) < 0)
                    apos++;
                else if(a[apos].CompareTo(b[bpos]) > 0)
                     bpos++;
                else
                {
                    count++;
                    apos++;
                    bpos++;
                }
            }

            return count;
        }

        /*
        Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. 
        Return the count of the number of strings which appear in both arrays. The best "linear" solution 
        makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical 
        order. Use Linq. Do not use loops.

        commonTwoLinq({"a", "c", "c", "x"}, {"b", "c", "d", "x"}) ? 2
        commonTwoLinq({"a", "c", "x"}, {"a", "b", "c", "x", "z"}) ? 3
        commonTwoLinq({"a", "b", "c"}, {"a", "b", "c"}) ? 3
        */
        public static int commonTwoLinq(string[] a, string[] b)
        {
            return a.Intersect(b).Count();
        }


            Console.WriteLine("scoresIncreasing");
            Console.WriteLine(scoresIncreasing(new int[] { 1, 3, 4 }) == true);
            Console.WriteLine(scoresIncreasing(new int[] { 1, 3, 2 }) == false);
            Console.WriteLine(scoresIncreasing(new int[] { 1, 1, 4 }) == true);

            Console.WriteLine("scoresIncreasingLinq");
            Console.WriteLine(scoresIncreasingLinq(new int[] { 1, 3, 4 }) == true);
            Console.WriteLine(scoresIncreasingLinq(new int[] { 1, 3, 2 }) == false);
            Console.WriteLine(scoresIncreasingLinq(new int[] { 1, 1, 4 }) == true);

            Console.WriteLine("scores100");
            Console.WriteLine(scores100(new int[] { 1, 100, 100 }) == true);
            Console.WriteLine(scores100(new int[] { 1, 100, 99, 100 }) == false);
            Console.WriteLine(scores100(new int[] { 100, 1, 100, 100 }) == true);

            Console.WriteLine("scores100Linq");
            Console.WriteLine(scores100Linq(new int[] { 1, 100, 100 }) == true);
            Console.WriteLine(scores100Linq(new int[] { 1, 100, 99, 100 }) == false);
            Console.WriteLine(scores100Linq(new int[] { 100, 1, 100, 100 }) == true);

            Console.WriteLine("scoresClump");
            Console.WriteLine(scoresClump(new int[] { 3, 4, 5 }) == true);
            Console.WriteLine(scoresClump(new int[] { 3, 4, 6 }) == false);
            Console.WriteLine(scoresClump(new int[] { 1, 3, 5, 5 }) == true);

            Console.WriteLine("scoresClumpLinq");
            Console.WriteLine(scoresClumpLinq(new int[] { 3, 4, 5 }) == true);
            Console.WriteLine(scoresClumpLinq(new int[] { 3, 4, 6 }) == false);
            Console.WriteLine(scoresClumpLinq(new int[] { 1, 3, 5, 5 }) == true);
            
            Console.WriteLine("scoresAverage");
            Console.WriteLine(scoresAverage(new int[] { 2, 2, 4, 4 }) == 4);
            Console.WriteLine(scoresAverage(new int[] { 4, 4, 4, 2, 2, 2 }) == 4);
            Console.WriteLine(scoresAverage(new int[] { 3, 4, 5, 1, 2, 3 }) == 4);

            Console.WriteLine("scoresAverageLinq");
            Console.WriteLine(scoresAverageLinq(new int[] { 2, 2, 4, 4 }) == 4);
            Console.WriteLine(scoresAverageLinq(new int[] { 4, 4, 4, 2, 2, 2 }) == 4);
            Console.WriteLine(scoresAverageLinq(new int[] { 3, 4, 5, 1, 2, 3 }) == 4);

            Console.WriteLine("wordsCount");
            Console.WriteLine(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 1) == 2);
            Console.WriteLine(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 3) == 1);
            Console.WriteLine(wordsCount(new string[] { "a", "bb", "b", "ccc" }, 4) == 0);

            Console.WriteLine("wordsCountLinq");
            Console.WriteLine(wordsCountLinq(new string[] { "a", "bb", "b", "ccc" }, 1) == 2);
            Console.WriteLine(wordsCountLinq(new string[] { "a", "bb", "b", "ccc" }, 3) == 1);
            Console.WriteLine(wordsCountLinq(new string[] { "a", "bb", "b", "ccc" }, 4) == 0);
            
            Console.WriteLine("wordsFront");
            Console.WriteLine(wordsFront(new string[] { "a", "b", "c", "d" }, 1).SequenceEqual(new string[] { "a" }));
            Console.WriteLine(wordsFront(new string[] { "a", "b", "c", "d" }, 2).SequenceEqual(new string[] { "a", "b" }));
            Console.WriteLine(wordsFront(new string[] { "a", "b", "c", "d" }, 3).SequenceEqual(new string[] { "a", "b", "c" }));

            Console.WriteLine("wordsFrontLinq");
            Console.WriteLine(wordsFrontLinq(new string[] { "a", "b", "c", "d" }, 1).SequenceEqual(new string[] { "a" }));
            Console.WriteLine(wordsFrontLinq(new string[] { "a", "b", "c", "d" }, 2).SequenceEqual(new string[] { "a", "b" }));
            Console.WriteLine(wordsFrontLinq(new string[] { "a", "b", "c", "d" }, 3).SequenceEqual(new string[] { "a", "b", "c" }));
            
            Console.WriteLine("wordsWithoutList");
            Console.WriteLine(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 1).SequenceEqual(new string[] { "bb", "ccc" }));
            Console.WriteLine(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 3).SequenceEqual(new string[] { "a", "bb", "b" }));
            Console.WriteLine(wordsWithoutList(new string[] { "a", "bb", "b", "ccc" }, 4).SequenceEqual(new string[] { "a", "bb", "b", "ccc" }));

            Console.WriteLine("wordsWithoutListLinq");
            Console.WriteLine(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 1).SequenceEqual(new string[] { "bb", "ccc" }));
            Console.WriteLine(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 3).SequenceEqual(new string[] { "a", "bb", "b" }));
            Console.WriteLine(wordsWithoutListLinq(new string[] { "a", "bb", "b", "ccc" }, 4).SequenceEqual(new string[] { "a", "bb", "b", "ccc" }));
            
            Console.WriteLine("hasOneLinq");
            Console.WriteLine(hasOneLinq(10) == true);
            Console.WriteLine(hasOneLinq(22) == false);
            Console.WriteLine(hasOneLinq(220) == false);

            Console.WriteLine("hasOne");
            Console.WriteLine(hasOne(10) == true);
            Console.WriteLine(hasOne(22) == false);
            Console.WriteLine(hasOne(220) == false);
            
            Console.WriteLine("dividesSelf");
            Console.WriteLine(dividesSelf(128) == true);
            Console.WriteLine(dividesSelf(12) == true);
            Console.WriteLine(dividesSelf(120) == false);
            
            Console.WriteLine("copyEvens");
            Console.WriteLine(copyEvens(new int[] { 3, 2, 4, 5, 8 }, 2).SequenceEqual(new int[] { 2, 4 }));
            Console.WriteLine(copyEvens(new int[] { 3, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 2, 4, 8 }));
            Console.WriteLine(copyEvens(new int[] { 6, 1, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 6, 2, 4 }));

            Console.WriteLine("copyEvensLinq");
            Console.WriteLine(copyEvensLinq(new int[] { 3, 2, 4, 5, 8 }, 2).SequenceEqual(new int[] { 2, 4 }));
            Console.WriteLine(copyEvensLinq(new int[] { 3, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 2, 4, 8 }));
            Console.WriteLine(copyEvensLinq(new int[] { 6, 1, 2, 4, 5, 8 }, 3).SequenceEqual(new int[] { 6, 2, 4 }));
            
            Console.WriteLine("copyEndy");
            Console.WriteLine(copyEndy(new int[] { 9, 11, 90, 22, 6 }, 2).SequenceEqual(new int[] { 9, 90 }));
            Console.WriteLine(copyEndy(new int[] { 9, 11, 90, 22, 6 }, 3).SequenceEqual(new int[] { 9, 90, 6 }));
            Console.WriteLine(copyEndy(new int[] { 12, 1, 1, 13, 0, 20 }, 2).SequenceEqual(new int[] { 1, 1 }));

            Console.WriteLine("copyEndyLinq");
            Console.WriteLine(copyEndyLinq(new int[] { 9, 11, 90, 22, 6 }, 2).SequenceEqual(new int[] { 9, 90 }));
            Console.WriteLine(copyEndyLinq(new int[] { 9, 11, 90, 22, 6 }, 3).SequenceEqual(new int[] { 9, 90, 6 }));
            Console.WriteLine(copyEndyLinq(new int[] { 12, 1, 1, 13, 0, 20 }, 2).SequenceEqual(new int[] { 1, 1 }));
            
            Console.WriteLine("matchUp");
            Console.WriteLine(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "xx", "bb" }) == 1);
            Console.WriteLine(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "b", "bb" }) == 2);
            Console.WriteLine(matchUp(new string[] { "aa", "bb", "cc" }, new string[] { "", "", "ccc" }) == 1);

            Console.WriteLine("matchUpLinq");
            Console.WriteLine(matchUpLinq(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "xx", "bb" }) == 1);
            Console.WriteLine(matchUpLinq(new string[] { "aa", "bb", "cc" }, new string[] { "aaa", "b", "bb" }) == 2);
            Console.WriteLine(matchUpLinq(new string[] { "aa", "bb", "cc" }, new string[] { "", "", "ccc" }) == 1);
            
            Console.WriteLine("scoreUp");
            Console.WriteLine(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "c", "b", "c" }) == 6);
            Console.WriteLine(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "c" }) == 11);
            Console.WriteLine(scoreUp(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "b" }) == 16);

            Console.WriteLine("scoreUpLinq");
            Console.WriteLine(scoreUpLinq(new string[] { "a", "a", "b", "b" }, new string[] { "a", "c", "b", "c" }) == 6);
            Console.WriteLine(scoreUpLinq(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "c" }) == 11);
            Console.WriteLine(scoreUpLinq(new string[] { "a", "a", "b", "b" }, new string[] { "a", "a", "b", "b" }) == 16);
            
            Console.WriteLine("wordsWithout");
            Console.WriteLine(wordsWithout(new string[] { "a", "b", "c", "a" }, "a").SequenceEqual(new string[] { "b", "c" }));
            Console.WriteLine(wordsWithout(new string[] { "a", "b", "c", "a" }, "b").SequenceEqual(new string[] { "a", "c", "a" }));
            Console.WriteLine(wordsWithout(new string[] { "a", "b", "c", "a" }, "c").SequenceEqual(new string[] { "a", "b", "a" }));

            Console.WriteLine("wordsWithoutLinq");
            Console.WriteLine(wordsWithoutLinq(new string[] { "a", "b", "c", "a" }, "a").SequenceEqual(new string[] { "b", "c" }));
            Console.WriteLine(wordsWithoutLinq(new string[] { "a", "b", "c", "a" }, "b").SequenceEqual(new string[] { "a", "c", "a" }));
            Console.WriteLine(wordsWithoutLinq(new string[] { "a", "b", "c", "a" }, "c").SequenceEqual(new string[] { "a", "b", "a" }));
            
            Console.WriteLine("scoresSpecial");
            Console.WriteLine(scoresSpecial(new int[] { 12, 10, 4 }, new int[] { 2, 20, 30 }) == 40);
            Console.WriteLine(scoresSpecial(new int[] { 20, 10, 4 }, new int[] { 2, 20, 10 }) == 40);
            Console.WriteLine(scoresSpecial(new int[] { 12, 11, 4 }, new int[] { 2, 20, 31 }) == 20);

            Console.WriteLine("scoresSpecialLinq");
            Console.WriteLine(scoresSpecialLinq(new int[] { 12, 10, 4 }, new int[] { 2, 20, 30 }) == 40);
            Console.WriteLine(scoresSpecialLinq(new int[] { 20, 10, 4 }, new int[] { 2, 20, 10 }) == 40);
            Console.WriteLine(scoresSpecialLinq(new int[] { 12, 11, 4 }, new int[] { 2, 20, 31 }) == 20);
            
            Console.WriteLine("sumHeights");
            Console.WriteLine(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 6);
            Console.WriteLine(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 2);
            Console.WriteLine(sumHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 11);

            Console.WriteLine("sumHeightsLinq");
            Console.WriteLine(sumHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 6);
            Console.WriteLine(sumHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 2);
            Console.WriteLine(sumHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 11);

            Console.WriteLine("sumHeights2");
            Console.WriteLine(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 7);
            Console.WriteLine(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 2);
            Console.WriteLine(sumHeights2(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 15);
            
            Console.WriteLine("bigHeights");
            Console.WriteLine(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 1);
            Console.WriteLine(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 0);
            Console.WriteLine(bigHeights(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 1);

            Console.WriteLine("bigHeightsLinq");
            Console.WriteLine(bigHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 2, 4) == 1);
            Console.WriteLine(bigHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 0, 1) == 0);
            Console.WriteLine(bigHeightsLinq(new int[] { 5, 3, 6, 7, 2 }, 0, 4) == 1);
            
            Console.WriteLine("userCompare");
            Console.WriteLine(userCompare("bb", 1, "zz", 2) == -1);
            Console.WriteLine(userCompare("bb", 1, "aa", 2) == 1);
            Console.WriteLine(userCompare("bb", 1, "bb", 1) == 0);
            
            Console.WriteLine("mergeTwo");
            Console.WriteLine(mergeTwo(new string[] { "a", "c", "z" }, new string[] { "b", "f", "z" }, 3).SequenceEqual(new string[] { "a", "b", "c" }));
            Console.WriteLine(mergeTwo(new string[] { "a", "c", "z" }, new string[] { "c", "f", "z" }, 3).SequenceEqual(new string[] { "a", "c", "f" }));
            Console.WriteLine(mergeTwo(new string[] { "f", "g", "z" }, new string[] { "c", "f", "g" }, 3).SequenceEqual(new string[] { "c", "f", "g" }));

            Console.WriteLine("mergeTwoLinq");
            Console.WriteLine(mergeTwoLinq(new string[] { "a", "c", "z" }, new string[] { "b", "f", "z" }, 3).SequenceEqual(new string[] { "a", "b", "c" }));
            Console.WriteLine(mergeTwoLinq(new string[] { "a", "c", "z" }, new string[] { "c", "f", "z" }, 3).SequenceEqual(new string[] { "a", "c", "f" }));
            Console.WriteLine(mergeTwoLinq(new string[] { "f", "g", "z" }, new string[] { "c", "f", "g" }, 3).SequenceEqual(new string[] { "c", "f", "g" }));
            
            Console.WriteLine("commonTwo");
            Console.WriteLine(commonTwo(new string[] { "a", "c", "c", "x" }, new string[] { "b", "c", "d", "x" }) == 2);
            Console.WriteLine(commonTwo(new string[] { "a", "c", "x" }, new string[] { "a", "b", "c", "x", "z" }) == 3);
            Console.WriteLine(commonTwo(new string[] { "a", "b", "c" }, new string[] { "a", "b", "c" }) == 3);

            Console.WriteLine("commonTwoLinq");
            Console.WriteLine(commonTwoLinq(new string[] { "a", "c", "c", "x" }, new string[] { "b", "c", "d", "x" }) == 2);
            Console.WriteLine(commonTwoLinq(new string[] { "a", "c", "x" }, new string[] { "a", "b", "c", "x", "z" }) == 3);
            Console.WriteLine(commonTwoLinq(new string[] { "a", "b", "c" }, new string[] { "a", "b", "c" }) == 3);
