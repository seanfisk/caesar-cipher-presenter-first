class ApplicationModel(object):
    def caesar_encode(self, message, key):
        result = []
        check = 0
        for i in range(len(message)):
            if(message[i].islower()):
                check = ord('a') + ((ord(message[i]) - ord('a') + key) % 26)
            else:
                check = ord('A') + ((ord(message[i]) - ord('A') + key) % 26)
            result.append(chr(check))
        return ''.join(result)