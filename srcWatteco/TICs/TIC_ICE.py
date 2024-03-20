# -*- coding: utf-8 -*-
from ._TIC_Tools import *
from ._TIC_Types import *

###
#
# New method avoiding code duplication but more complex behind 
# Cf _TIC_Tools.py:
#   TIC_STDField, TIC_STDFieldRepeater, TIC_BatchType
# 
# [(<Fid>,<Batchable>,<Label>,<Type/SubCons>[,<meterVersion>]),...]
#
###

ICEGeneralFields = [
	( 0,	False,	"CONTRAT",	BytesToUTF8Class(CString())),
	( 1,	False,	"DATECOUR",	TYPE_DMYhms, "-"),
	( 2,	False,	"DATE",	TYPE_DMYhms, "2.4"),
	( 3,	True,	"EA",	Int24ub),
	( 4,	True,	"ERP",	Int24ub),
	( 5,	False,	"PTCOUR",	BytesToUTF8Class(CString() )),
	( 6,	False,	"PREAVIS",	BytesToUTF8Class(CString() )),
	( 7,	False,	"MODE",	Computed("CONTROLE"), "-" ),

	( 8,	False,	"DATEPA1",	TYPE_DMYhms),
	( 9,	True,	"PA1",	Int16ub),
	(10,	False,	"DATEPA2",	TYPE_DMYhms),
	(11,	True,	"PA2",	Int16ub),
	(12,	False,	"DATEPA3",	TYPE_DMYhms),
	(13,	True,	"PA3",	Int16ub),
	(14,	False,	"DATEPA4",	TYPE_DMYhms),
	(15,	True,	"PA4",	Int16ub),

	(16,	False,	"DATEPA5",	TYPE_DMYhms),
	(17,	True,	"PA5",	Int16ub),
	(18,	False,	"DATEPA6",	TYPE_DMYhms),
	(19,	True,	"PA6",	Int16ub),
	(20,	False,	"*P*",	Pass),
	(21,	True,	"KDC",	Int8ub),
	(22,	True,	"KDCD",	Int8ub),
	(23,	True,	"TGPHI",	Float32b, "2.4"),

	(24,	True,	"PSP",	Int16ub),
	(25,	True,	"PSPM",	Int16ub),
	(26,	True,	"PSHPH",	Int16ub),
	(27,	True,	"PSHPD",	Int16ub),
	(28,	True,	"PSHCH",	Int16ub),
	(29,	True,	"PSHCD",	Int16ub),
	(30,	True,	"PSHPE",	Int16ub),
	(31,	True,	"PSHCE",	Int16ub),

	(32,	True,	"PSJA",	Int16ub),
	(33,	True,	"PSHH",	Int16ub),
	(34,	True,	"PSHD",	Int16ub),
	(35,	True,	"PSHM",	Int16ub),
	(36,	True,	"PSDSM",	Int16ub),
	(37,	True,	"PSSCM",	Int16ub),
	(38,	False,	"MODE",	Computed("CONTROLE"), "2.4"),
	(39,	True,	"PA1MN",	Int16ub),
	
	(40,	True,	"PA10MN",	Int16ub),
	(41,	True,	"PREA1MN",	Int16sb),
	(42,	True,	"PREA10MN",	Int16sb),
	(43,	True,	"TGPHI",	Float32b, "-"),
	(44,	True,	"U10MN",	Int16ub)
]

ICEpFields = [
	( 0,	False,	"DEBUTp",	TYPE_DMYhms),
	( 1,	False,	"FINp",	TYPE_DMYhms),
	( 2,	True,	"CAFp",	Int16ub),
	( 3,	False,	"DATE_EAp",	TYPE_DMYhms),
	( 4,	True,	"EApP",	Int24ub),
	( 5,	True,	"EApPM",	Int24ub),
	( 6,	True,	"EApHCE",	Int24ub),
	( 7,	True,	"EApHCH",	Int24ub),

	( 8,	True,	"EApHH",	Int24ub),
	( 9,	True,	"EApHCD",	Int24ub),
	(10,	True,	"EApHD",	Int24ub),
	(11,	True,	"EApJA",	Int24ub),
	(12,	True,	"EApHPE",	Int24ub),
	(13,	True,	"EApHPH",	Int24ub),
	(14,	True,	"EApHPD",	Int24ub),
	(15,	True,	"EApSCM",	Int24ub),

	(16,	True,	"EApHM",	Int24ub),
	(17,	True,	"EApDSM",	Int24ub),
	(18,	False,	"DATE_ERPp",	TYPE_DMYhms),
	(19,	True,	"ERPpP",	Int24ub),
	(20,	True,	"ERPpPM",	Int24ub),
	(21,	True,	"ERPpHCE",	Int24ub),
	(22,	True,	"ERPpHCH",	Int24ub),
	(23,	True,	"ERPpHH",	Int24ub),

	(24,	True,	"ERPpHCD",	Int24ub),
	(25,	True,	"ERPpHD",	Int24ub),
	(26,	True,	"ERPpJA",	Int24ub),
	(27,	True,	"ERPpHPE",	Int24ub),
	(28,	True,	"ERPpHPH",	Int24ub),
	(29,	True,	"ERPpHPD",	Int24ub),
	(30,	True,	"ERPpSCM",	Int24ub),
	(31,	True,	"ERPpHM",	Int24ub),

	(32,	True,	"ERPpDSM",	Int24ub),
	(33,	False,	"DATE_ERNp",	TYPE_DMYhms),
	(34,	True,	"ERNpP",	Int24ub),
	(35,	True,	"ERNpPM",	Int24ub),
	(36,	True,	"ERNpHCE",	Int24ub),
	(37,	True,	"ERNpHCH",	Int24ub),
	(38,	True,	"ERNpHH",	Int24ub),
	(39,	True,	"ERNpHCD",	Int24ub),
	
	(40,	True,	"ERNpHD",	Int24ub),
	(41,	True,	"ERNpJA",	Int24ub),
	(42,	True,	"ERNpHPE",	Int24ub),
	(43,	True,	"ERNpHPH",	Int24ub),
	(44,	True,	"ERNpHPD",	Int24ub),
	(45,	True,	"ERNpSCM",	Int24ub),
	(46,	True,	"ERNpHM",	Int24ub),
	
	(47,	True,	"ERNpDSM",	Int24ub)
]

ICEp1Fields = [
	( 0,	False,	"DEBUTp1",	TYPE_DMYhms),
	( 1,	False,	"FINp1",	TYPE_DMYhms),
	( 2,	True,	"CAFp1",	Int16ub),
	( 3,	False,	"DATE_EAp1",	TYPE_DMYhms),
	( 4,	True,	"EAp1P",	Int24ub),
	( 5,	True,	"EAp1PM",	Int24ub),
	( 6,	True,	"EAp1HCE",	Int24ub),
	( 7,	True,	"EAp1HCH",	Int24ub),

	( 8,	True,	"EAp1HH",	Int24ub),
	( 9,	True,	"EAp1HCD",	Int24ub),
	(10,	True,	"EAp1HD",	Int24ub),
	(11,	True,	"EAp1JA",	Int24ub),
	(12,	True,	"EAp1HPE",	Int24ub),
	(13,	True,	"EAp1HPH",	Int24ub),
	(14,	True,	"EAp1HPD",	Int24ub),
	(15,	True,	"EAp1SCM",	Int24ub),

	(16,	True,	"EAp1HM",	Int24ub),
	(17,	True,	"EAp1DSM",	Int24ub),
	(18,	False,	"DATE_ERPp1",	TYPE_DMYhms),
	(19,	True,	"ERPp1P",	Int24ub),
	(20,	True,	"ERPp1PM",	Int24ub),
	(21,	True,	"ERPp1HCE",	Int24ub),
	(22,	True,	"ERPp1HCH",	Int24ub),
	(23,	True,	"ERPp1HH",	Int24ub),

	(24,	True,	"ERPp1HCD",	Int24ub),
	(25,	True,	"ERPp1HD",	Int24ub),
	(26,	True,	"ERPp1JA",	Int24ub),
	(27,	True,	"ERPp1HPE",	Int24ub),
	(28,	True,	"ERPp1HPH",	Int24ub),
	(29,	True,	"ERPp1HPD",	Int24ub),
	(30,	True,	"ERPp1SCM",	Int24ub),
	(31,	True,	"ERPp1HM",	Int24ub),

	(32,	True,	"ERPp1DSM",	Int24ub),
	(33,	False,	"DATE_ERNp1",	TYPE_DMYhms),
	(34,	True,	"ERNp1P",	Int24ub),
	(35,	True,	"ERNp1PM",	Int24ub),
	(36,	True,	"ERNp1HCE",	Int24ub),
	(37,	True,	"ERNp1HCH",	Int24ub),
	(38,	True,	"ERNp1HH",	Int24ub),
	(39,	True,	"ERNp1HCD",	Int24ub),
	
	(40,	True,	"ERNp1HD",	Int24ub),
	(41,	True,	"ERNp1JA",	Int24ub),
	(42,	True,	"ERNp1HPE",	Int24ub),
	(43,	True,	"ERNp1HPH",	Int24ub),
	(44,	True,	"ERNp1HPD",	Int24ub),
	(45,	True,	"ERNp1SCM",	Int24ub),
	(46,	True,	"ERNp1HM",	Int24ub),
	
	(47,	True,	"ERNp1DSM",	Int24ub)
]

TICDataICEGeneralFromBitfields = TIC_STDFieldRepeater(len(ICEGeneralFields), TIC_STDField(ICEGeneralFields,FindFieldBitField))
TICDataBatchICEGeneralFromFieldIndex = TIC_BatchType(FindFieldIndex,ICEGeneralFields)

TICDataICEpFromBitfields = TIC_STDFieldRepeater(len(ICEpFields), TIC_STDField(ICEpFields,FindFieldBitField))
TICDataICEp1FromBitfields = TIC_STDFieldRepeater(len(ICEp1Fields), TIC_STDField(ICEp1Fields,FindFieldBitField))
TICDataBatchICEpxFromFieldIndex = TIC_BatchType(FindFieldIndex,ICEp1Fields)
