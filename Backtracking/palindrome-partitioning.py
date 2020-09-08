class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == None or len(s) == 0:
            return []
        result = []
        self.helper(s, [], result)
        return result
    
    
    def helper(self, s, current, result):
        if s == None or len(s) == 0:
            result.append(list(current))
            return
        else:
            for i in range(1, len(s)+1, 1):
                temp = s[:i]
                if(self.checkPalindrome(temp)==True):
                    current.append(temp)
                    self.helper(s[i:], current, result)
                    current.pop()
            return
              
    def checkPalindrome(self, s):
        i = 0
        j = len(s)-1
        while(i <= j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
