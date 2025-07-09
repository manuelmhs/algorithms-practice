"""
Given two strings str1 and str2 of the same length. Find the longest prefix of str1 which is common in str2.
Return the length of the longest common prefix.
"""

import sys

# Time complexity: O(n^2), Space complexity: O(1)
# see KMP algorithm to improve time complexity to O(n)
def LongestCommonPrefix(str1, str2):
    # we loop through the second array searching for the first char of str1
    # when we find it, say at idx2 = k, we start reading str1 and str2 from that point while the characters are equal
    # if we encounter different chars, we consider the length of the substring we read as a possible maximum
    # then, we continue the algorithm from idx2 = k+1 (in case a prefix is partially included in a previous one)
    # we end the algorithm if we run out of chars in any of the 2 strs
    maxPrefixSize = 0
    
    idx1 = idx2 = 0
    lastStart = -1
    while (idx1 < len(str1) and idx2 < len(str2)):
        if str1[idx1] == str2[idx2]:
            if idx1 == 0:
                lastStart = idx2

            idx1 += 1
        else:
            if idx1 != 0:
                maxPrefixSize = max(maxPrefixSize, idx1)

                idx1 = 0
                idx2 = lastStart

        idx2 += 1

    return max(maxPrefixSize, idx1)

def main():
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    m = LongestCommonPrefix(str1, str2)

    print(m)
    return m

if __name__ == "__main__":
    main()