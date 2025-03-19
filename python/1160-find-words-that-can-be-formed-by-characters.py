class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = Counter(chars)
        result = 0

        for word in words:
            word_counter = Counter(word)
            if char_counter >= word_counter:
                result += len(word)

        return result