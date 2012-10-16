""":mod:`caesar_cipher.models --- Application models`
"""

ASCII_LOWER_OFFSET = ord('a')
ASCII_UPPER_OFFSET = ord('A')
ALPHABET_SIZE = 26


class ApplicationModel(object):
    """Primary application model."""
    def caesar_encode(self, text, key):
        """Encode a Caesar cipher.

        :param text: the text to encode
        :type text: :class:`str`
        :param key: the number by which to rotate
        :type key: :class:`int`
        :return: the encoded text
        :rtype: :class:`str`
        """
        result_list = []
        for char in text:
            if char.isalpha():
                if char.islower():
                    offset = ASCII_LOWER_OFFSET
                else:
                    offset = ASCII_UPPER_OFFSET
                char = chr((ord(char) - offset + key) % ALPHABET_SIZE + offset)
            result_list.append(char)
        return ''.join(result_list)
