# -*- coding: utf-8 -*-
from construct import *
from WTC_CodecTools import *
import sys

from binascii import hexlify,unhexlify
		
##### TIC Attribute ID #####################################
# Specific for TIC attribute: <Intance u8><Attribute ID u8>
TICAttributeID = IfStrStartWithElse(FindClusterID,"TIC_ICE",
	Enum (Int8ub,
		General = 0x00,
		ICEp    = 0x01,
		ICEpm1  = 0x02
	),
	Enum (Int8ub,
		General = 0x00
	)
)

OptionalTICAttributeInstance = Embedded (
	IfStrStartWithElse(FindClusterID,"TIC_",
		Struct (
			"Instance" / Int8ub
		),
		Pass
	)
)

##### TIC Descriptor header #####################################
class TICDescHeaderSizeAdapter(Adapter):
	# make specific EndPoint Encoding/Decoding
	def _encode(self, obj, context):
		assert ((obj >= 0) and (obj < 32))
		return ( 8 if (obj == 0) else obj )

	def _decode(self, obj, context):
		return ( 8 if (obj == 0) else obj )

TICDescHeaderSize = TICDescHeaderSizeAdapter(BitsInteger(5))

TICDescHeader = BitStruct(
	"Obsolete"     / Enum(Bit, Yes = 1 , No = 0),
	"Report"       / Enum(Bit, Standard = 0 , Decale = 1),
	"PresentField" / Enum(Bit, DescVarIndexes = 1 , DescVarBitfield = 0),
	"Size"         / TICDescHeaderSize,
)	

def _TICDescIndexesToBitsfield(InByteArray):
	# format input : list of int (indexes)
	# format output : array of bytes with bits set in position of indexes
	
	# return an empty bytearray if list is empty
	if not InByteArray: return bytearray()

	result = bytearray((max(InByteArray) // 8) + 1)
	
	for val in InByteArray:
		result[(val // 8)] |= 1 << (val % 8)
	return result[::-1]
	
def _TICDescBitsfieldToIndexes(InByteArray):
	# format input : array of bytes with bits set in position of indexes
	# format output : list of int (indexes)
	result = bytearray()
	numByte = 0;
	for val in InByteArray[::-1]:
		for numBit in range(8):
			if (val & (1<<numBit)):
				result.append((numByte * 8) + numBit)
		numByte = numByte + 1
	return result

def _ByteArrayTo01String(InByteArray):
	# format input : array of bytes with bits set in position of indexes
	# format output : list of int (indexes)
	result = ""
	numByte = 0;
	for val in InByteArray:
		for numBit in range(8):
			result = result + ("1" if (val & (1<<numBit)) else "0")
		numByte = numByte + 1
	return result
	
def _01StringToByteArray(InO1String):
	# format input : array of bytes with bits set in position of indexes
	# format output : list of int (indexes)
	result = bytearray()
	numByte = 0; numBit=0;
	for car in InO1String:
		if (numBit == 0) :
			result.append(0)
		if (car == "1") :
			result[numByte] |= 1 << numBit
		numBit = numBit + 1
		if (numBit == 8):
			numBit = 0
			numByte = numByte + 1
			
	return result	
		
class TICDescBitsFieldAdapter(Adapter):
	# Revert bitfield to process in growing order from b0 to bn
	def _encode(self, obj, context):
		return ( (_01StringToByteArray(obj))[::-1] )

	def _decode(self, obj, context):
		return ( _ByteArrayTo01String(obj[::-1]) )
		
				
class TICDescIndexesAdapter(Adapter):
	# Revert bitfield to process in growing order from b0 to bn
	def _encode(self, obj, context):
		
		res = _TICDescBitsfieldToIndexes((_01StringToByteArray(obj))[::-1])
		return ( res )

	def _decode(self, obj, context):
		res = _TICDescIndexesToBitsfield(obj)
		return ( _ByteArrayTo01String(res[::-1]) )
 

##### TIC Fields and Selector #####################################	
TICFieldsSelector = Struct(
	"DescHeader" / TICDescHeader,
	Embedded( IfThenElse (this.DescHeader.PresentField == "DescVarBitfield", 
			Struct("BitField" / TICDescBitsFieldAdapter(Bytes(this._.DescHeader.Size - 1))),
			Struct("BitField" / TICDescIndexesAdapter(Bytes(this._.DescHeader.Size - 1)))
	))
 )

#_TICdata_ Must always be associated (prepend) by a TICDataSelector Struct 
# Notice that the lamda verify that :
# - bit is set to "1"
# - if tested bit not over number of char String bitfield Index
def _isSelectedBit(ctx, BitNum):
	print("====>")
	if ( BitNum >= len(ctx._.TICDataSelector.BitField) ): return False
	if (ctx._.TICDataSelector.BitField[BitNum] == "1"): return  True
	else: return False
	
def TICDataSelectorIfBit(BitNum, thensubcon):
	return Embedded( 
		Switch(
			lambda 
				ctx: (ctx._.TICDataSelector.BitField[BitNum] == "1")  \
				if ( BitNum < len(ctx._.TICDataSelector.BitField) ) \
				else False,
			{
			   True : thensubcon,
			}, default = Pass
		)
	)
	
''' Test for more "autodefined format" (cf TIC_ICE.py)
def TICDataSelectorIfBitTest(BitNum, Name, Type):
	return Embedded( Switch(
		lambda 
			ctx: (ctx._.TICDataSelector.BitField[BitNum] == "1")  \
			if ( BitNum < len(ctx._.TICDataSelector.BitField) ) \
			else False,
		{
		   True : Struct(('ID_%03d' % BitNum) / Struct("Name"/Computed(Name), "Type" /Computed(str(Type)), "Value"/Type)),
		}, default = Pass
	))
'''
 
# COULD define many explicit errors to get construct errors more explicits ;O)) !

class TICUnbatchableFieldError(Construct):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.flagbuildnone = True
	def _parse(self, stream, context, path):
		raise ExplicitError("%s : field %d not batchable !" % (FindClusterID(context), FindFieldIndex(context)))
	def _build(self, obj, stream, context, path):
		raise ExplicitError("%s : field %d not batchable !" % (FindClusterID(context), FindFieldIndex(context)))


#############################################################################
#
# Following are experimental based on array of Tuple of TIC field definition
# [(<Fid>,<Batchable>,<Label>,<Type/SubCons>
#
# ==>  TIC STD Field constructor 
#      Repeater for TIC field constructor
#
# ==>  Type Finder based on Field index
#   
#
#############################################################################

def TICIsAttrPresent(context):
	if (hasattr(context._,"TICReportSelector")):
		if ((context._FieldIndex_) < len(context._.TICReportSelector.BitField)):
			if (context._.TICReportSelector.BitField[context._FieldIndex_] == "1"):
				return True
	if (hasattr(context._,"TICDataSelector")):
		if ((context._FieldIndex_) < len(context._.TICDataSelector.BitField)):
			if (context._.TICDataSelector.BitField[context._FieldIndex_] == "1"):
				return True
	return False


def TICAttr(context, subcon):
	_rptsel = _data = "No"
	if (hasattr(context._,"TICReportSelector")):
		if ((context._FieldIndex_) < len(context._.TICReportSelector.BitField)):
			if (context._.TICReportSelector.BitField[context._FieldIndex_] == "1"):
				_rptsel = "Yes"
	if (hasattr(context._,"TICDataSelector")):
		if ((context._FieldIndex_) < len(context._.TICDataSelector.BitField)):
			if (context._.TICDataSelector.BitField[context._FieldIndex_] == "1"):
				_data = "Yes"

	# Analyse les cas ou les attributs "IsReported", "IsCriteria" et "Value" doivent être présents dans l'objet du champ concerné'
	if (_data == "Yes"):
		if (hasattr(context._,"TICReportSelector")):
			return Struct( "IsReported"/Computed(_rptsel), "IsCriteria"/Computed(_data),"Value"/subcon)
		else:
			return Struct( "Value"/subcon)
	else:
		if (hasattr(context._,"TICReportSelector")):
			if (_rptsel == "Yes"):
				return Struct( "IsReported"/Computed(_rptsel), "IsCriteria"/Computed(_data))

def TICBestDesc(HeaderByte, DescVarIndexes):

	nbFields = len(DescVarIndexes)
	# print("A: nbFields = %s" % nbFields)
	
	HeaderByte &= ~(0x3F) # Clear (b5 : 0 VarBitField ) and (b0-b4: size)

	if (nbFields > 0):
		lastIndex = DescVarIndexes[nbFields-1]
		nbBits = lastIndex + 1
		nbBytes = int(nbBits / 8) + (0 if (nbBits % 8 == 0) else 1)
		if ((nbBytes < nbFields) ) :
			DescVarBitsField = bytearray([0] * nbBytes) 
			for i in range(0,nbFields):
				fieldIndex = DescVarIndexes[i]
				byteIndex = int(nbBytes - 1 - int(fieldIndex / 8))
				bitPos = fieldIndex % 8
				DescVarBitsField[byteIndex] |= (1 << bitPos)
			HeaderByte |= ((nbBytes + 1) & 0x1F) # Set Size
			DescVarBitsField = HeaderByte.to_bytes(1) + DescVarBitsField
			#print("B: DescVarBitsField = %s" % hexlify(DescVarBitsField))
			return DescVarBitsField
		else:
			HeaderByte |= (0x01 << 5) # b5 : 1 VarIndexes
			HeaderByte |= ((nbFields + 1) & 0x1F) # Set Size
			DescVarIndexes = HeaderByte.to_bytes(1) + DescVarIndexes
			#print("B: DescVarIndexes = %s" % hexlify(DescVarIndexes))
			return DescVarIndexes
	else:
		HeaderByte |= (0x01 << 5) # b5 : 1 VarIndexes
		HeaderByte |= (0x01) # Set Size
		DescVarIndexes = HeaderByte.to_bytes(1) + DescVarIndexes
		return DescVarIndexes

class TIC_STDField(Construct):

	__slots__ = ["subcons","TICFieldDescArray","BitField"]
	def __init__(self, TICFieldDescArray, BitField):
		super(TIC_STDField, self).__init__()
		self.TICFieldDescArray = TICFieldDescArray
		self.BitField = BitField

	def _parse(self, stream, context, path):
		if hasattr(context,"_FieldIndex_"):	
			context._FieldIndex_ += 1
		else: 
			context._FieldIndex_ = 0
			# Get eventual parameter for filed parsing
			context.meterVersion = GetValueFromKeyLookUP(context, 'meterVersion')

		#print("A: Context._ = %s" % context._)
		#bf = self.BitField(context)

		if (not(TICIsAttrPresent(context))): return Pass._parse(stream, context, path)
		
		key = self.TICFieldDescArray[context._FieldIndex_][2]

		if (context.meterVersion != ''):
			if (len(self.TICFieldDescArray[context._FieldIndex_]) > 4):
				if (self.TICFieldDescArray[context._FieldIndex_][4] != context.meterVersion):
					raise ExplicitError("%s : field '%s (index %d)' not compatible with meterVersion %s  !" % (FindClusterID(context), key, context._FieldIndex_,context.meterVersion ))
				
		obj = TICAttr(context,self.TICFieldDescArray[context._FieldIndex_][3])._parse(stream, context, path)
		return (key,obj) 

	def _build(self, obj, stream, context, path):
		if hasattr(context,"_FieldIndex_"):	
			context._FieldIndex_ += 1
		else: 
			# Init on first Index parsing of meter field list table
			context._FieldIndex_ = 0
			# Get eventual parameter for filed parsing
			context.meterVersion = GetValueFromKeyLookUP(context, 'meterVersion')
			# Set commandID once
			context._theCommandID = FindCommandID(context)
			# Before truncating existing descriptors, get descriptors header templates from already build stream
			b = stream.getvalue()
			#print ("stream.getvalue()    : %s", hexlify(b))
			if ((context._theCommandID == "ConfigureReporting" ) or (context._theCommandID == "ReadReportingConfigurationResponse")):
				context.RptSelHeader=b[0:((b[0]&0x1F))]
				context.DataSelHeader=b[((b[0]&0x1F)):]
				#print ("context.RptSelHeader : %s" % hexlify(context.RptSelHeader))
			else:
				context.RptSelHeader=''
				context.DataSelHeader=b[0:((b[0]&0x1F))]
			#print ("context.DataSelHeader: %s" % hexlify(context.DataSelHeader))
			# Truncate current TIC data header as it may be changed according to beter decsriptor selection
			stream.truncate(0)
			stream.seek(0)
			# Init 
			context.RptSelDescVarIndexes = bytearray([0] * 0) 
			context.DataDescVarIndexes = bytearray([0] * 0) 

		# Find fieldIndex in TIC data
		key = self.TICFieldDescArray[context._FieldIndex_][2]
		
		doNotProcess = False
		if (context.meterVersion != ''):
			if (len(self.TICFieldDescArray[context._FieldIndex_]) > 4):
				if (self.TICFieldDescArray[context._FieldIndex_][4] != context.meterVersion):
					doNotProcess = True

		if ((not doNotProcess) and (key in obj)):
			# Manages some JSON explicit errors in TIC fields
			if ((context._theCommandID == "ConfigureReporting" ) or (context._theCommandID == "ReadReportingConfigurationResponse")):
				if (not(("IsReported" in obj[key]) and ("IsCriteria" in obj[key]))):
					raise ExplicitError("%s : field '%s' must define 'IsReported' and 'IsCriteria' attributes  !" % (FindClusterID(context), key))
				if ((obj[key]["IsCriteria"] == "Yes") and not("Value" in obj[key])):
					raise ExplicitError("%s : field '%s' must define 'Value' when 'IsCriteria' = 'Yes'  !" % (FindClusterID(context), key))
			else:
				if (not("Value" in obj[key])):
					raise ExplicitError("%s : field '%s' must define 'Value'  !" % (FindClusterID(context), key))

			if ("Value" in obj[key]):
				# If data field required "Value" is present it has to be built and set in dataIndexes
				context.DataDescVarIndexes += context._FieldIndex_.to_bytes(1)
				self.TICFieldDescArray[context._FieldIndex_][3]._build(obj[key]["Value"], stream, context, path)
			
			if ("IsReported" in obj[key]):
				if (obj[key]["IsReported"] == "Yes") :
					context.RptSelDescVarIndexes += context._FieldIndex_.to_bytes(1)

		# If end of meter field list
		# Build the VarBitfield descriptors they'll have to be used if shorter than VarIndexes
		if (context._FieldIndex_ + 1 >= len(self.TICFieldDescArray)) : 
			# print("A: buffer   = %s" % hexlify(stream.getvalue()))

			# Now rebuild current stream context to prefixe the buffer with the descriptor
			b = stream.getvalue()
			stream.seek(0)
			stream.truncate(0)
			if ((context._theCommandID == "ConfigureReporting" ) or (context._theCommandID == "ReadReportingConfigurationResponse")):
				stream.write(TICBestDesc(context.RptSelHeader[0], context.RptSelDescVarIndexes))
			stream.write(TICBestDesc(context.DataSelHeader[0],context.DataDescVarIndexes))
			stream.write(b)

	def _sizeof(self, context, path):
		raise SizeofError("size calculaton maybe impossible")



class TIC_STDFieldRepeater(Construct):
	__slots__ = ["nb","subcon"]
	
	def __init__(self, nb, subcon):
		super(TIC_STDFieldRepeater, self).__init__()
		self.subcon = subcon
		self.nb = nb
		
	def _parse(self, stream, context, path):
		nb = self.nb(context) if callable(self.nb) else self.nb
		if not 0 <=nb <= sys.maxsize:
			raise RangeError("unsane nb %s " % nb)
		obj = Container()
		context = Container(_ = context)
		for i in range(0,nb):
			try:
				sc = self.subcon
				subobj = sc._parse(stream, context, path)
				if subobj is not None:
					obj[subobj[0]] = subobj[1]
					context[subobj[0]] = subobj[1]
			except StopIteration:
				break
		return obj
		
	def _build(self, obj, stream, context, path):
		nb = self.nb(context) if callable(self.nb) else self.nb
		if not 0 <=nb <= sys.maxsize:
			raise RangeError("unsane nb %s " % nb)
		context = Container(_ = context)
		context.update(obj)
		for i in range(0,nb):
			try:
				sc = self.subcon
				buildret = sc._build(obj, stream, context, path)
			except StopIteration:
				break
		return context
	def _sizeof(self, context, path):
		raise SizeofError("size calculaton maybe impossible")

class TIC_BatchType(Construct):
	__slots__ = ["subcons", "fifunc","TICFieldDescArray"]
	def __init__(self, fifunc, TICFieldDescArray):
		super(TIC_BatchType, self).__init__()
		self.fifunc = fifunc
		self.TICFieldDescArray = TICFieldDescArray

	def _parse(self, stream, context, path):
		FieldIndex = self.fifunc(context) if callable(self.fifunc) else self.fifunc
		if not 0 <= FieldIndex < len(self.TICFieldDescArray):
			raise RangeError("unsane FieldIndex %s " % FieldIndex)
		if not self.TICFieldDescArray[FieldIndex][1]:
			raise ExplicitError("%s : field %d not batchable !" % (FindClusterID(context), FindFieldIndex(context)))
		obj = self.TICFieldDescArray[FieldIndex][3]._parse(stream, context, path)
		return obj

	def _build(self, obj, stream, context, path):
		FieldIndex = self.fifunc(context) if callable(self.fifunc) else self.fifunc
		if not 0 <= FieldIndex < len(self.TICFieldDescArray): 
			raise RangeError("unsane FieldIndex %s " % FieldIndex)
		if not self.TICFieldDescArray[FieldIndex][1]:
			raise ExplicitError("%s : field %d not batchable !" % (FindClusterID(context), FindFieldIndex(context)))
		self.TICFieldDescArray[FieldIndex][3]._build(obj, stream, context, path)

	def _sizeof(self, context, path):
		try:
			FieldIndex = self.fifunc(context) if callable(self.fifunc) else self.fifunc
			if not 0 <= FieldIndex < len(self.TICFieldDescArray): 
				raise RangeError("unsane FieldIndex %s " % nb)
			if not self.TICFieldDescArray[FieldIndex][1]:
				raise ExplicitError("%s : field %d not batchable !" % (FindClusterID(context), FindFieldIndex(context)))
			sc = self.TICFieldDescArray[FieldIndex][3]
			return sc._sizeof(context, path)
		except (KeyError, AttributeError):
			raise SizeofError("cannot calculate size, index not found")
