class Solution:
    #want to store lengths of each string in a list
    #prefix it with a terminating character
    #iterate through list and simultaneously thru string
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s+=str(len(strs[i]))
            s+="#"
            s+=strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        while(s.find("#") != -1):
            start_index = s.find("#")+1
            end_index = s.find("#")+1+int(s[0:s.find("#")])
            ans.append(s[start_index:end_index])
            if(end_index<len(s)):
                s = s[end_index:]
            else:
                s = ""
        return ans



"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded = encoded + strs[i] + "/0"
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        print(s.count("/0"))
        while("/0" in s):
            print(s.find("/0"))
            ans.append(s[:s.find("/0")])
            s = s[s.find("/0")+2:]
        return ans
"""