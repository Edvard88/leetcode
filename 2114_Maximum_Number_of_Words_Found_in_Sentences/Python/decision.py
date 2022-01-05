from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        len_of_sentences = {}

        for number_of_sent, sentence in enumerate(sentences):
            len_of_sentences[sentence] = len(sentence.split())

        return max(len_of_sentences.values())


if __name__ == '__main__':

    sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
    solution = Solution()

    result = solution.mostWordsFound(sentences)

    print(result)