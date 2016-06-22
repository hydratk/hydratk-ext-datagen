# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.datagen.translation.en.help
   :platform: Unix
   :synopsis: English language translation for Datagen extension help generator
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""
language = {
  'name' : 'English',
  'ISO-639-1' : 'en'
} 

''' Datagen Commands '''
help_cmd = {
    'gen-asn1' : 'encode text file, decode binary file according to ASN.1 specification',
    'gen-json' : 'generate sample json file according to JSON specification',
    'gen-xml'  : 'generate sample xml file according to WSDL/XSD specification',
    
    #standalone with option profile datagen 
    'asn1' : 'encode text file, decode binary file according to ASN.1 specification',
    'json' : 'generate sample json file according to JSON specification',
    'xml'  : 'generate sample xml file according to WSDL/XSD specification'
}

''' Datagen Options '''
help_opt = {             
   'gen-spec'     : { '{h}--gen-spec <path>{e}' : { 'description' : 'specification filename', 'commands' : ('gen-asn1', 'gen-json', 'gen-xml')}},
   'gen-input'    : { '{h}--gen-input <path>{e}' : { 'description' : 'input filename', 'commands' : ('gen-asn1')}},
   'gen-output'   : { '{h}[--gen-output <path>]{e}' : { 'description' : 'output filename, default input filename with changed suffix or sample.json, sample.xml', 'commands' : ('gen-asn1', 'gen-json', 'gen-xml')}},
   'gen-action'   : { '{h}--gen-action encode|decode{e}' : { 'description' : 'action', 'commands' : ('gen-asn1')}},
   'gen-element'  : { '{h}--gen-element <title>{e}' : { 'description' : 'element title from specification', 'commands' : ('gen-asn1', 'gen-xml')}},
   'gen-envelope' : { '{h}[--gen-envelope]{e}' : { 'description' : 'generate including SOAP envelope', 'commands' : ('gen-xml')}},
   
   #standalone with option profile datagen  
   'spec'     : { '{h}--spec <path>{e}' : { 'description' : 'specification filename', 'commands' : ('asn1', 'json', 'xml')}},
   'input'    : { '{h}--input <path>{e}' : { 'description' : 'input filename', 'commands' : ('asn1')}},
   'output'   : { '{h}[--output <path>]{e}' : { 'description' : 'output filename, default input filename with changed suffix or sample.json, sample.xml', 'commands' : ('asn1', 'json', 'xml')}},
   'action'   : { '{h}--action encode|decode{e}' : { 'description' : 'action', 'commands' : ('asn1')}},
   'element'  : { '{h}--element <title>{e}' : { 'description' : 'element title from specification', 'commands' : ('asn1', 'xml')}},
   'envelope' : { '{h}[--envelope]{e}' : { 'description' : 'generate including SOAP envelope', 'commands' : ('xml')}}                  
}

