# -*- coding: utf-8 -*-
from ._TIC_Tools import *


###
#
# New method avoiding code duplication but more complex behind 
# Cf _TIC_Tools.py:
#   TIC_STDField, TIC_STDFieldRepeater, TIC_BatchType
# 
# [(<Fid>,<Batchable>,<Label>,<Type/SubCons>),...]
#
###

CBEFields = [
	( 0,	True,	"ADIR1",	Int16ub),
	( 1,	True,	"ADIR2",	Int16ub),
	( 2,	True,	"ADIR3",	Int16ub),
	( 3,	False,	"ADCO",		BytesToUTF8Class(CString())),
	( 4,	False,	"OPTARIF",	BytesToUTF8Class(CString())),
	( 5,	True,	"ISOUSC",	Int8ub),
	( 6,	True,	"BASE",		Int32ub),
	( 7,	True,	"HCHC",		Int32ub),
	
	( 8,	True,	"HCHP",		Int32ub),
	( 9,	True,	"EJPHN",	Int32ub),
	(10,	True,	"EJPHPM",	Int32ub),
	(11,	True,	"BBRHCJB",	Int32ub),
	(12,	True,	"BBRHPJB",	Int32ub),
	(13,	True,	"BBRHCJW",	Int32ub),
	(14,	True,	"BBRHPJW",	Int32ub),
	(15,	True,	"BBRHCJR",	Int32ub),
	
	(16,	True,	"BBRHPJR",	Int32ub),
	(17,	True,	"PEJP",		Int8ub),
	(18,	True,	"GAZ",		Int32ub),
	(19,	True,	"AUTRE",	Int32ub),
	(20,	False,	"PTEC",		BytesToUTF8Class(CString())),
	(21,	False,	"DEMAIN",	BytesToUTF8Class(CString())),
	(22,	True,	"IINST",	Int16ub),
	(23,	True,	"IINST1",	Int16ub),
	
	(24,	True,	"IINST2",	Int16ub),
	(25,	True,	"IINST3",	Int16ub),
	(26,	True,	"ADPS",		Int16ub),
	(27,	True,	"IMAX",		Int16ub),
	(28,	True,	"IMAX1",	Int16ub),
	(29,	True,	"IMAX2",	Int16ub),
	(30,	True,	"IMAX3",	Int16ub),
	(31,	True,	"PMAX",		Int32ub),
	
	(32,	True,	"PAPP",		Int32ub),
	(33,	False,	"HHPHC",	BytesToUTF8Class(String(1))),
	(34,	False,	"MOTDETAT",	BytesToUTF8Class(CString())),
	(35,	False,	"PPOT",		BytesToUTF8Class(CString())),
]	
		
TICDataCBEFromBitfields = TIC_STDFieldRepeater(len(CBEFields), TIC_STDField(CBEFields,FindFieldBitField))

TICDataBatchCBEFromFieldIndex = TIC_BatchType(FindFieldIndex,CBEFields)



