# -*- coding: utf-8 -*-
from ._TIC_Tools import *
from ._TIC_Types import *

###
#
# New method avoiding code duplication but more complex behind 
# Cf _TIC_Tools.py:
#   TIC_STDField, TIC_STDFieldRepeater, TIC_BatchType
# 
# [(<Fid>,<Batchable>,<Label>,<Type/SubCons>),...]
#
###

STDFields = [
	( 0,	False,	"ADSC",	BytesToUTF8Class(CString())),
	( 1,	True,	"VTIC",	Int8ub),
	( 2,	False,	"DATE",	TYPE_SDMYhms),
	( 3,	False,	"NGTF",	TYPE_STD_E_CONTRAT),
	( 4,	True,	"LTARF",	TYPE_STD_E_PT),
	( 5,	True,	"EAST",	Int32ub),
	( 6,	True,	"EASF01",	Int32ub),
	( 7,	True,	"EASF02",	Int32ub),

	( 8,	True,	"EASF03",	Int32ub),
	( 9,	True,	"EASF04",	Int32ub),
	(10,	True,	"EASF05",	Int32ub),
	(11,	True,	"EASF06",	Int32ub),
	(12,	True,	"EASF07",	Int32ub),
	(13,	True,	"EASF08",	Int32ub),
	(14,	True,	"EASF09",	Int32ub),
	(15,	True,	"EASF10",	Int32ub),

	(16,	True,	"EASD01",	Int32ub),
	(17,	True,	"EASD02",	Int32ub),
	(18,	True,	"EASD03",	Int32ub),
	(19,	True,	"EASD04",	Int32ub),
	(20,	True,	"EAIT",	Int32ub),
	(21,	True,	"ERQ1",	Int32ub),
	(22,	True,	"ERQ2",	Int32ub),
	(23,	True,	"ERQ3",	Int32ub),

	(24,	True,	"ERQ4",	Int32ub),
	(25,	True,	"IRMS1",	Int16ub),
	(26,	True,	"IRMS2",	Int16ub),
	(27,	True,	"IRMS3",	Int16ub),
	(28,	True,	"URMS1",	Int16ub),
	(29,	True,	"URMS2",	Int16ub),
	(30,	True,	"URMS3",	Int16ub),
	(31,	True,	"PREF",	Int8ub),

	(32,	True,	"PCOUP",	Int8ub),
	(33,	True,	"SINSTS",	Int24ub),
	(34,	True,	"SINSTS1",	Int24ub),
	(35,	True,	"SINSTS2",	Int24ub),
	(36,	True,	"SINSTS3",	Int24ub),
	(37,	False,	"SMAXN",	TYPE_SDMYhmsU24),
	(38,	False,	"SMAXN1",	TYPE_SDMYhmsU24),
	(39,	False,	"SMAXN2",	TYPE_SDMYhmsU24),

	(40,	False,	"SMAXN3",	TYPE_SDMYhmsU24),
	(41,	False,	"SMAXN_1",	TYPE_SDMYhmsU24),
	(42,	False,	"SMAXN1-1",	TYPE_SDMYhmsU24),
	(43,	False,	"SMAXN2-1",	TYPE_SDMYhmsU24),
	(44,	False,	"SMAXN3-1",	TYPE_SDMYhmsU24),
	(45,	True,	"SINSTI",	Int24ub),
	(46,	False,	"SMAXIN",	TYPE_SDMYhmsU24),
	(47,	False,	"SMAXIN-1",	TYPE_SDMYhmsU24),

	(48,	False,	"CCASN",	TYPE_SDMYhmsU24),
	(49,	False,	"CCASN-1",	TYPE_SDMYhmsU24),
	(50,	False,	"CCAIN",	TYPE_SDMYhmsU24),
	(51,	False,	"CCAIN-1",	TYPE_SDMYhmsU24),
	(52,	False,	"UMOY1",	TYPE_SDMYhmsU16),
	(53,	False,	"UMOY2",	TYPE_SDMYhmsU16),
	(54,	False,	"UMOY3",	TYPE_SDMYhmsU16),
	(55,	False,	"STGE",	TYPE_U32xbe),

	(56,	False,	"DPM1",	TYPE_SDMYhmsU8),
	(57,	False,	"FPM1",	TYPE_SDMYhmsU8),
	(58,	False,	"DPM2",	TYPE_SDMYhmsU8),
	(59,	False,	"FPM2",	TYPE_SDMYhmsU8),
	(60,	False,	"DPM3",	TYPE_SDMYhmsU8),
	(61,	False,	"FPM3",	TYPE_SDMYhmsU8),
	(62,	False,	"MSG1",	BytesToUTF8Class(CString())),
	(63,	False,	"MSG2",	BytesToUTF8Class(CString())),

	(64,	False,	"PRM",	BytesToUTF8Class(CString())),
	(65,	False,	"RELAIS",	TYPE_bf8d),
	(66,	True,	"NTARF",	Int8ub),
	(67,	True,	"NJOURF",	Int8ub),
	(68,	True,	"NJOURFp1",	Int8ub),
	(69,	False,	"PJOURFp1", TYPE_11hhmmSSSS),
	(70,	False,	"PPOINTE",	TYPE_11hhmmSSSS)
]
		
TICDataSTDFromBitfields = TIC_STDFieldRepeater(len(STDFields), TIC_STDField(STDFields,FindFieldBitField))
TICDataBatchSTDFromFieldIndex = TIC_BatchType(FindFieldIndex,STDFields)
