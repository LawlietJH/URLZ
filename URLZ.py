

def Hex_Asc(Hex):	#~ Hexadecimal a Ascii
	
	Hex = Hex.replace(' ', '')		#~ Quita los espacios.
	
	Ascii = ''.join((chr(int(Hex[i:i+2], 16)) for i in range(0, len(Hex), 2)))
	
	return Ascii


def getHexs(URL):
	save = False
	cont = 0
	hexa = ''
	salida = []
	for c in URL:
		if save:
			hexa += c
			if len(hexa) == 2:
				if hexa not in salida:
					salida.append(hexa)
				save = False
				cont = 0
				hexa = ''
		if '%' == c:
			save = True
	return salida



if __name__ == '__main__':
	
	l_hex = []
	ver = '1.0.0'
	# ~ URL_Prueba = 'http%3A%2F%2Fwww.mediafire.com%2Ffile%2F972uw7faxf6yswe%2FSeguridad%2BInformatica-20170725T135202Z-001.zip%3Ffbclid%3DIwAR1Eoa0-90t6rJZz8kZv2tkxOrcdOCQZapCKz4Due919ltKH_Z7F9ZFH-ZA'
	
	print('\n URLZ {}'.format(ver))
	URL = input('\n\n [?] URL:\n ')
	
	hexs = getHexs(URL)
	
	for h in hexs:
		asc = Hex_Asc(h)
		l_hex.append((h, asc))
		URL = URL.replace('%'+h, asc)
	
	print('\n [+] Resultado:\n', URL)
