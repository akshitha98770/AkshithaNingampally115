def totalFruit(fruits: List[int]) -> int:
        left =0
        ans=0
        freq={}
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
fruits=[1,2,2]
print(totalFruit(fruits))
def lengthOfLongestSubstring(s: str) -> int:
        left,ans=0,0
        char_set=set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            ans=max(ans,right-left+1)
        return ans
s="abcaabbcc"
print(lengthOfLongestSubstring(s))