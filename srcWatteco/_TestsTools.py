#!python
# -*- coding: utf-8 -*-

# TODO: Continuer ce fichier de tests automatisés (pour Non reg ou autres ...)
"""
from construct import *
from construct.lib import *

from ZCL_FRAME import *
"""
from binascii import hexlify,unhexlify
from ZCL_FRAME import *
import json 
import sys

def setBracesOnDiffs(listdiff, a,b):
	# return 
	#  b if no diff
	#  b with square braces [] around string containing different hex digits
	#  if b is shorter than a ".." string is added to b before last ]
	#  And force two digit alignment of braces
	if (len(a) > len (b)) :
		b = b + ".."
		endDiff = len(b)
	else:
		endDiff = listdiff[len(listdiff)-1]
		endDiff = endDiff - (endDiff % 2) + 2
		
	startDiff = listdiff[0]
	startDiff = startDiff - (startDiff % 2)
		
	b = b[:startDiff] + '[' + b[startDiff:endDiff]+ ']' + b[endDiff:]
	
	return b

def diff(a, b):
	theMax = max(len(a), len(b))
	theMin = min(len(a), len(b))
	listdiff = [i for i in range(theMin) if a[i] != b[i]]
	for i in range(theMin,theMax): listdiff.append(i)

	# return input strings in with Braces to show diffs
	return setBracesOnDiffs(listdiff, b, a), setBracesOnDiffs(listdiff, a, b), 
	
	
	
	##### Purge Dict/Container from None values #########
def dictPurgeNoneValues(purged):
	if (isinstance(purged,dict) ):
		for k in list(purged):
			if purged[k] == None:
				del purged[k]
				# print(str(k)+"..DELETED")
			else:
				dictPurgeNoneValues(purged[k])
				
	elif (isinstance(purged,list) ):
		filter(lambda x: x!=None, purged)
		for k,item in enumerate(purged):
			dictPurgeNoneValues(purged[k])
			
	else:
		return purged
	
def prepareConstructForJSON (constructObj):
	resDict = constructObj
	# Remove None/Zombie Attributes comming from Parsing
	dictPurgeNoneValues(resDict)
	# Remove "private" entries ('_xxx", and replace strange 'u' before 'Enumxxx' ???)
	resDict = dict(resDict)
	if '_io' in resDict: del resDict['_io']
	resDict = (str(resDict)).replace("uEnum","Enum")
	# Then evaluate as a simple dict either than Construct Container
	resDict = eval(resDict)
	return(resDict)
	

class WTCParseStat:
	def __init__(self):
		self.Nb_TEST = 0
		self.Nb_OK = 0
		self.Nb_FAIL = 0
		self.Nb_ERR_HEXIN = 0
		self.Nb_ERR_PARSE = 0
		self.Nb_ERR_JSON = 0
		self.Nb_ERR_BUILD = 0
		self.Nb_ERR_SYM = 0


def WTCParseConclude():
	global gStats
	
	if ('gStats' not in globals()):
		WTCParseInit()
		
	print ("\nRESULTS\t     \t     \tERRORS")
	print ("TESTS\t   OK\t FAIL\tHEXIN\tPARSE\t JSON\t BUILD\t  SYM")
	print ("%5d\t%5d\t%5d\t%5d\t%5d\t%5d\t%5d\t%5d" % 
		(gStats.Nb_TEST,gStats.Nb_OK,gStats.Nb_FAIL,gStats.Nb_ERR_HEXIN,
		 gStats.Nb_ERR_PARSE,gStats.Nb_ERR_JSON,gStats.Nb_ERR_BUILD,gStats.Nb_ERR_SYM))
	
def WTCParseInit():
	global gStats 
	gStats = WTCParseStat()
	print ("RESULT\tHEX_IN\tHEX_OUT\tJSON")

def WTCParse(hexMsgInP, ERR_PARSE_EXP=False, ERR_JSON_EXP=False, PRINT_JSON_IF_OK=True):
	global gStats
	
	if ('gStats' not in globals()):
		WTCParseInit()
	
	gStats.Nb_TEST += 1
	try :
		# Extract eventual parameters from end of input hexstring 
		(hexMsgInP, args) = processHexMsgAndArgsString(hexMsgInP)
		#print(args)
		
		bytesIn = unhexlify(hexMsgInP.replace(" ", ""))
		hexMsgIn = hexlify(bytesIn).decode()
		try :
			obj = STDFrame.parse(bytesIn, args)
			try :
				json_str = json.dumps(prepareConstructForJSON(obj))
				print ("OK\t%s\t%s\t%s" % ( hexMsgIn,'',json_str if (PRINT_JSON_IF_OK) else ''))
				gStats.Nb_OK += 1
			except :
				gStats.Nb_ERR_JSON += 1
				if (ERR_JSON_EXP) :
					print ("OK err_json\t%s\t%s\t%s\t%s" % (hexMsgIn,"",prepareConstructForJSON(obj),sys.exc_info()))
					gStats.Nb_OK += 1
				else :
					print ("ERR_JSON\t%s\t%s\t%s\t%s" % (hexMsgIn,"",prepareConstructForJSON(obj),sys.exc_info()))
					gStats.Nb_FAIL += 1
		except:
			gStats.Nb_ERR_PARSE += 1
			if (ERR_PARSE_EXP) :
				print ("OK err_parse\t%s\t%s\t%s\t%s" % (hexMsgIn,'','',sys.exc_info()))
				gStats.Nb_OK += 1
			else :
				print ("ERR_PARSE\t%s\t%s\t%s\t%s" % (hexMsgIn,'','',sys.exc_info()))
				gStats.Nb_FAIL += 1
	except :
		print ("ERR_HEXIN\t%s\t%s\t%s\t%s" % (hexMsgInP,'','',sys.exc_info()))

def WTCParseBuildTest(format, hexMsgInP, 
	ERR_PARSE_EXP=False, ERR_JSON_EXP=False, ERR_BUILD_EXP=False, ERR_SYM_EXP=False, 
	PRINT_JSON_IF_OK=False):
	global gStats
	
	if ('gStats' not in globals()):
		WTCParseInit()
		
	gStats.Nb_TEST += 1
	try :
		# Extract eventual parameters from end of input hexstring 
		(hexMsgInP, args) = processHexMsgAndArgsString(hexMsgInP)
		#print(args)
		
		bytesIn = unhexlify(hexMsgInP.replace(" ", ""))
		hexMsgIn = hexlify(bytesIn).decode()
		try :
			obj = format.parse(bytesIn, args)
			try :
				json_str = json.dumps(prepareConstructForJSON(obj)) 
				try :
					bytesOut = format.build(obj, args) # TODO: Find why args not found when buildding (see PMEPMI validation test case)
					hexMsgOut = hexlify(bytesOut).decode()
					try :
						assert ( hexMsgIn == hexMsgOut) 
						print ("OK\t%s\t%s\t%s" % ( hexMsgIn,'',json_str if (PRINT_JSON_IF_OK) else ''))
						gStats.Nb_OK += 1
					except :
						gStats.Nb_ERR_SYM += 1
						a,b = diff(hexMsgIn,hexMsgOut)
						if (ERR_SYM_EXP) :
							print ("OK err_sym\t%s\t%s\t%s" % (a,b,json_str if (PRINT_JSON_IF_OK) else ''))
							gStats.Nb_OK += 1
						else :
							print ("ERR_SYM\t%s\t%s\t%s" % (a,b,json_str))
							gStats.Nb_FAIL += 1
				except:
					gStats.Nb_ERR_BUILD += 1
					if (ERR_BUILD_EXP) :
						print ("OK err_build\t%s\t%s\t%s\t%s" % (hexMsgIn,'',json_str if (PRINT_JSON_IF_OK) else '',sys.exc_info()))
						gStats.Nb_OK += 1
					else :
						print ("ERR_BUILD\t%s\t%s\t%s\t%s" % (hexMsgIn,'',json_str,sys.exc_info()[1]))
						gStats.Nb_FAIL += 1
				
			except :
				gStats.Nb_ERR_JSON += 1
				if (ERR_JSON_EXP) :
					print ("OK err_json\t%s\t%s\t%s\t%s" % (hexMsgIn,"",prepareConstructForJSON(obj),sys.exc_info()))
					gStats.Nb_OK += 1
				else :
					print ("ERR_JSON\t%s\t%s\t%s\t%s" % (hexMsgIn,"",prepareConstructForJSON(obj),sys.exc_info()))
					gStats.Nb_FAIL += 1
					
		except:
			gStats.Nb_ERR_PARSE += 1
			if (ERR_PARSE_EXP) :
				print ("OK err_parse\t%s\t%s\t%s\t%s" % (hexMsgIn,'','',sys.exc_info()))
				gStats.Nb_OK += 1
			else :
				print ("ERR_PARSE\t%s\t%s\t%s\t%s" % (hexMsgIn,'','',sys.exc_info()))
				gStats.Nb_FAIL += 1
	except :
		gStats.Nb_ERR_HEXIN += 1
		print ("ERR_HEXIN\t%s\t%s\t%s\t%s" % (hexMsgInP,'','',sys.exc_info()))
		gStats.Nb_FAIL += 1

