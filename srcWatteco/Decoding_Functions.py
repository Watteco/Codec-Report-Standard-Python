# -*- coding: utf-8 -*-

import json 
import dicttoxml
import xml
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree
from xml.etree import cElementTree as ET
from xml.dom import minidom
from ZCL_FRAME import *
from ZCL import *
import datetime

import sys

version = 'NKE_Frame_Codec_v_1.0.svn5087'


#-- coding/decoding in Standrd Mode
def Decoding_Standard(trame):
	#zclORbatch(trame)
	
	# Extract eventual parameters from end of input hexstring 
	(trame, args) = processHexMsgAndArgsString(trame)
	#print(args)
	
	print (version)
	date = datetime.datetime.now()
	print (date)
	print (STDFrame.parse(unhexlify(trame),args ))
	
#-- coding/decoding in JSON
def Decoding_JSON(trame, OnStdOut, OutPutProcessingFunction = None):
	d = {}
	d['version'] = version
	d['TimeStamp'] = datetime.datetime.now()
	
	# Extract eventual parameters from end of input hexstring 
	(trame, args) = processHexMsgAndArgsString(trame)
	#print(args)
	
	def myconverter(o):
		if isinstance(o, datetime.datetime):
			return o.__str__()
	
	if( OnStdOut ):
		try:
			sys.stdout.write(json.dumps(d, default = myconverter))
			sys.stdout.write("\n")
			
			decodedResult = STDFrame.parse(unhexlify(trame), args)
			if (OutPutProcessingFunction is not None): decodedResult = OutPutProcessingFunction(decodedResult)
			
			sys.stdout.write(json.dumps(decodedResult,indent=1))
		except:
			sys.stdout.write("A problem occured while trying to decode the frame. Please check the frame and try again.")
	else:
		try:
			decodedResult = STDFrame.parse(unhexlify(trame))
			if (OutPutProcessingFunction is not None): decodedResult = OutPutProcessingFunction(decodedResult)
			
			StringToReturn = json.dumps(decodedResult,indent=1)
				
		except:
			StringToReturn = "ERROR"
		
		return StringToReturn

	
def Decoding_JSON_VERIF(trame):
	
	# Extract eventual parameters from end of input hexstring 
	(trame, args) = processHexMsgAndArgsString(trame)
	#print(args)
	
	sys.stdout.write("\n")
	sys.stdout.write(json.dumps(STDFrame.parse(unhexlify(trame),args ),indent=1))
	print("\nVerification :\n")
	print("\ni:" + trame)
	print(hexlify(STDFrame.build(json.loads(json.dumps(STDFrame.parse(unhexlify(trame) ))))))
	
	print("\njson sans indentation:\n")
	sys.stdout.write(json.dumps(STDFrame.parse(unhexlify(trame) )))
	print("\n")

def Encoding_JSON(trame):	
	trame = bytearray(STDFrame.build(json.loads(trame)))
	if((trame[4])&1 != 0):
		trame[4] = ((len(trame)-7) << 1) + 1
	print(hexlify(trame))

#--coding/decoding in en XMl
def Decoding_XML_Pretty(trame):
	
	# Extract eventual parameters from end of input hexstring 
	(trame, args) = processHexMsgAndArgsString(trame)
	#print(args)
	
	xml_with_ids = dicttoxml.dicttoxml(STDFrame.parse(unhexlify(trame),args ),custom_root=version)
	print(parseString(xml_with_ids).toprettyxml())
	
def Decoding_XML_Line(trame):
	
	# Extract eventual parameters from end of input hexstring 
	(trame, args) = processHexMsgAndArgsString(trame)
	#print(args)
	
	print(dicttoxml.dicttoxml(STDFrame.parse(unhexlify(trame),args ),custom_root=version))

