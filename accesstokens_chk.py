#! python3

import requests , os , sys , time

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


print(R + '''+++++++++++++++++++++++++++++++++++++++++++++++++
+             access token master               +
+                CODER : BEN_TH                 +
+           WHATSAPP : +201006698345            +
+ please Dont use this script in spam (illegal) +
+    FB : www.facebook.com/bassem.beso.18659    +
+++++++++++++++++++++++++++++++++++++++++++++++++''')
print()
print('Put the path of the list or put your access tokens in the file named' + G + ' [access.txt] ' + W + ' and write ' + G + '[access.txt]')
print()
print(G + 'PATH :>> ', end='' + W)
put = input()

file = open(put , 'r')
readfile = file.read()
lista = readfile.split('\n')

# lista = ['kjlahsflhas' , 'ajskhkgas']

file.close()
print()
print(G + 'Starting ...')
print()
live = []
die = []

print(W + 'the number of access tokens : ' , G + str(len(lista)))
print()
print('+'.center(40 , '+'))
print()
# def chk(access):
	

x = 1
x2 =  .5
for access in lista:
	if x == 6:
		time.sleep(x2)
		x = 1
		x2 += .1
	if not access.isalnum():
		continue
	
	try:
		res = requests.get('https://graph.facebook.com/me?access_token=' + access)
	except Exception as exc:
		print(R + 'Error ... Skipping and' + G + ' Continue ...')
	


	if 'Error validating access token' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)
	elif 'The access token could not be decrypted' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)
	elif 'Malformed access token' in res.text:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(R + ' [!] DIE ...')
		die.append(access)

	else:
		print( G + '[*]' + ' Checking : ' + W + access  , end='')
		print(G + ' [!] LIVE ...')
		live.append(access)
	x +=1


print('LIVE = ', len(live))
print('DIE = ', len(die) )

os.makedirs('output' , exist_ok=True)

livefile = open(os.path.join('.','output','live.txt') , 'a')

for i in live:
	livefile.write(i + '\n')
livefile.close()

diefile = open(os.path.join('.','output','die.txt'), 'a')
for i in die:
	diefile.write(i + '\n')
diefile.close()
print('[*] The Results have been saved in the folder named'+ G + ' [Output] ... Goodbye' +W )
