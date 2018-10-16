# Encrypt and Decrypt
'''
class Cipher:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
   # def __init__(self):
 '''       
    
def Encrypt():
    global text 
    global key
    global new_position
    global alphabet
    global decrypted
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = input("enter a text that you want to encrypt ")
    key = input("Enter a key: ")
    new_position = ''
    decrypted = ''
    
    
    for name in text:
        if name is not None:
            position = alphabet.find(name)
            encrypted_value = (position + int(key)) % 26
            encrypted_text = alphabet[encrypted_value]
            new_position = new_position + encrypted_text
            print(new_position)           
    return new_position


def Decrypt():
    for decrypt in new_position:
        if decrypt is not None:
            decrypt_position = alphabet.find(decrypt)
            decrypted_value = (position - int(key)) % 26
            decrypted_text = alphabet[decrypted_value]
            decrypted = decrypted + decrypted_text
    return decrypted
        
e = Encrypt()

print("-------------------------------------------------")
print("Entered text is {} ".format(text))
print("Encrypted message is {} ".format(e))

d = Decrypt()
print("-------------------------------------------------")
print("Encryted text is {} ".format(text))
print("decrypted message is {} ".format(d))

