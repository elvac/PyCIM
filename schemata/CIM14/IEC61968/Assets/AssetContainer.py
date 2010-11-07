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

from CIM14.IEC61968.Assets.Asset import Asset

class AssetContainer(Asset):
    """Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """

    def __init__(self, Seals=None, Assets=None, **kw_args):
        """Initializes a new 'AssetContainer' instance.

        @param Seals: All seals applied to this asset container.
        @param Assets:
        """
        self._Seals = []
        self.Seals = [] if Seals is None else Seals

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(AssetContainer, self).__init__(**kw_args)

    def getSeals(self):
        """All seals applied to this asset container.
        """
        return self._Seals

    def setSeals(self, value):
        for x in self._Seals:
            x._AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Seals = value

    Seals = property(getSeals, setSeals)

    def addSeals(self, *Seals):
        for obj in Seals:
            obj._AssetContainer = self
            self._Seals.append(obj)

    def removeSeals(self, *Seals):
        for obj in Seals:
            obj._AssetContainer = None
            self._Seals.remove(obj)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x._AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj._AssetContainer = self
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj._AssetContainer = None
            self._Assets.remove(obj)
