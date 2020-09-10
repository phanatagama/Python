from PIL import Image
from pyzbar.pyzbar import decode
import sys

def decodeQR(file):
	return decode(Image.open(file))[0][0].decode('utf-8')


def main():
	try:
		if len(sys.argv) > 1:
			print("[*] Message :",decodeQR(sys.argv[1]))
		else:
			print('[!] Usage : python {} <image>'.format(sys.argv[0]))
	except:
		print("[!] Failed : your image isn't valid")

if __name__ == '__main__':
	main()
