ASCII_LOWER_OFFSET = ord('a')
ASCII_UPPER_OFFSET = ord('A')
ALPHABET_SIZE = 26


class ApplicationModel(object):
    def caesar_encode(self, message, key):
        result_list = []
        for char in message:
            if char.isalpha():
                if char.islower():
                    offset = ASCII_LOWER_OFFSET
                else:
                    offset = ASCII_UPPER_OFFSET
                char = chr((ord(char) - offset + key) % ALPHABET_SIZE + offset)
            result_list.append(char)
        return ''.join(result_list)
