# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


nsPrefix = "cimGenerators"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Generators"

from CIM14.Dynamics.Generators.GenLoad import GenLoad
from CIM14.Dynamics.Generators.GenEquiv import GenEquiv
from CIM14.Dynamics.Generators.GenAsync import GenAsync

class IfdBaseType(str):
    """Values are: other, iffl, ifag, ifnl
    """
    pass

class SynchronousGeneratorType(str):
    """Type of synchronous generator as used in dynamic simulation applications
    Values are: roundRotor, transient, typeF, typeJ, salientPole
    """
    pass

class ParametersFormType(str):
    """Values are: timeConstantReactance, equivalentCircuit
    """
    pass