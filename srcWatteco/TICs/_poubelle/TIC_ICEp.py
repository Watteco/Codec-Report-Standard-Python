# -*- coding: utf-8 -*-

# Pour passer de TICDataXXXFromBitfields @ TICDataBatchXXXFromFieldIndex
# Expressions régulière notepad++ 
# Find   : TICDataSelectorIfBit\( ([0-9]*), Struct\("([^\"]*)"\/([^\)]*).*
# Replace: \1 : \3, # \2

from ._TIC_Tools import *
from ._TIC_Types import *

TICDataICEpFromBitfields = Struct(
	TICDataSelectorIfBit( 0, Struct("DEBUTp"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 1, Struct("FINp"/TYPE_DMYhms)),
	TICDataSelectorIfBit( 2, Struct("CAFp"/Int16ub) ),
	TICDataSelectorIfBit( 3, Struct("DATE_EAp"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 4, Struct("EApP"/Int24ub) ),
	TICDataSelectorIfBit( 5, Struct("EApPM"/Int24ub) ),
	TICDataSelectorIfBit( 6, Struct("EApHCE"/Int24ub) ),
	TICDataSelectorIfBit( 7, Struct("EApHCH"/Int24ub) ),

	TICDataSelectorIfBit( 8, Struct("EApHH"/Int24ub) ),
	TICDataSelectorIfBit( 9, Struct("EApHCD"/Int24ub) ),
	TICDataSelectorIfBit( 10, Struct("EApHD"/Int24ub) ),
	TICDataSelectorIfBit( 11, Struct("EApJA"/Int24ub) ),
	TICDataSelectorIfBit( 12, Struct("EApHPE"/Int24ub) ),
	TICDataSelectorIfBit( 13, Struct("EApHPH"/Int24ub) ),
	TICDataSelectorIfBit( 14, Struct("EApHPD"/Int24ub) ),
	TICDataSelectorIfBit( 15, Struct("EApSCM"/Int24ub) ),

	TICDataSelectorIfBit( 16, Struct("EApHM"/Int24ub) ),
	TICDataSelectorIfBit( 17, Struct("EApDSM"/Int24ub) ),
	TICDataSelectorIfBit( 18, Struct("DATE_ERPp"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 19, Struct("ERPpP"/Int24ub) ),
	TICDataSelectorIfBit( 20, Struct("ERPpPM"/Int24ub) ),
	TICDataSelectorIfBit( 21, Struct("ERPpHCE"/Int24ub) ),
	TICDataSelectorIfBit( 22, Struct("ERPpHCH"/Int24ub) ),
	TICDataSelectorIfBit( 23, Struct("ERPpHH"/Int24ub) ),

	TICDataSelectorIfBit( 24, Struct("ERPpHCD"/Int24ub) ),
	TICDataSelectorIfBit( 25, Struct("ERPpHD"/Int24ub) ),
	TICDataSelectorIfBit( 26, Struct("ERPpJA"/Int24ub) ),
	TICDataSelectorIfBit( 27, Struct("ERPpHPE"/Int24ub) ),
	TICDataSelectorIfBit( 28, Struct("ERPpHPH"/Int24ub) ),
	TICDataSelectorIfBit( 29, Struct("ERPpHPD"/Int24ub) ),
	TICDataSelectorIfBit( 30, Struct("ERPpSCM"/Int24ub) ),
	TICDataSelectorIfBit( 31, Struct("ERPpHM"/Int24ub) ),

	TICDataSelectorIfBit( 32, Struct("ERPpDSM"/Int24ub) ),
	TICDataSelectorIfBit( 33, Struct("DATE_ERNp"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 34, Struct("ERNpP"/Int24ub) ),
	TICDataSelectorIfBit( 35, Struct("ERNpPM"/Int24ub) ),
	TICDataSelectorIfBit( 36, Struct("ERNpHCE"/Int24ub) ),
	TICDataSelectorIfBit( 37, Struct("ERNpHCH"/Int24ub) ),
	TICDataSelectorIfBit( 38, Struct("ERNpHH"/Int24ub) ),
	TICDataSelectorIfBit( 39, Struct("ERNpHCD"/Int24ub) ),
	
	TICDataSelectorIfBit( 40, Struct("ERNpHD"/Int24ub) ),
	TICDataSelectorIfBit( 41, Struct("ERNpJA"/Int24ub) ),
	TICDataSelectorIfBit( 42, Struct("ERNpHPE"/Int24ub) ),
	TICDataSelectorIfBit( 43, Struct("ERNpHPH"/Int24ub) ),
	TICDataSelectorIfBit( 44, Struct("ERNpHPD"/Int24ub) ),
	TICDataSelectorIfBit( 45, Struct("ERNpSCM"/Int24ub) ),
	TICDataSelectorIfBit( 46, Struct("ERNpHM"/Int24ub) ),
	
	TICDataSelectorIfBit( 47, Struct("ERNpDSM"/Int24ub) )
	
)

# NOTE: For Batch only scalar/numeric values are accepeted
TICDataBatchICEpFromFieldIndex = Switch( FindFieldIndex, 
	{
		#0 : TYPE_DMYhms, # DEBUTp
		#1 : TYPE_DMYhms, # FINp
		2 : Int16ub, # CAFp
		#3 : TYPE_DMYhms, # DATE_EAp
		4 : Int24ub, # EApP
		5 : Int24ub, # EApPM
		6 : Int24ub, # EApHCE
		7 : Int24ub, # EApHCH

		8 : Int24ub, # EApHH
		9 : Int24ub, # EApHCD
		10 : Int24ub, # EApHD
		11 : Int24ub, # EApJA
		12 : Int24ub, # EApHPE
		13 : Int24ub, # EApHPH
		14 : Int24ub, # EApHPD
		15 : Int24ub, # EApSCM

		16 : Int24ub, # EApHM
		17 : Int24ub, # EApDSM
		#18 : TYPE_DMYhms, # DATE_ERPp
		19 : Int24ub, # ERPpP
		20 : Int24ub, # ERPpPM
		21 : Int24ub, # ERPpHCE
		22 : Int24ub, # ERPpHCH
		23 : Int24ub, # ERPpHH

		24 : Int24ub, # ERPpHCD
		25 : Int24ub, # ERPpHD
		26 : Int24ub, # ERPpJA
		27 : Int24ub, # ERPpHPE
		28 : Int24ub, # ERPpHPH
		29 : Int24ub, # ERPpHPD
		30 : Int24ub, # ERPpSCM
		31 : Int24ub, # ERPpHM

		32 : Int24ub, # ERPpDSM
		#33 : TYPE_DMYhms, # DATE_ERNp
		34 : Int24ub, # ERNpP
		35 : Int24ub, # ERNpPM
		36 : Int24ub, # ERNpHCE
		37 : Int24ub, # ERNpHCH
		38 : Int24ub, # ERNpHH
		39 : Int24ub, # ERNpHCD
		
		40 : Int24ub, # ERNpHD
		41 : Int24ub, # ERNpJA
		42 : Int24ub, # ERNpHPE
		43 : Int24ub, # ERNpHPH
		44 : Int24ub, # ERNpHPD
		45 : Int24ub, # ERNpSCM
		46 : Int24ub, # ERNpHM
		
		47 : Int24ub, # ERNpDSM
		
	}, default = TICUnbatchableFieldError()
)


