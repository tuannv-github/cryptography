from Crypto.Cipher import AES
key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(input('Enter a message: ').encode('ascii'))

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print(f'Cipher text: {ciphertext}')

if not plaintext:
    print('Message is corrupted!')
else:
    print(f"Plain text: {plaintext.decode('ascii')}")