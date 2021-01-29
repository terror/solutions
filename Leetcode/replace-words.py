class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(dict)):
            w = dict[i]
            for j in range(len(sentence)):
                if sentence[j].startswith(w):
                    sentence[j] = w

        ans, idx = "", 0
        for i in sentence:
            if idx != len(sentence)-1:
                ans += "{} ".format(i)
            else:
                ans += i
            idx += 1
        return ans
