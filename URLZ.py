
rep = lambda r: r.replace(' ', '')
hexToAsc = lambda h: ''.join((chr(int(rep(h)[i:i+2], 16)) for i in range(0, len(rep(h)), 2)))

def getHexs(URL):
	salida = []
	for i, c in enumerate(URL):
		if not c == '%':
			continue
		else:
			hexa = URL[i+1:i+3]
			if hexa not in salida:
				salida.append(hexa)
	salida.sort()
	return salida


if __name__ == '__main__':
	
	l_hex = []
	ver = 'v1.0.1'
	# ~ URL = 'http%3A%2F%2Fwww.mediafire.com%2Ffile%2F972uw7faxf6yswe%2FSeguridad%2BInformatica-20170725T135202Z-001.zip%3Ffbclid%3DIwAR1Eoa0-90t6rJZz8kZv2tkxOrcdOCQZapCKz4Due919ltKH_Z7F9ZFH-ZA'
	
	print('\n URLZ {}'.format(ver))
	URL = input('\n [?] URL:\n ')
	
	hexs = getHexs(URL)
	
	for h in hexs:
		asc = hexToAsc(h)
		l_hex.append((h, asc))
		URL = URL.replace('%'+h, asc)
	
	print('\n [+] Resultado:\n', URL)
