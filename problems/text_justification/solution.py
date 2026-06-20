class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        final=[]
        current=[]
        numalpha=0
        for word in words:
            if numalpha+len(word)+len(current)>maxWidth:
                for i in range(maxWidth-numalpha):
                    current[i % (len(current) - 1 or 1)] += ' '
                final.append("".join(current))
                current=[]
                numalpha=0
            current.append(word)
            numalpha+=len(word)
        final.append(" ".join(current).ljust(maxWidth))
        return final