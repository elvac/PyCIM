# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""The IEC 61968 subpackages of the CIM are developed, standardized and maintained by IEC TC57 Working Group 14: interfaces for distribution management (WG14). Currently, normative parts of the model support the needs of information exchange defined in IEC 61968-9 and in IEC 61968-13.
"""

from CDPSM.Asset.Element import Element

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-4/CDPSM/Asset"
nsPrefix = "asset"

packageMap = {
    "Element": "CDPSM.Asset",
    "PerLengthSequenceImpedance": "CDPSM.Asset.IEC61970.Wires",
    "ACLineSegment": "CDPSM.Asset.IEC61970.Wires",
    "TransformerCoreAdmittance": "CDPSM.Asset.IEC61970.Wires",
    "TransformerTank": "CDPSM.Asset.IEC61970.Wires",
    "TransformerTankEnd": "CDPSM.Asset.IEC61970.Wires",
    "TransformerStarImpedance": "CDPSM.Asset.IEC61970.Wires",
    "PerLengthPhaseImpedance": "CDPSM.Asset.IEC61970.Wires",
    "TransformerEnd": "CDPSM.Asset.IEC61970.Wires",
    "NameType": "CDPSM.Asset.IEC61970.Core",
    "IdentifiedObject": "CDPSM.Asset.IEC61970.Core",
    "Name": "CDPSM.Asset.IEC61970.Core",
    "ConductorInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "WireArrangement": "CDPSM.Asset.IEC61968.AssetModels",
    "WireType": "CDPSM.Asset.IEC61968.AssetModels",
    "EndDeviceInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "OverheadConductorInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "TapChangerInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "TransformerTankInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "CableInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "TransformerEndInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "PowerTransformerInfo": "CDPSM.Asset.IEC61968.AssetModels",
    "AssetInfo": "CDPSM.Asset.IEC61968.Assets",
}


class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class ResistancePerLength(float):
    """Resistance (real part of impedance) per unit of length.
    """
    pass

class Temperature(float):
    """Value of temperature in degrees Celsius.
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass

class Length(float):
    """Unit of length.
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
    """
    pass

class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class Displacement(float):
    """Unit of displacement relative a reference position, hence can be negative.
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class Frequency(float):
    """Cycles per second
    """
    pass

class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass
