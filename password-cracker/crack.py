import hashlib

flag = 0

pass_hash = ''

try:
	pass_file = open('passlist.txt', 'r')
except:
	print('No File Found')
	exit()

for word in pass_file:
	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strp()).hexdigest()

	if digest == pass_hash:
		print('Password is ' + word)
		flag = 1
		break

if flag = 0:
	print('Password/passphrase is not in the list')