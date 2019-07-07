#!/usr/bin/env python3
# convert roman numberals to integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return_int = 0
        i = 0
        while i < len(s):
            if s[i] == 'C' and i + 1 < len(s): 
                    if s[i+1] =='M':
                        return_int = return_int + 900
                        i = i + 2
                        print('here')
                        continue
                    elif s[i+1] == 'D':
                        return_int = return_int + 400
                        i = i + 2
                        continue
            if s[i] == 'X' and i + 1 < len(s): 
                    if s[i+1] =='C':
                        return_int = return_int + 90
                        i = i + 2
                        continue
                    elif s[i+1] == 'L':
                        return_int = return_int + 40
                        i = i + 2
                        continue
            if s[i] == 'I' and i + 1 < len(s): 
                    if s[i+1] == 'X':
                        return_int = return_int + 9
                        i = i + 2
                        break
                    elif s[i+1] == 'V':
                        i = i + 2
                        return_int = return_int + 4
                        break
            if s[i] == 'M':
                    print('there')
                    return_int = return_int + 1000
                    i = i + 1
                    continue
            if s[i] == 'D':
                    return_int = return_int + 500
                    i = i + 1
                    continue
            if s[i] == 'C':
                    return_int = return_int + 100
                    i = i + 1
                    continue
            if s[i] == 'L':
                    return_int = return_int + 50
                    i = i + 1
                    continue
            if s[i] == 'X':
                    return_int = return_int + 10
                    i = i + 1
                    continue
            if s[i] == 'V':
                    return_int = return_int + 5
                    i = i + 1
                    continue
            if s[i] == 'I':
                    return_int = return_int + 1 
                    i = i + 1          
        return return_int


if __name__ == "__main__":
  print(Solution().romanToInt("MCMIX"))
