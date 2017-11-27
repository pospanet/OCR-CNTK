# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# author: janpos@microsoft.com
# ==============================================================================

import string

class Constants:
    _otherCharacters = ".,-_@/#&"
    _nationalCharacters = "ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ"
    _nationalCharacterAlternatives = ["Aapex","Ccaron","Dcaron","Eapex","Ecaron","Iapex","Ncaron",
        "Oapex","Rcaron","Scaron","Tcaron","Uapex","Ucaron","Yapex","Zcaron"]
    _obsoleteNationalCharacters = "ÁcdÉeÍnÓrŠtÚuÝŽ"

    @classmethod
    def getCzechCharacters(self):
        characters = string.ascii_uppercase + string.digits + self._otherCharacters + self._nationalCharacters
        return characters

    @classmethod
    def getCzechCharactersOnly(self):
        return self._nationalCharacters
  
    @classmethod
    def getObsoleteCzechCharactersOnly(self):
        return self._obsoleteNationalCharacters
    
    @classmethod
    def getCzechCharactersOnly(cls):
        return cls._nationalCharacters

    @classmethod
    def getNationalCharacterAlternative(self, character):
        if character in list(self._nationalCharacters):
            return self._nationalCharacterAlternatives[self._nationalCharacters.index(character)]
        if character in list(self._obsoleteNationalCharacters):
            return self._nationalCharacterAlternatives[self._nationalCharacters.index(character)]
        return character