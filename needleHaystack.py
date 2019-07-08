#!/usr/bin/env python3
#find a string in another string and return the index
#return -1 if the needle is not in the haystack

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) < 1:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
