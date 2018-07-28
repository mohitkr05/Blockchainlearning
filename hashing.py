#
# Python implementation for blockchain understanding
import hashlib

def hash256(message):
	return hashlib.sha256(message.encode('utf-8')).hexdigest()

print("This program will generate a sha256 hash, the goal of this program is to make sure that the the output has a fixed length")
message = input("Please enter the message to be encrypted\n")
print(hash256(message))




