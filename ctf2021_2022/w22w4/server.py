#!/usr/bin/env python3

import json
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import GCD, isPrime
from Crypto.Random.random import getrandbits
from socketserver import StreamRequestHandler, ThreadingTCPServer


HOST = "localhost"
PORT = 31337
BITS = 2048


class RSA:

	# Initialize values in RSA object so we can perform encryption and decryption.
	def __init__(self, bits):

		if bits % 512 != 0:
			raise ValueError("Argument \'bits\' must be a multiple of 512")
		self.n_bits = bits

		# Get two n_bits length primes and compute public modulus
		p = getrandbits(self.n_bits)
		while  True:
			if isPrime(p):
				break
			p += 1
		q = p + 1
		while True:
			if isPrime(q):
				break
			q += 1
		self.N = p*q

		# Compute keys
		carmichael_N = int((p-1)*(q-1)//GCD(p-1, q-1))
		self.e = 65537
		self.d = pow(self.e, -1, carmichael_N)


	# Return a copy of the public key.
	def public_key(self):
		return {"e": self.e, "N": self.N, "n_bits": self.n_bits}


	# Encrypt a given string plaintext
	def encrypt(self, ptxt):
		if len(ptxt) > self.n_bits//8:
			raise ValueError("Plaintext is too long.")

		int_ptxt = int.from_bytes(pad(bytes(ptxt, "utf-8"), self.n_bits//8), "big")
		ctxt = pow(int_ptxt, self.e, self.N)
		return ctxt


	# Decrypt a given int ciphertext
	def decrypt(self, ctxt):
		bytes_ptxt = pow(ctxt, self.d, self.N).to_bytes(self.n_bits//8, "big")
		ptxt = str(unpad(bytes_ptxt, self.n_bits//8), "utf-8")
		return ptxt


class FlagServer(StreamRequestHandler):

	def handle(self):

		# Get RSA instance for this client.
		rsa = RSA(BITS)

		# Read and encrypt flag
		with open("flag.txt") as f:
			flag = f.read().rstrip()
		ctxt = rsa.encrypt(flag)

		# Package encrypted flag with public key
		msg = rsa.public_key()
		msg["ctxt"] = ctxt
		
		self.request.send(bytes(json.dumps(msg), "utf-8"))


if __name__ == "__main__":
	ThreadingTCPServer((HOST, PORT), FlagServer).serve_forever()