#A sample block chain with n number of nodes
#To do rather than id, include the hash of the block
import hashlib

class Block:
	def __init__(self, id, data , prev):
		self.id = id
		#Define the genesis block
		self.data = data
		if (self.id==1):
			self.prev = '0000000000000000000000000000000000000000000000000000000000000000'
		else:
			self.prev = prev
		nonce_blockhash = self.mine()
		self.nonce_blockhash = nonce_blockhash
		self.prev  = prev
		

	def mine(self):
		nonce = 0
		while True:
			sha256digest = hashlib.sha256((self.data + str(self.prev) + str(nonce)).encode('utf-8')).hexdigest()
			nonce = nonce +1
			if (str(sha256digest[0:4]) == '0000'):
				return (nonce,sha256digest)



	def display_block(self):
		print("------------------------------------------------------------")
		print("Block number " + str(self.id) )
		print("nonce = " + str(self.nonce_blockhash[0]))
		print("hash = " + str(self.nonce_blockhash[1]))
		print("previous = " + str(self.prev))
		print("------------------------------------------------------------")


class BlockChain:
	def __init__(self,number):
		self.number = number
		for x in range(1,self.number):
			if x > 0:
				b = Block(x,"x",x-1)
				b.display_block()



chain = BlockChain(10)

