class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = []
        for word in strs:
            answer.append(str(len(word))+'#'+word)
        return "".join(answer)

    def decode(self, s: str) -> List[str]:
        print(s)
        answer = []
        i = 0
        while i < len(s):
            begin = i
            while s[i] != '#':
                i += 1
            word = s[i+1:int(s[begin:i]) + i+1]
            answer.append(word)
            i = int(s[begin:i]) + i+1
        return answer
