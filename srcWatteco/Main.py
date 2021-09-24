#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Decoding_Functions import *
from Scroll_Decoding_Functions import *

# HUBO post processing (uncomment to test)
# from Modbus_Tools import *

def doDecode(frame, outFmt):
	if args.outputformat == 'std':
		Decoding_Standard(frame)
	elif args.outputformat== 'json':
		Decoding_JSON(frame, True)
		# HUBO post processing test (uncomment to test)
		# Decoding_JSON(frame, True,HUBOModbusDecodingPostProcess)
	elif args.outputformat== 'json-verif':
		Decoding_JSON_VERIF(frame)
	elif args.outputformat== 'xmlp':
		Decoding_XML_Pretty(frame)
	elif args.outputformat== 'xmll':
		Decoding_XML_Line(frame)
	print ("")


parser = argparse.ArgumentParser(description="NKE Watteco DECODER")
parser.add_argument("-m", "--mode", default='d', const='d',nargs='?',choices=['d', 'e'],help='Select the mode : [d=decode e=encode] default is "d" ; encode needs json input')

parser.add_argument("-if", "--inputframe", default='-', const='-',nargs='?',help='select the frame input : [- = std input; "hexstring";  ] default is "-" ')

parser.add_argument("-of", "--outputformat", default='json', const='json',nargs='?',choices=['json', 'xmll', 'xmlp', 'std', 'json-verif'],help='Decode the frame to the selected format default is "json"')
args = parser.parse_args()


if args.mode == 'd':
	if args.inputframe == '-':
	
		for frame in sys.stdin :
			doDecode(frame.rstrip(), args.outputformat)
			
	elif args.inputframe == '0x':
		doDecode(input(), args.outputformat)

	else:
		doDecode(args.inputframe, args.outputformat)
			
elif args.mode == 'e':
	for frame in sys.stdin :
		frame = frame.rstrip()
		Encoding_JSON(frame)
