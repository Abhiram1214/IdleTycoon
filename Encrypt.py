# Encrypt and Decrypt


class Cipher:

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.new_position = ''
        self.decrypted = ''


    def Encrypt(self):
        text = input("enter a text that you want to encrypt ")
        global key
        key = input("Enter a key: ")

        for name in text:
            if name is not None:
                position = self.alphabet.find(name)
                encrypted_value = (position + int(key)) % 26
                encrypted_text = self.alphabet[encrypted_value]
                self.new_position = self.new_position + encrypted_text
                print(self.new_position)
        return self.new_position


    def Decrypt(self, e):

        for decrypt in e:
            if decrypt is not None:
                print(decrypt)
                decrypt_position = self.alphabet.find(decrypt)
                decrypted_value = (decrypt_position - int(key)) % 26
                decrypted_text = self.alphabet[decrypted_value]
                self.decrypted = self.decrypted + decrypted_text
        return self.decrypted

result = Cipher()

Encrypted = result.Encrypt()
print("The encrypted mesaage is {} ".format(Encrypted))

print("-------------------------------------------------")

Decrypted = result.Decrypt(Encrypted)
print("The mesaage when decrypted back is {} ".format(Decrypted))
