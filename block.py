import hashlib


class Block:
	def __init__(self, id, data):
		self.id = id
		self.data = data

	def mine(self):
		nonce = 0
		while True:
			sha256digest = hashlib.sha256((self.data + str(nonce)).encode('utf-8')).hexdigest()
			nonce = nonce +1
			print(nonce,sha256digest)
			if (str(sha256digest[0:4]) == '0000'):
				return (nonce)



b = Block(1,"x")
print(b.mine())