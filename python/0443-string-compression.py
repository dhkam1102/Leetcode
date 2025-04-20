class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0

        while read < len(chars):
            count = 0
            character = chars[read]

            while read < len(chars) and character == chars[read]:
                count += 1
                read += 1

            chars[write] = character
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write

