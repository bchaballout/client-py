#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import careplan
from .fhirdate import FHIRDate


class CarePlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CarePlan", js["resourceType"])
        return careplan.CarePlan(js)
    
    def testCarePlan1(self):
        inst = self.instantiate_from("careplan-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan1(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan1(inst2)
    
    def implCarePlan1(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "procedure")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "64915003")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Operation on heart")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-06-27T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP2903")
        self.assertEqual(inst.modified.date, FHIRDate("2011-06-27T09:30:10+01:00").date)
        self.assertEqual(inst.modified.as_json(), "2011-06-27T09:30:10+01:00")
        self.assertEqual(inst.period.end.date, FHIRDate("2011-06-27").date)
        self.assertEqual(inst.period.end.as_json(), "2011-06-27")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-06-26").date)
        self.assertEqual(inst.period.start.as_json(), "2011-06-26")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan2(self):
        inst = self.instantiate_from("careplan-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan2(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan2(inst2)
    
    def implCarePlan2(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "procedure")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "359615001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Partial lobectomy of lung")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-07-07T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP2934")
        self.assertEqual(inst.modified.date, FHIRDate("2011-07-07T09:30:10+01:00").date)
        self.assertEqual(inst.modified.as_json(), "2011-07-07T09:30:10+01:00")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-07-07").date)
        self.assertEqual(inst.period.end.as_json(), "2013-07-07")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-07-06").date)
        self.assertEqual(inst.period.start.as_json(), "2011-07-06")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan3(self):
        inst = self.instantiate_from("careplan-example-f003-pharynx.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan3(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan3(inst2)
    
    def implCarePlan3(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "procedure")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "172960003")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Incision of retropharyngeal abscess")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledString, "2011-06-27T09:30:10+01:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/careplans")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CP3953")
        self.assertEqual(inst.modified.date, FHIRDate("2013-06-27T09:30:10+01:00").date)
        self.assertEqual(inst.modified.as_json(), "2013-06-27T09:30:10+01:00")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-08T09:30:10+01:00").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-08T09:30:10+01:00")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-08T09:00:10+01:00").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-08T09:00:10+01:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan4(self):
        inst = self.instantiate_from("careplan-example-f201-renal.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan4(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan4(inst2)
    
    def implCarePlan4(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "diet")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "284093001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Potassium supplementation")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.activity[0].detail.dailyAmount.code, "258718000")
        self.assertEqual(inst.activity[0].detail.dailyAmount.system, "http://snomed.info/sct")
        self.assertEqual(inst.activity[0].detail.dailyAmount.units, "mmol")
        self.assertEqual(inst.activity[0].detail.dailyAmount.value, 80)
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledString, "daily")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.activity[1].detail.category, "observation")
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "306005")
        self.assertEqual(inst.activity[1].detail.code.coding[0].display, "Echography of kidney")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[1].detail.prohibited)
        self.assertEqual(inst.activity[1].detail.status, "completed")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.modified.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.modified.as_json(), "2013-03-11")
        self.assertEqual(inst.participant[0].role.coding[0].code, "425268008")
        self.assertEqual(inst.participant[0].role.coding[0].display, "Review of care plan")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.participant[1].role.coding[0].code, "229774002")
        self.assertEqual(inst.participant[1].role.coding[0].display, "Carer")
        self.assertEqual(inst.participant[1].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-03-13").date)
        self.assertEqual(inst.period.end.as_json(), "2013-03-13")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2013-03-11")
        self.assertEqual(inst.status, "planned")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan5(self):
        inst = self.instantiate_from("careplan-example-f202-malignancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan5(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan5(inst2)
    
    def implCarePlan5(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "procedure")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "367336001")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "Chemotherapy")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.status, "in-progress")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.participant[0].role.coding[0].code, "28995006")
        self.assertEqual(inst.participant[0].role.coding[0].display, "Treated with")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan6(self):
        inst = self.instantiate_from("careplan-example-f203-sepsis.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan6(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan6(inst2)
    
    def implCarePlan6(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "observation")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "241541005")
        self.assertEqual(inst.activity[0].detail.code.coding[0].display, "High resolution computed tomography of lungs")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.status, "not-started")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.modified.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.modified.as_json(), "2013-03-11")
        self.assertEqual(inst.participant[0].role.coding[0].code, "425268008")
        self.assertEqual(inst.participant[0].role.coding[0].display, "Review of care plan")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.participant[1].role.coding[0].code, "278110001")
        self.assertEqual(inst.participant[1].role.coding[0].display, "Radiographic imaging")
        self.assertEqual(inst.participant[1].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-04-21").date)
        self.assertEqual(inst.period.end.as_json(), "2013-04-21")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-04-14").date)
        self.assertEqual(inst.period.start.as_json(), "2013-04-14")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan7(self):
        inst = self.instantiate_from("careplan-example-GPVisit.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan7(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan7(inst2)
    
    def implCarePlan7(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "encounter")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "nursecon")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.activity[0].detail.code.text, "Nurse Consultation")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.end.date, FHIRDate("2013-01-01T10:50:00+00:00").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.end.as_json(), "2013-01-01T10:50:00+00:00")
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.date, FHIRDate("2013-01-01T10:38:00+00:00").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.as_json(), "2013-01-01T10:38:00+00:00")
        self.assertEqual(inst.activity[0].detail.status, "completed")
        self.assertEqual(inst.activity[1].detail.category, "encounter")
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "doccon")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.activity[1].detail.code.text, "Doctor Consultation")
        self.assertFalse(inst.activity[1].detail.prohibited)
        self.assertEqual(inst.activity[1].detail.status, "scheduled")
        self.assertEqual(inst.id, "gpvisit")
        self.assertEqual(inst.participant[0].id, "part1")
        self.assertEqual(inst.participant[0].role.coding[0].code, "nur")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.participant[0].role.text, "nurse")
        self.assertEqual(inst.participant[1].id, "part2")
        self.assertEqual(inst.participant[1].role.coding[0].code, "doc")
        self.assertEqual(inst.participant[1].role.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.participant[1].role.text, "doctor")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-01-01T10:30:00+00:00").date)
        self.assertEqual(inst.period.start.as_json(), "2013-01-01T10:30:00+00:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")
    
    def testCarePlan8(self):
        inst = self.instantiate_from("careplan-example-integrated.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan8(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan8(inst2)
    
    def implCarePlan8(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "other")
        self.assertEqual(inst.activity[0].detail.extension[0].url, "http://example.org/DoNotUse/StructureDefinition/RevisionDate")
        self.assertEqual(inst.activity[0].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[0].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[0].detail.note, "Eve will review photos of high and low density foods and share with her parents")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[0].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[0].detail.status, "not-started")
        self.assertEqual(inst.activity[0].notes, "9/10/12 Eve eats one meal a day with her parents")
        self.assertEqual(inst.activity[1].detail.category, "other")
        self.assertEqual(inst.activity[1].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[1].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[1].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[1].detail.note, "Eve will ask her dad to asist her to put the head of her bed on blocks")
        self.assertFalse(inst.activity[1].detail.prohibited)
        self.assertEqual(inst.activity[1].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[1].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[1].detail.status, "not-started")
        self.assertEqual(inst.activity[1].notes, "9/10/12 Eve will sleep in her bed more often than the couch")
        self.assertEqual(inst.activity[2].detail.category, "other")
        self.assertEqual(inst.activity[2].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[2].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[2].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[2].detail.note, "Eve will reduce her intake of coffee and chocolate")
        self.assertFalse(inst.activity[2].detail.prohibited)
        self.assertEqual(inst.activity[2].detail.scheduledPeriod.start.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[2].detail.scheduledPeriod.start.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[2].detail.status, "in-progress")
        self.assertEqual(inst.activity[3].detail.category, "other")
        self.assertEqual(inst.activity[3].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[3].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[3].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[3].detail.note, "Eve will walk her friend's dog up and down a big hill 15-30 minutes 3 days a week")
        self.assertFalse(inst.activity[3].detail.prohibited)
        self.assertEqual(inst.activity[3].detail.scheduledPeriod.start.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[3].detail.scheduledPeriod.start.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[3].detail.status, "in-progress")
        self.assertEqual(inst.activity[3].notes, "8/27/12 Eve would like to try for 5 days a week.  9/10/12 Eve is still walking the dogs.")
        self.assertEqual(inst.activity[4].detail.category, "other")
        self.assertEqual(inst.activity[4].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[4].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[4].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[4].detail.note, "Eve will walk 3 blocks to her parents house twice a week")
        self.assertFalse(inst.activity[4].detail.prohibited)
        self.assertEqual(inst.activity[4].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[4].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[4].detail.status, "in-progress")
        self.assertEqual(inst.activity[4].notes, "8/13/12 Eve walked 4 times the last week.  9/10/12 Eve did not walk to her parents the last week, but has plans to start again")
        self.assertEqual(inst.activity[5].detail.category, "other")
        self.assertEqual(inst.activity[5].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[5].detail.extension[0].valueDate.date, FHIRDate("2012-08-13").date)
        self.assertEqual(inst.activity[5].detail.extension[0].valueDate.as_json(), "2012-08-13")
        self.assertEqual(inst.activity[5].detail.note, "Eve will us a calendar to check off after medications are taken")
        self.assertFalse(inst.activity[5].detail.prohibited)
        self.assertEqual(inst.activity[5].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[5].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[5].detail.status, "in-progress")
        self.assertEqual(inst.activity[6].detail.category, "other")
        self.assertEqual(inst.activity[6].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[6].detail.extension[0].valueDate.date, FHIRDate("2012-08-27").date)
        self.assertEqual(inst.activity[6].detail.extension[0].valueDate.as_json(), "2012-08-27")
        self.assertEqual(inst.activity[6].detail.note, "Eve will use her lights MWF after her shower for 3 minutes")
        self.assertFalse(inst.activity[6].detail.prohibited)
        self.assertEqual(inst.activity[6].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[6].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[6].detail.status, "in-progress")
        self.assertEqual(inst.activity[7].detail.category, "other")
        self.assertEqual(inst.activity[7].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[7].detail.extension[0].valueDate.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.activity[7].detail.extension[0].valueDate.as_json(), "2012-09-10")
        self.assertEqual(inst.activity[7].detail.note, "Eve will use a calendar of a chart to help her remember when to take her medications")
        self.assertFalse(inst.activity[7].detail.prohibited)
        self.assertEqual(inst.activity[7].detail.scheduledPeriod.start.date, FHIRDate("2012-07-10").date)
        self.assertEqual(inst.activity[7].detail.scheduledPeriod.start.as_json(), "2012-07-10")
        self.assertEqual(inst.activity[7].detail.status, "in-progress")
        self.assertEqual(inst.activity[7].notes, "7/23/12 Eve created a chart as a reminer to take the medications that do not fit in her pill box")
        self.assertEqual(inst.activity[8].detail.category, "other")
        self.assertEqual(inst.activity[8].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[8].detail.extension[0].valueDate.date, FHIRDate("2012-08-23").date)
        self.assertEqual(inst.activity[8].detail.extension[0].valueDate.as_json(), "2012-08-23")
        self.assertEqual(inst.activity[8].detail.note, "Eve will start using stretch bands and one step 2 days a week Mon/Wed 6-7am and maybe Friday afternoon")
        self.assertFalse(inst.activity[8].detail.prohibited)
        self.assertEqual(inst.activity[8].detail.scheduledPeriod.start.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[8].detail.scheduledPeriod.start.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[8].detail.status, "on-hold")
        self.assertEqual(inst.activity[8].notes, "7/30/12 will be able to esume exercise.  8/13/12 Eve prefers to focus on walking at this time")
        self.assertEqual(inst.activity[9].detail.category, "other")
        self.assertEqual(inst.activity[9].detail.extension[0].url, "http://example.org/DoNotUse/General/RevisionDate")
        self.assertEqual(inst.activity[9].detail.extension[0].valueDate.date, FHIRDate("2012-07-23").date)
        self.assertEqual(inst.activity[9].detail.extension[0].valueDate.as_json(), "2012-07-23")
        self.assertEqual(inst.activity[9].detail.note, "Eve will match a printed medication worksheet with the medication bottles at home")
        self.assertFalse(inst.activity[9].detail.prohibited)
        self.assertEqual(inst.activity[9].detail.scheduledPeriod.start.date, FHIRDate("2012-07-10").date)
        self.assertEqual(inst.activity[9].detail.scheduledPeriod.start.as_json(), "2012-07-10")
        self.assertEqual(inst.activity[9].detail.status, "completed")
        self.assertEqual(inst.id, "integrate")
        self.assertEqual(inst.modified.date, FHIRDate("2012-09-10").date)
        self.assertEqual(inst.modified.as_json(), "2012-09-10")
        self.assertEqual(inst.notes, "Patient family is not ready to commit to goal setting at this time.  Goal setting will be addressed in the future")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testCarePlan9(self):
        inst = self.instantiate_from("careplan-example-pregnancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan9(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan9(inst2)
    
    def implCarePlan9(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "encounter")
        self.assertEqual(inst.activity[0].detail.code.coding[0].code, "1an")
        self.assertEqual(inst.activity[0].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[0].detail.code.text, "First Antenatal encounter")
        self.assertEqual(inst.activity[0].detail.note, "The first antenatal encounter. This is where a detailed physical examination is performed.             and the pregnanacy discussed with the mother-to-be.")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.bounds.end.date, FHIRDate("2013-02-28").date)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.bounds.end.as_json(), "2013-02-28")
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.bounds.start.date, FHIRDate("2013-02-14").date)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.bounds.start.as_json(), "2013-02-14")
        self.assertEqual(inst.activity[0].detail.status, "scheduled")
        self.assertEqual(inst.activity[0].extension[0].url, "http://example.org/DoNotUse/careplan#andetails")
        self.assertEqual(inst.activity[0].extension[0].valueUri, "http://orionhealth.com/fhir/careplan/1andetails")
        self.assertEqual(inst.activity[1].detail.category, "encounter")
        self.assertEqual(inst.activity[1].detail.code.coding[0].code, "an")
        self.assertEqual(inst.activity[1].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[1].detail.code.text, "Follow-up Antenatal encounter")
        self.assertEqual(inst.activity[1].detail.note, "The second antenatal encounter. Discuss any issues that arose from the first antenatal encounter")
        self.assertFalse(inst.activity[1].detail.prohibited)
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.bounds.end.date, FHIRDate("2013-03-14").date)
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.bounds.end.as_json(), "2013-03-14")
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.bounds.start.date, FHIRDate("2013-03-01").date)
        self.assertEqual(inst.activity[1].detail.scheduledTiming.repeat.bounds.start.as_json(), "2013-03-01")
        self.assertEqual(inst.activity[1].detail.status, "not-started")
        self.assertEqual(inst.activity[2].detail.category, "encounter")
        self.assertEqual(inst.activity[2].detail.code.coding[0].code, "del")
        self.assertEqual(inst.activity[2].detail.code.coding[0].system, "http://example.org/mySystem")
        self.assertEqual(inst.activity[2].detail.code.text, "Delivery")
        self.assertEqual(inst.activity[2].detail.note, "The delivery.")
        self.assertFalse(inst.activity[2].detail.prohibited)
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.bounds.end.date, FHIRDate("2013-09-14").date)
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.bounds.end.as_json(), "2013-09-14")
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.bounds.start.date, FHIRDate("2013-09-01").date)
        self.assertEqual(inst.activity[2].detail.scheduledTiming.repeat.bounds.start.as_json(), "2013-09-01")
        self.assertEqual(inst.activity[2].detail.status, "not-started")
        self.assertEqual(inst.extension[0].url, "http://example.org/DoNotUse/careplan#lmp")
        self.assertEqual(inst.extension[0].valueDateTime.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.extension[0].valueDateTime.as_json(), "2013-01-01")
        self.assertEqual(inst.id, "preg")
        self.assertEqual(inst.participant[0].role.coding[0].code, "lmc")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://example.org/mysys")
        self.assertEqual(inst.participant[0].role.text, "Midwife")
        self.assertEqual(inst.participant[1].role.coding[0].code, "obs")
        self.assertEqual(inst.participant[1].role.coding[0].system, "http://example.org/mysys")
        self.assertEqual(inst.participant[1].role.text, "Obstretitian")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-10-01").date)
        self.assertEqual(inst.period.end.as_json(), "2013-10-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2013-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")
    
    def testCarePlan10(self):
        inst = self.instantiate_from("careplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CarePlan instance")
        self.implCarePlan10(inst)
        
        js = inst.as_json()
        self.assertEqual("CarePlan", js["resourceType"])
        inst2 = careplan.CarePlan(js)
        self.implCarePlan10(inst2)
    
    def implCarePlan10(self, inst):
        self.assertEqual(inst.activity[0].detail.category, "observation")
        self.assertEqual(inst.activity[0].detail.code.text, "a code for weight measurement")
        self.assertFalse(inst.activity[0].detail.prohibited)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.frequency, 1)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.period, 1)
        self.assertEqual(inst.activity[0].detail.scheduledTiming.repeat.periodUnits, "d")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.participant[0].role.text, "responsiblePerson")
        self.assertEqual(inst.participant[1].role.text, "adviser")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "additional")

