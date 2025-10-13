class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ogword = "".join(sorted(words[0]))
        clean = [words[0]]
        for i in range(1, len(words)):
            word = "".join(sorted(words[i]))
            if word == ogword:
                pass
            else:
                clean.append(words[i])
                ogword = word 
        return clean