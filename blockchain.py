import json
import hashlib
from time import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		self.new_block(previous_hash=1,proof=100)

	def new_block(self, proof, previous_hash=None):
		block = {
		#increment size of the chain
		'index' : len(self.chain) + 1,
		'timestamp': time(),
		'transaction': self.current_transactions,
		'proof': proof,
		#hash of the last block
		'previous_hash': previous_hash or self.hash(self.chain[-1]), 
		}

		self.current_transactions = []
		self.chain.append(block)
		return block

	# Add a transaction to a block
	def new_transaction(self, sender, receiver, amount):
		self.current_transactions.append({
			'sender' : sender,
			'receiver': receiver,
			'amount' : amount,
			})

		return self.last_block['index'] + 1


	@staticmethod
	def hash(block):
		#Convert dictionary 'block' to JSON and make it ordered
		#encode() ensures it is a bytestring
		block_string = json.dumps(block, sort_keys=True).encode()
		#returns hash string
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		# Returns last block of the chain
		return (self.chain[-1])