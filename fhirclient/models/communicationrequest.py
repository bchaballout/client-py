#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2015-07-06.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    
    A request to convey information. E.g., the CDS system proposes that an
    alert be sent to a responsible provider, the CDS system proposes that the
    public health agency be notified about a reportable condition.
    """
    
    resource_name = "CommunicationRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Message category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter leading to message.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None
        """ Communication medium.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.orderedOn = None
        """ When ordered or proposed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ Message urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Requester of communication.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.scheduledTime = None
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | failed.
        Type `str`. """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("medium", "medium", codeableconcept.CodeableConcept, True),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False),
            ("payload", "payload", CommunicationRequestPayload, True),
            ("priority", "priority", codeableconcept.CodeableConcept, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True),
            ("recipient", "recipient", fhirreference.FHIRReference, True),
            ("requester", "requester", fhirreference.FHIRReference, False),
            ("scheduledTime", "scheduledTime", fhirdate.FHIRDate, False),
            ("sender", "sender", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js


class CommunicationRequestPayload(fhirelement.FHIRElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    
    resource_name = "CommunicationRequestPayload"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.contentString = None
        """ Message part content.
        Type `str`. """
        
        super(CommunicationRequestPayload, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False),
            ("contentString", "contentString", str, False),
        ])
        return js

