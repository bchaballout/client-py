#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import list
from .fhirdate import FHIRDate


class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("List", js["resourceType"])
        return list.List(js)
    
    def testList1(self):
        inst = self.instantiate_from("list-example-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList1(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList1(inst2)
    
    def implList1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2012-11-26T07:30:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-26T07:30:23+11:00")
        self.assertEqual(inst.emptyReason.coding[0].code, "nil-known")
        self.assertEqual(inst.emptyReason.coding[0].display, "Nil Known")
        self.assertEqual(inst.emptyReason.coding[0].system, "http://hl7.org/fhir/special-values")
        self.assertEqual(inst.emptyReason.text, "The patient is not on any medications")
        self.assertEqual(inst.id, "example-empty")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList2(self):
        inst = self.instantiate_from("list-example-familyhistory-f201-roel.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList2(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList2(inst2)
    
    def implList2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.note, "Both parents, both brothers and both children (twin) are still alive.")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList3(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile-annie.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList3(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList3(inst2)
    
    def implList3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "prognosis")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList4(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList4(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList4(inst2)
    
    def implList4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "genetic")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.div, "<div>To do</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testList5(self):
        inst = self.instantiate_from("list-example-medlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList5(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList5(inst2)
    
    def implList5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2013-11-20T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2013-11-20T23:10:23+11:00")
        self.assertEqual(inst.entry[0].flag[0].coding[0].code, "01")
        self.assertEqual(inst.entry[0].flag[0].coding[0].display, "Prescribed")
        self.assertEqual(inst.entry[0].flag[0].coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.entry[0].flag[1].text, "Review required")
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(inst.entry[1].flag[0].coding[0].code, "02")
        self.assertEqual(inst.entry[1].flag[0].coding[0].display, "Cancelled")
        self.assertEqual(inst.entry[1].flag[0].coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.id, "med-list")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList6(self):
        inst = self.instantiate_from("list-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList6(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList6(inst2)
    
    def implList6(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-11-25T22:17:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-25T22:17:00+11:00")
        self.assertTrue(inst.entry[0].deleted)
        self.assertEqual(inst.entry[0].flag[0].text, "Deleted due to error")
        self.assertEqual(inst.entry[1].flag[0].text, "Added")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")

