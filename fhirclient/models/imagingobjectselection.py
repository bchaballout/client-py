#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference


class ImagingObjectSelection(domainresource.DomainResource):
    """ Key Object Selection.
    
    A set of DICOM SOP Instances of a patient, selected for some application
    purpose, e.g., quality assurance, teaching, conference, consulting, etc.
    Objects selected can be from different studies, but must be of the same
    patient.
    """
    
    resource_name = "ImagingObjectSelection"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authoringTime = None
        """ Authoring time of the selection.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Description text.
        Type `str`. """
        
        self.patient = None
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study identity of the selected instances.
        List of `ImagingObjectSelectionStudy` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uid = None
        """ Instance UID.
        Type `str`. """
        
        super(ImagingObjectSelection, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingObjectSelection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False),
            ("authoringTime", "authoringTime", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("study", "study", ImagingObjectSelectionStudy, True),
            ("title", "title", codeableconcept.CodeableConcept, False),
            ("uid", "uid", str, False),
        ])
        return js


class ImagingObjectSelectionStudy(fhirelement.FHIRElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudy"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.series = None
        """ Series identity of the selected instances.
        List of `ImagingObjectSelectionStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Study instance uid.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudy, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudy, self).elementProperties()
        js.extend([
            ("series", "series", ImagingObjectSelectionStudySeries, True),
            ("uid", "uid", str, False),
            ("url", "url", str, False),
        ])
        return js


class ImagingObjectSelectionStudySeries(fhirelement.FHIRElement):
    """ Series identity of the selected instances.
    
    Series indetity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudySeries"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.instance = None
        """ The selected instance.
        List of `ImagingObjectSelectionStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Series instance uid.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeries, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeries, self).elementProperties()
        js.extend([
            ("instance", "instance", ImagingObjectSelectionStudySeriesInstance, True),
            ("uid", "uid", str, False),
            ("url", "url", str, False),
        ])
        return js


class ImagingObjectSelectionStudySeriesInstance(fhirelement.FHIRElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.frames = None
        """ The frame set.
        List of `ImagingObjectSelectionStudySeriesInstanceFrames` items (represented as `dict` in JSON). """
        
        self.sopClass = None
        """ SOP class uid of instance.
        Type `str`. """
        
        self.uid = None
        """ Uid of the selected instance.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeriesInstance, self).elementProperties()
        js.extend([
            ("frames", "frames", ImagingObjectSelectionStudySeriesInstanceFrames, True),
            ("sopClass", "sopClass", str, False),
            ("uid", "uid", str, False),
            ("url", "url", str, False),
        ])
        return js


class ImagingObjectSelectionStudySeriesInstanceFrames(fhirelement.FHIRElement):
    """ The frame set.
    
    Identity and location information of the frames in the selected instance.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstanceFrames"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.frameNumbers = None
        """ Frame numbers.
        List of `int` items. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstanceFrames, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingObjectSelectionStudySeriesInstanceFrames, self).elementProperties()
        js.extend([
            ("frameNumbers", "frameNumbers", int, True),
            ("url", "url", str, False),
        ])
        return js

