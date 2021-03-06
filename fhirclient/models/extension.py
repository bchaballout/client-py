#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Extension) on 2015-07-06.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import signature
from . import timing


class Extension(fhirelement.FHIRElement):
    """ Optional Extensions Element - found in all resources..
    
    Optional Extensions Element - found in all resources.
    """
    
    resource_name = "Extension"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.url = None
        """ identifies the meaning of the extension.
        Type `str`. """
        
        self.valueAddress = None
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Value of extension.
        Type `str`. """
        
        self.valueBoolean = None
        """ Value of extension.
        Type `bool`. """
        
        self.valueCode = None
        """ Value of extension.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of extension.
        Type `float`. """
        
        self.valueHumanName = None
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Value of extension.
        Type `int`. """
        
        self.valuePeriod = None
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Value of extension.
        Type `str`. """
        
        self.valueTime = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUri = None
        """ Value of extension.
        Type `str`. """
        
        super(Extension, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, False),
            ("valueAddress", "valueAddress", address.Address, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False),
            ("valueBase64Binary", "valueBase64Binary", str, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCode", "valueCode", str, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("valueCoding", "valueCoding", coding.Coding, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False),
            ("valueInteger", "valueInteger", int, False),
            ("valuePeriod", "valuePeriod", period.Period, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueRange", "valueRange", range.Range, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False),
            ("valueSignature", "valueSignature", signature.Signature, False),
            ("valueString", "valueString", str, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False),
            ("valueTiming", "valueTiming", timing.Timing, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js

