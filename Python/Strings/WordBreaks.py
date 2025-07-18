"""
Given a string s and a dictionary dict[] of valid words, you need to return all possible ways to break
the string s into sentence such that each word in the sentence is a valid dictionary word.
You are allowed to use a valid word multiple times in the sentence.

Input: s = "likegfg", dict[] = ["lik", "like", "egfg", "gfg"]
Output: 
"lik egfg"
"like gfg"

Input: s = "geeksforgeeks", dict[] = ["for", "geeks"]
Output: "geeks for geeks"
"""

import sys

# idea: we iterate through str say with index i, searching for a valid word in str[start:i+1]
# if we encounter a coincide, we recursively search for all possible decompositions of the remaining string
# and append "word" before each one of them. Then, we continue looping through the string, in case we have
# valid words contained in others (e.g lik and like)
# another way would be: search each word coincide in string, and save it to a hashmap where key is the
# starting index of the word, and the value is a list of the words starting and that index
# this can be done with two nested loops or using only one loop and an auxiliar structure of starting indexes
# then, we have to form all possible decompositions that start in hashmap's key 0: we take the word_1 in key 0,
# and then search for a word in key (0+len(word_1)), and so on. It's a valid decomposition if we end the chain
# in a word_k such that (key_k + len(word_k) == len(str))
# --- in both cases, we should implement dp (memoization or tabulation) because we have overlapping subproblems
# and end up doing recomputations ---
def wordBreaks(str, dict, start = 0):
    res = []

    l = len(str)
    for i in range(start, l):
        # we always consider the substring starting from "start", expanding it one char at once
        substr = str[start:i+1]
        if (substr in dict):
            # base case, we reached the last char of str, there's no recursion, just append the word
            if i == l-1:
                res.append(substr)
            else:
                # recursive case, we set start to i+1 and recursively search to decompose the rest of str
                # if that's not possible, rec will be [] and there won't be any valid decompositions
                rec = wordBreaks(str, dict, i+1)
                for j, r in enumerate(rec):
                    rec[j] = substr + " " + r
                res.extend(rec)

    return res

def main():
    string = sys.argv[1]
    dict = set()
    [dict.add(word) for word in sys.argv[2:]]

    res = wordBreaks(string, dict)

    print(res)
    return res

if __name__ == "__main__":
    main()