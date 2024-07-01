class Solution(object):
    def romanToInt(self, s):
        Roman={ "I":1, "v":5,"x":10,
                "L":50,"C":100,"D":500, "M":1000}
        N=len(s)
        i=N-1
        output=0
        while i>=0:
            if i < N-1 and Roman[s[i]]<Roman[s[i+1]]:
                output-=Roman[s[i]]
            else:
                output+=Roman[s[i]]
            i-=1
        return output