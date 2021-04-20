from Crypto.Hash import SHA3_224
h_obj = SHA3_224.new()
h_obj.update(b'Some data')
print(h_obj.hexdigest())