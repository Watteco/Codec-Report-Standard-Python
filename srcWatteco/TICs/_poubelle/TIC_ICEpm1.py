# -*- coding: utf-8 -*-

# Pour passer de TICDataXXXFromBitfields @ TICDataBatchXXXFromFieldIndex
# Expressions régulière notepad++ 
# Find   : TICDataSelectorIfBit\( ([0-9]*), Struct\("([^\"]*)"\/([^\)]*).*
# Replace: \1 : \3, # \2

from ._TIC_Tools import *
from ._TIC_Types import *

TICDataICEpm1FromBitfields = Struct(
	TICDataSelectorIfBit( 0, Struct("DEBUTp1"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 1, Struct("FINp1"/TYPE_DMYhms)),
	TICDataSelectorIfBit( 2, Struct("CAFp1"/Int16ub) ),
	TICDataSelectorIfBit( 3, Struct("DATE_EAp1"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 4, Struct("EAp1P"/Int24ub) ),
	TICDataSelectorIfBit( 5, Struct("EAp1PM"/Int24ub) ),
	TICDataSelectorIfBit( 6, Struct("EAp1HCE"/Int24ub) ),
	TICDataSelectorIfBit( 7, Struct("EAp1HCH"/Int24ub) ),

	TICDataSelectorIfBit( 8, Struct("EAp1HH"/Int24ub) ),
	TICDataSelectorIfBit( 9, Struct("EAp1HCD"/Int24ub) ),
	TICDataSelectorIfBit( 10, Struct("EAp1HD"/Int24ub) ),
	TICDataSelectorIfBit( 11, Struct("EAp1JA"/Int24ub) ),
	TICDataSelectorIfBit( 12, Struct("EAp1HPE"/Int24ub) ),
	TICDataSelectorIfBit( 13, Struct("EAp1HPH"/Int24ub) ),
	TICDataSelectorIfBit( 14, Struct("EAp1HPD"/Int24ub) ),
	TICDataSelectorIfBit( 15, Struct("EAp1SCM"/Int24ub) ),

	TICDataSelectorIfBit( 16, Struct("EAp1HM"/Int24ub) ),
	TICDataSelectorIfBit( 17, Struct("EAp1DSM"/Int24ub) ),
	TICDataSelectorIfBit( 18, Struct("DATE_ERPp1"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 19, Struct("ERPp1P"/Int24ub) ),
	TICDataSelectorIfBit( 20, Struct("ERPp1PM"/Int24ub) ),
	TICDataSelectorIfBit( 21, Struct("ERPp1HCE"/Int24ub) ),
	TICDataSelectorIfBit( 22, Struct("ERPp1HCH"/Int24ub) ),
	TICDataSelectorIfBit( 23, Struct("ERPp1HH"/Int24ub) ),

	TICDataSelectorIfBit( 24, Struct("ERPp1HCD"/Int24ub) ),
	TICDataSelectorIfBit( 25, Struct("ERPp1HD"/Int24ub) ),
	TICDataSelectorIfBit( 26, Struct("ERPp1JA"/Int24ub) ),
	TICDataSelectorIfBit( 27, Struct("ERPp1HPE"/Int24ub) ),
	TICDataSelectorIfBit( 28, Struct("ERPp1HPH"/Int24ub) ),
	TICDataSelectorIfBit( 29, Struct("ERPp1HPD"/Int24ub) ),
	TICDataSelectorIfBit( 30, Struct("ERPp1SCM"/Int24ub) ),
	TICDataSelectorIfBit( 31, Struct("ERPp1HM"/Int24ub) ),

	TICDataSelectorIfBit( 32, Struct("ERPp1DSM"/Int24ub) ),
	TICDataSelectorIfBit( 33, Struct("DATE_ERNp1"/TYPE_DMYhms) ),
	TICDataSelectorIfBit( 34, Struct("ERNp1P"/Int24ub) ),
	TICDataSelectorIfBit( 35, Struct("ERNp1PM"/Int24ub) ),
	TICDataSelectorIfBit( 36, Struct("ERNp1HCE"/Int24ub) ),
	TICDataSelectorIfBit( 37, Struct("ERNp1HCH"/Int24ub) ),
	TICDataSelectorIfBit( 38, Struct("ERNp1HH"/Int24ub) ),
	TICDataSelectorIfBit( 39, Struct("ERNp1HCD"/Int24ub) ),
	
	TICDataSelectorIfBit( 40, Struct("ERNp1HD"/Int24ub) ),
	TICDataSelectorIfBit( 41, Struct("ERNp1JA"/Int24ub) ),
	TICDataSelectorIfBit( 42, Struct("ERNp1HPE"/Int24ub) ),
	TICDataSelectorIfBit( 43, Struct("ERNp1HPH"/Int24ub) ),
	TICDataSelectorIfBit( 44, Struct("ERNp1HPD"/Int24ub) ),
	TICDataSelectorIfBit( 45, Struct("ERNp1SCM"/Int24ub) ),
	TICDataSelectorIfBit( 46, Struct("ERNp1HM"/Int24ub) ),
	
	TICDataSelectorIfBit( 47, Struct("ERNp1DSM"/Int24ub) )
	
)

# NOTE: For Batch only scalar/numeric values are accepeted
TICDataBatchICEpm1FromFieldIndex = Switch( FindFieldIndex, 
	{
		#0 : TYPE_DMYhms, # DEBUTp1
		#1 : TYPE_DMYhms, # FINp1
		2 : Int16ub, # CAFp1
		#3 : TYPE_DMYhms, # DATE_EAp1
		4 : Int24ub, # EAp1P
		5 : Int24ub, # EAp1PM
		6 : Int24ub, # EAp1HCE
		7 : Int24ub, # EAp1HCH

		8 : Int24ub, # EAp1HH
		9 : Int24ub, # EAp1HCD
		10 : Int24ub, # EAp1HD
		11 : Int24ub, # EAp1JA
		12 : Int24ub, # EAp1HPE
		13 : Int24ub, # EAp1HPH
		14 : Int24ub, # EAp1HPD
		15 : Int24ub, # EAp1SCM

		16 : Int24ub, # EAp1HM
		17 : Int24ub, # EAp1DSM
		#18 : TYPE_DMYhms, # DATE_ERPp1
		19 : Int24ub, # ERPp1P
		20 : Int24ub, # ERPp1PM
		21 : Int24ub, # ERPp1HCE
		22 : Int24ub, # ERPp1HCH
		23 : Int24ub, # ERPp1HH

		24 : Int24ub, # ERPp1HCD
		25 : Int24ub, # ERPp1HD
		26 : Int24ub, # ERPp1JA
		27 : Int24ub, # ERPp1HPE
		28 : Int24ub, # ERPp1HPH
		29 : Int24ub, # ERPp1HPD
		30 : Int24ub, # ERPp1SCM
		31 : Int24ub, # ERPp1HM

		32 : Int24ub, # ERPp1DSM
		#33 : TYPE_DMYhms, # DATE_ERNp1
		34 : Int24ub, # ERNp1P
		35 : Int24ub, # ERNp1PM
		36 : Int24ub, # ERNp1HCE
		37 : Int24ub, # ERNp1HCH
		38 : Int24ub, # ERNp1HH
		39 : Int24ub, # ERNp1HCD
		
		40 : Int24ub, # ERNp1HD
		41 : Int24ub, # ERNp1JA
		42 : Int24ub, # ERNp1HPE
		43 : Int24ub, # ERNp1HPH
		44 : Int24ub, # ERNp1HPD
		45 : Int24ub, # ERNp1SCM
		46 : Int24ub, # ERNp1HM
		
		47 : Int24ub, # ERNp1DSM
		
	}, default = TICUnbatchableFieldError()
)


