#!/usr/bin/env python3

import json
import socket


HOST = "chal.ctf-league.osusec.org"
PORT = 31337

HOST = "localhost"


if __name__ == "__main__":
	
	# Connect to server
	s = socket.socket()
	s.connect((HOST, PORT))

	# Display values received from server
	pkey = json.loads(s.recv(2600))
	print(f"n_bits: {pkey['n_bits']}")
	print(f"e: {pkey['e']}")
	print(f"N: {pkey['N']}")
	print(f"ctxt: {pkey['ctxt']}")

	s.close()