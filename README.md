# Codec-Python

ENGLISH
--------------
--------------


Pre-requesite:
--------------

Need Python 3.6 or Upper

. install dicctoxml:
	- go to dicttoxml-1.7.4/
	- command to execute: py setup.py install
	
. install construct:
	- go to construct-2.8.12/
	- command to execute: py setup.py install

Could also be installed with pip:
	- pip install dicttoxml==1.7.4 
	- pip install construct==2.8.12 

Run the decoding:
-----------------
. Go to srcWatteco/
. To decode a frame in xmll: echo 11... | py Main.py -of xmlp
. To decode a frame in json: echo 11... | py Main.py -of json

Run the encoding:
-----------------
. Go to srcWatteco/
. To encode a json in frame : echo {"EndPoint": 0, ...} | py Main.py -m e


Exemples:
---------
1. decode NodePowerDescriptor in json:

> echo 110a005000064107010536d80e4e01a059022ee0000001 | py Main.py -of json

{"version": "WATTECO_Frame_Codec_v_1.0", "TimeStamp": "2018-05-14 09:35:36.186645"}
{
 "FrameCtrl": {
  "EndPoint": 0,
  "Report": "Standard"
 },
 "CommandID": "ReportAttributes",
 "ClusterID": "Configuration",
 "AttributeID": "NodePowerDescriptor",
 "AttributeType": "ByteString",
 "Data": {
  "CurrentPowerMode": "PeriodicallyON",
  "AvailablePowerSourceBitField": 5,
  "ConstantVoltage": 14040,
  "DisposableBatteryVoltage": 3662,
  "CurrentPowerSource": "Constant"
 }
}

2. decode Temperature in xmlp:

> echo 110a04020000290A25 | py Main.py -of xmlp

<?xml version="1.0" ?>
<WATTECO_Frame_Codec_v_1.0>
        <FrameCtrl type="dict">
                <EndPoint type="int">0</EndPoint>
                <Report type="str">Standard</Report>
        </FrameCtrl>
        <CommandID type="str">ReportAttributes</CommandID>
        <ClusterID type="str">Temperature</ClusterID>
        <AttributeID type="str">MeasuredValue</AttributeID>
        <AttributeType type="str">Int16</AttributeType>
        <Data type="int">2597</Data>
</WATTECO_Frame_Codec_v_1.0>





Trame exemple:

1. report Alarme with Long cause Binary Input Count
118a000f0402230000000aa0d00000000a0000000001

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ReportAttributesAlarm",
 "ClusterID": "BinaryInput",
 "AttributeID": "Count",
 "AttributeType": "UInt32",
 "Data": 10,
 "Cause": [
  {
   "ReportParameters": {
    "New": "Yes",
    "Reserved": 0,
    "CauseRequest": "Long",
    "SecuredIfAlarm": "No",
    "Secured": "No",
    "NoHeaderPort": "No",
    "Batch": "No"
   },
   "SlotDescriptors": [
    {
     "CriteriaSlotDescriptor": {
      "Alarm": "Yes",
      "OnExceed": "Yes",
      "OnFall": "No",
      "Mode": "Threshold",
      "CriterionIndex": 0
     },
     "Value": 10,
     "Gap": 0,
     "Occurence": {
      "ExtendedOccurences": "No",
      "Occurences": 1
     }
    }
   ]
  }
 ]
}

2. report woth Long cause Node descriptor
110a005000064107010536d80e4e01a059022ee0000001

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ReportAttributes",
 "ClusterID": "Configuration",
 "AttributeID": "NodePowerDescriptor",
 "AttributeType": "ByteString",
 "Data": {
  "CurrentPowerMode": "PeriodicallyON",
  "AvailablePowerSourceBitField": 5,
  "ConstantVoltage": 14040,
  "DisposableBatteryVoltage": 3662,
  "CurrentPowerSource": "Constant"
 },
 "Cause": [
  {
   "ReportParameters": {
    "New": "Yes",
    "Reserved": 0,
    "CauseRequest": "Long",
    "SecuredIfAlarm": "No",
    "Secured": "No",
    "NoHeaderPort": "No",
    "Batch": "No"
   },
   "SlotDescriptors": [
    {
     "CriteriaSlotDescriptor": {
      "Alarm": "No",
      "OnExceed": "Yes",
      "OnFall": "No",
      "Mode": "ThresholdWithActions",
      "CriterionIndex": 1
     },
     "FieldIndex": 2,
     "Value": 12000,
     "Gap": 0,
     "Occurence": {
      "ExtendedOccurences": "No",
      "Occurences": 1
     }
    }
   ]
  }
 ]
}

3. read reporting configuration
1108000f000055

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ReadReportingConfiguration",
 "ClusterID": "BinaryInput",
 "ReportParameters": {
  "New": "No",
  "Reserved": 0,
  "CauseRequest": "No",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "PresentValue"
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ReadReportingConfiguration", "ClusterID": "BinaryInput", "ReportParameters": {"New": "No", "Reserved": 0, "CauseRequest": "No", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "PresentValue"}


4. Read attribut req
1100000f0055

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ReadAttribute",
 "ClusterID": "BinaryInput",
 "AttributeID": "PresentValue"
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ReadAttribute", "ClusterID": "BinaryInput", "AttributeID": "PresentValue"}

5. Configure reporting
5106000f000402238001800a01020304


{
 "EndPoint": 2,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "BinaryInput",
 "ReportParameters": {
  "New": "No",
  "Reserved": 0,
  "CauseRequest": "No",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "Count",
 "AttributeType": "UInt32",
 "MinReport": {
  "Unit": "Minutes",
  "Value": 1
 },
 "MaxReport": {
  "Unit": "Minutes",
  "Value": 10
 },
 "Data": 16909060
}
=>To use in encoding: {"EndPoint": 2, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "BinaryInput", "ReportParameters": {"New": "No", "Reserved": 0, "CauseRequest": "No", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "Count", "AttributeType": "UInt32", "MinReport": {"Unit": "Minutes", "Value": 1}, "MaxReport": {"Unit": "Minutes", "Value": 10}, "Data": 16909060}

6. Configure Binary Input reporting cause long + alarme
1106000fA004022300008001D00000000a0000000001

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "BinaryInput",
 "ReportParameters": {
  "New": "Yes",
  "Reserved": 0,
  "CauseRequest": "Long",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "Count",
 "AttributeType": "UInt32",
 "MinReport": {
  "Unit": "Seconds",
  "Value": 0
 },
 "MaxReport": {
  "Unit": "Minutes",
  "Value": 1
 },
 "Cause": [
  {
   "CriteriaSlotDescriptor": {
    "Alarm": "Yes",
    "OnExceed": "Yes",
    "OnFall": "No",
    "Mode": "Threshold",
    "CriterionIndex": 0
   },
   "Value": 10,
   "Gap": 0,
   "Occurence": {
    "ExtendedOccurences": "No",
    "Occurences": 1
   }
  }
 ],
 "Data": null
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "BinaryInput", "ReportParameters": {"New": "Yes", "Reserved": 0, "CauseRequest": "Long", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "Count", "AttributeType": "UInt32", "MinReport": {"Unit": "Seconds", "Value": 0}, "MaxReport": {"Unit": "Minutes", "Value": 1}, "Cause": [{"CriteriaSlotDescriptor": {"Alarm": "Yes", "OnExceed": "Yes", "OnFall": "No", "Mode": "Threshold", "CriterionIndex": 0}, "Value": 10, "Gap": 0, "Occurence": {"ExtendedOccurences": "No", "Occurences": 1}}], "Data": null}

7. Conf rep cause long + node descriptor + action
11060050A0000641000580011838022ee00000010600000001000259022ee0000001020003

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "Configuration",
 "ReportParameters": {
  "New": "Yes",
  "Reserved": 0,
  "CauseRequest": "Long",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "NodePowerDescriptor",
 "AttributeType": "ByteString",
 "MinReport": {
  "Unit": "Seconds",
  "Value": 5
 },
 "MaxReport": {
  "Unit": "Minutes",
  "Value": 1
 },
 "Size": 24,
 "Cause": [
  {
   "CriteriaSlotDescriptor": {
    "Alarm": "No",
    "OnExceed": "No",
    "OnFall": "Yes",
    "Mode": "ThresholdWithActions",
    "CriterionIndex": 0
   },
   "FieldIndex": 2,
   "Value": 12000,
   "Gap": 0,
   "Occurence": {
    "ExtendedOccurences": "No",
    "Occurences": 1
   },
   "Actions": {
    "ActDesc": {
     "SendingOfreport": "Yes",
     "Size": 6
    },
    "Action": [
     0,
     0,
     0,
     1,
     0,
     2
    ]
   }
  },
  {
   "CriteriaSlotDescriptor": {
    "Alarm": "No",
    "OnExceed": "Yes",
    "OnFall": "No",
    "Mode": "ThresholdWithActions",
    "CriterionIndex": 1
   },
   "FieldIndex": 2,
   "Value": 12000,
   "Gap": 0,
   "Occurence": {
    "ExtendedOccurences": "No",
    "Occurences": 1
   },
   "Actions": {
    "ActDesc": {
     "SendingOfreport": "Yes",
     "Size": 2
    },
    "Action": [
     0,
     3
    ]
   }
  }
 ],
 "Data": null
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "Configuration", "ReportParameters": {"New": "Yes", "Reserved": 0, "CauseRequest": "Long", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "NodePowerDescriptor", "AttributeType": "ByteString", "MinReport": {"Unit": "Seconds", "Value": 5}, "MaxReport": {"Unit": "Minutes", "Value": 1}, "Size": 24, "Cause": [{"CriteriaSlotDescriptor": {"Alarm": "No", "OnExceed": "No", "OnFall": "Yes", "Mode": "ThresholdWithActions", "CriterionIndex": 0}, "FieldIndex": 2, "Value": 12000, "Gap": 0, "Occurence": {"ExtendedOccurences": "No", "Occurences": 1}, "Actions": {"ActDesc": {"SendingOfreport": "Yes", "Size": 6}, "Action": [0, 0, 0, 1, 0, 2]}}, {"CriteriaSlotDescriptor": {"Alarm": "No", "OnExceed": "Yes", "OnFall": "No", "Mode": "ThresholdWithActions", "CriterionIndex": 1}, "FieldIndex": 2, "Value": 12000, "Gap": 0, "Occurence": {"ExtendedOccurences": "No", "Occurences": 1}, "Actions": {"ActDesc": {"SendingOfreport": "Yes", "Size": 2}, "Action": [0, 3]}}], "Data": null}

8. Conf rep cause long + node descriptor  
11060050A0000641000580011830022ee000000151022ee0000001

{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "Configuration",
 "ReportParameters": {
  "New": "Yes",
  "Reserved": 0,
  "CauseRequest": "Long",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "NodePowerDescriptor",
 "AttributeType": "ByteString",
 "MinReport": {
  "Unit": "Seconds",
  "Value": 5
 },
 "MaxReport": {
  "Unit": "Minutes",
  "Value": 1
 },
 "Size": 24,
 "Cause": [
  {
   "CriteriaSlotDescriptor": {
    "Alarm": "No",
    "OnExceed": "No",
    "OnFall": "Yes",
    "Mode": "Threshold",
    "CriterionIndex": 0
   },
   "FieldIndex": 2,
   "Value": 12000,
   "Gap": 0,
   "Occurence": {
    "ExtendedOccurences": "No",
    "Occurences": 1
   }
  },
  {
   "CriteriaSlotDescriptor": {
    "Alarm": "No",
    "OnExceed": "Yes",
    "OnFall": "No",
    "Mode": "Threshold",
    "CriterionIndex": 1
   },
   "FieldIndex": 2,
   "Value": 12000,
   "Gap": 0,
   "Occurence": {
    "ExtendedOccurences": "No",
    "Occurences": 1
   }
  }
 ],
 "Data": null
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "Configuration", "ReportParameters": {"New": "Yes", "Reserved": 0, "CauseRequest": "Long", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "NodePowerDescriptor", "AttributeType": "ByteString", "MinReport": {"Unit": "Seconds", "Value": 5}, "MaxReport": {"Unit": "Minutes", "Value": 1}, "Size": 24, "Cause": [{"CriteriaSlotDescriptor": {"Alarm": "No", "OnExceed": "No", "OnFall": "Yes", "Mode": "Threshold", "CriterionIndex": 0}, "FieldIndex": 2, "Value": 12000, "Gap": 0, "Occurence": {"ExtendedOccurences": "No", "Occurences": 1}}, {"CriteriaSlotDescriptor": {"Alarm": "No", "OnExceed": "Yes", "OnFall": "No", "Mode": "Threshold", "CriterionIndex": 1}, "FieldIndex": 2, "Value": 12000, "Gap": 0, "Occurence": {"ExtendedOccurences": "No", "Occurences": 1}}], "Data": null}


9. Conf Node descriptor Disposable Battery voltage
1106005000000641000aa76005000400c800
{
 "EndPoint": 0,
 "Report": "Standard",
 "CommandID": "ConfigureReporting",
 "ClusterID": "Configuration",
 "ReportParameters": {
  "New": "No",
  "Reserved": 0,
  "CauseRequest": "No",
  "SecuredIfAlarm": "No",
  "Secured": "No",
  "NoHeaderPort": "No",
  "Batch": "No"
 },
 "AttributeID": "NodePowerDescriptor",
 "AttributeType": "ByteString",
 "MinReport": {
  "Unit": "Seconds",
  "Value": 10
 },
 "MaxReport": {
  "Unit": "Minutes",
  "Value": 10080
 },
 "Data": {
  "Size": 5,
  "CurrentPowerMode": "ONWhenIdle",
  "AvailablePowerSourceBitField": 4,
  "DisposableBatteryVoltage": 200,
  "CurrentPowerSource": "No"
 }
}

=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "Configuration", "ReportParameters": {"New": "No", "Reserved": 0, "CauseRequest": "No", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "NodePowerDescriptor", "AttributeType": "ByteString", "MinReport": {"Unit": "Seconds", "Value": 10}, "MaxReport": {"Unit": "Minutes", "Value": 10080}, "Data": {"Size": 5, "CurrentPowerMode": 0, "AvailablePowerSourceBitField": 4, "DisposableBatteryVoltage": 200, "CurrentPowerSource": 0}}

9. Conf Node descriptor Disposable Battery voltage + Constant Voltage
=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "Configuration", "ReportParameters": {"New": "No", "Reserved": 0, "CauseRequest": "No", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "NodePowerDescriptor", "AttributeType": "ByteString", "MinReport": {"Unit": "Seconds", "Value": 10}, "MaxReport": {"Unit": "Minutes", "Value": 10080}, "Data": {"Size": 7, "CurrentPowerMode": 0, "AvailablePowerSourceBitField": 5, "DisposableBatteryVoltage": 200,"ConstantVoltage": 400, "CurrentPowerSource": 0}}

9. Conf Node descriptor Constant Voltage
=> To use in encoding: {"EndPoint": 0, "Report": "Standard", "CommandID": "ConfigureReporting", "ClusterID": "Configuration", "ReportParameters": {"New": "No", "Reserved": 0, "CauseRequest": "No", "SecuredIfAlarm": "No", "Secured": "No", "NoHeaderPort": "No", "Batch": "No"}, "AttributeID": "NodePowerDescriptor", "AttributeType": "ByteString", "MinReport": {"Unit": "Seconds", "Value": 10}, "MaxReport": {"Unit": "Minutes", "Value": 10080}, "Data": {"Size": 5, "CurrentPowerMode": 0, "AvailablePowerSourceBitField": 1, "ConstantVoltage": 200, "CurrentPowerSource": 0}}

FRANCAIS
--------------
--------------

Prérequis:
--------------

Python 3.6 ou une version plus récente

. installer dicctoxml:
	- aller dans dicttoxml-1.7.4/
	- executer dans un terminal: py setup.py install
	
. installer construct:
	- aller dans construct-2.8.12/
	- executer dans un terminal: py setup.py install


Lancer le décodage:
-----------------
. Aller dans srcWatteco/
. Décoder une trame en xml: echo 11... | py Main.py -of xmlp
. Décoder une trame en json: echo 11... | py Main.py -of json


Lancer l'encodage:
-----------------
. Aller dans srcWatteco/
. Encoder un json en trame : echo {"EndPoint": 0, ...} | py Main.py -m e

Pour les exemples cf la version anglaise.