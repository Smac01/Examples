"""

RSA (Asymmetric key cryptography)

 # Select two prime numbers p and q
 # Calculate n, such that n = (p * q)
 # Calculate 𝜙 (i.e phi), such that 𝜙 = (p-1) * (q-1)
 # Assume e, such that GCD(e, 𝜙(n)) = 1 and 1 < e < 𝜙(n) [co-prime]
 # Calculate d, such that d = ((𝜙(n) * i) + 1)/e is a whole number
 	# for i = 1 to 𝜙(n)

 # public key = { e, n }
 # private key = { d, n }

 # Encryption (convert plain text to cipher text)
 	# n should be greater than p (n > p)
 	# C = P^e mod n
 # Decryption (convert cipher text to plain text)
 	# P = C^d mod n

large primes:
p = 4529744291791584270107578401453542323616929750509389288843976597908183837251007222475788228191611764608260075490017363957004182537994337990875226354778778508897973109554522950148540918578243540540499704650434750455631645633356810232965826630971061107
q = 4164215748648093797608606675963547884055923752159129834747187730572469388547663115656464947509474130604943276802503049091123710432817560978941447232446050654745188389882267330722651570942096755573062086156639674260502720382675953064353409525592485141

"""


import math

def bytes_to_long(text: str) -> int:
	return int.from_bytes(text.encode(), byteorder='little')

def calculate_e(phi: int) -> int:
	"""Calculate e value with contraint gcd(e, phi) == 1 """
	for i in range(2, phi):
		if(math.gcd(phi, i) == 1):
			return i

def calculate_d(phi: int, e: int) -> int:
	"""Calculate d value"""
	for i in range(1, phi):
		temp = divmod(((phi * i) + 1), e)
		if(not temp[-1]):
			return temp[0]

plain_text = 'A quick brown fox jumps over the lazy dog'
# convert plain text to int value
p2i = bytes_to_long(plain_text) 

# prime numbers
p = 57140694569194923997089675352334396002512364480036647869314851331421918217214154304944524415966781659
q = 33902784548282375116964388270838028192268243957691211282369267923758155734015998147223844817542695019

n = p * q

# Euler's totient function
phi = (p-1) * (q-1)

# calculate digits length
plen = round(math.log10(p2i)) + 1
nlen = round(math.log10(n)) + 1

if(plen >= nlen):
	print("Can't perform RSA operation on plain text. Plain text length must less than n (use large prime numbers)")
	exit(1)

e = calculate_e(phi)

d = calculate_d(phi, e)

# public_key = { e, n }
# private_key = { d, n }

# convert plain text to cipher text
p2c = pow(p2i, e, n)

# convert cipher text to plain text
c2p = pow(p2c, d, n)

print('(Plain  text)', plain_text)
print('(Cipher text)', p2c)
print('\n=>', bytes.fromhex(format(c2p, 'x'))[::-1])
