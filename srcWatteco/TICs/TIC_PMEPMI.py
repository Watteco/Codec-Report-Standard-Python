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

PMEPMIFields = [
	( 0,	False,	"TRAME",	TYPE_E_DIV),
	( 1,	False,	"ADS",	Prefixed(Int8ub,BytesTostrHexClass(Bytes(6)))),
	( 2,	False,	"MESURES1",	TYPE_E_CONTRAT),
	( 3,	False,	"DATE",	TYPE_DMYhms),
	( 4,	True,	"EA_s",	Int24ub),
	( 5,	True,	"ERp_s",	Int24ub),
	( 6,	True,	"ERm_s",	Int24ub),
	( 7,	True,	"EAPP_s",	Int24ub),

	( 8,	True,	"EA_i",	Int24ub),
	( 9,	True,	"ERp_i",	Int24ub),
	(10,	True,	"ERm_i",	Int24ub),
	(11,	True,	"EAPP_i",	Int24ub),
	(12,	False,	"PTCOUR1",	TYPE_E_PT),
	(13,	False,	"TARIFDYN",	TYPE_E_DIV),
	(14,	False,	"ETATDYN1",	TYPE_E_PT),
	(15,	False,	"PREAVIS1",	TYPE_E_PT),

	(16,	False,	"TDYN1CD",	TYPE_tsDMYhms_E_PT),
	(17,	False,	"TDYN1CF",	TYPE_tsDMYhms_E_PT),
	(18,	False,	"TDYN1FD",	TYPE_tsDMYhms_E_PT),
	(19,	False,	"TDYN1FF",	TYPE_tsDMYhms_E_PT),
	(20,	False,	"MODE",	TYPE_E_DIV),
	(21,	False,	"CONFIG",	TYPE_E_DIV),
	(22,	False,	"DATEPA1",	TYPE_DMYhms),
	(23,	True,	"PA1_s",	Int16ub),

	(24,	True,	"PA1_i",	Int16ub),
	(25,	True,	"DATEPA2",	TYPE_tsDMYhms),
	(26,	True,	"PA2_s",	Int16ub),
	(27,	True,	"PA2_i",	Int16ub),
	(28,	True,	"DATEPA3",	TYPE_tsDMYhms),
	(29,	True,	"PA3_s",	Int16ub),
	(30,	True,	"PA3_i",	Int16ub),
	(31,	True,	"DATEPA4",	TYPE_tsDMYhms),

	(32,	True,	"PA4_s",	Int16ub),
	(33,	True,	"PA4_i",	Int16ub),
	(34,	True,	"DATEPA5",	TYPE_tsDMYhms),
	(35,	True,	"PA5_s",	Int16ub),
	(36,	True,	"PA5_i",	Int16ub),
	(37,	True,	"DATEPA6",	TYPE_tsDMYhms),
	(38,	True,	"PA6_s",	Int16ub),
	(39,	True,	"PA6_i",	Int16ub),
	
	(40,	True,	"DebP",	TYPE_tsDMYhms),
	(41,	True,	"EAP_s",	Int24ub),
	(42,	True,	"EAP_i",	Int24ub),
	(43,	True,	"ERpP_s",	Int24ub),
	(44,	True,	"ERmP_s",	Int24ub),
	(45,	True,	"ERpP_i",	Int24ub),
	(46,	True,	"ERmP_i",	Int24ub),
	(47,	True,	"DebPm1",	TYPE_tsDMYhms),

	(48,	True,	"FinPm1",	TYPE_tsDMYhms),
	(49,	True,	"EaPm1_s",	Int24ub),
	(50,	True,	"EaPm1_i",	Int24ub),
	(51,	True,	"ERpPm1_s",	Int24ub),
	(52,	True,	"ERmPm1_s",	Int24ub),
	(53,	True,	"ERpPm1_i",	Int24ub),
	(54,	True,	"ERmPm1_i",	Int24ub),
	(55,	True,	"PS",	TYPE_U24_E_DIV),

	(56,	False,	"PREAVIS",	TYPE_E_DIV),
	(57,	True,	"PA1MN",	Int16ub),
	(58,	False,	"PMAX_s",	TYPE_U24_E_DIV),
	(59,	False,	"PMAX_i",	TYPE_U24_E_DIV),
	(60,	True,	"TGPHI_s",	Float32b),
	(61,	True,	"TGPHI_i",	Float32b),
	(62,	False,	"MESURES2",	TYPE_E_CONTRAT),
	(63,	False,	"PTCOUR2",	TYPE_E_PT),

	(64,	False,	"ETATDYN2",	TYPE_E_PT),
	(65,	False,	"PREAVIS2",	TYPE_E_PT),
	(66,	False,	"TDYN2CD",	TYPE_tsDMYhms_E_PT),
	(67,	False,	"TDYN2CF",	TYPE_tsDMYhms_E_PT),
	(68,	False,	"TDYN2FD",	TYPE_tsDMYhms_E_PT),
	(69,	False,	"TDYN2FF",  TYPE_tsDMYhms_E_PT),
	(70,	False,	"DebP_2",	TYPE_DMYhms),
	(71,	True,	"EaP_s2",	Int24ub),
	
	(72,	True,	"DebPm1_2",	TYPE_tsDMYhms),
	(73,	True,	"FinPm1_2",	TYPE_tsDMYhms),
	(74,	True,	"EaPm1_s2",	Int24ub),
	(75,	True,	"_DDEPMES1_",	Int24ub)
]
		
TICDataPMEPMIFromBitfields = TIC_STDFieldRepeater(len(PMEPMIFields), TIC_STDField(PMEPMIFields,FindFieldBitField))
TICDataBatchPMEPMIFromFieldIndex = TIC_BatchType(FindFieldIndex,PMEPMIFields)
