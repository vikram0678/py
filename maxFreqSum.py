# Find Most Frequent Vowel and Consonant

##  This program finds the most frequent vowel and consonant in a given lowercase string.  
##  It calculates their frequencies and returns the sum of both maximum frequencies.  

##  Example  
##  Input: `successes` → Output: `6`  
##  Input: `aeiaeia` → Output: `3`  


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        freq ={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        count_vowels = 0
        max_vowels = 0
        count_consonents = 0
        max_consonents = 0
        for char in freq:
            if char in vowels:
                max_vowels = max(freq[char], max_vowels)
            else:
                max_consonents = max(freq[char], max_consonents)
        return max_vowels + max_consonents
        

s="successes"
print(maxFreqSum(s))




# var maxFreqSum = function(s) {
#     let map ={};
#     for(let i = 0;i < s.length ; i++){
#         map[s[i]] = !map[s[i]] ? 1 : ++map[s[i]];
#     }
#     let vowels = ['a', 'e', 'i', 'o', 'u']
#     let maxVowels = 0;
#     let maxConsonant = 0;
#     let mapKeys = Object.keys(map);
#     for(let i = 0; i< mapKeys.length; i++){
#         if(vowels.includes(mapKeys[i])){
#             maxVowels = Math.max(maxVowels, map[mapKeys[i]])
#         }else{
#             maxConsonant = Math.max(maxConsonant, map[mapKeys[i]])
#         }
#     }
#     return maxVowels + maxConsonant
# };
