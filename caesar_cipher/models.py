

class ApplicationModel(object):
    def caesar_encode(self, message, key):
        result = []
        for i in range(len(message)):
            result.append(chr(ord(message[i]) + key))
        return ''.join(result)