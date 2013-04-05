""":mod:`caesar_cipher.models --- Application models`
"""

ASCII_LOWER_OFFSET = ord('a')
ASCII_UPPER_OFFSET = ord('A')
ALPHABET_SIZE = 26

from caesar_cipher.utils import Event


class ApplicationModel(object):
    """Primary application model."""

    def __init__(self):
        """Create event for when application starts."""
        self.started = Event()

    def run(self):
        """Called after the model is created."""
        self.started()

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
