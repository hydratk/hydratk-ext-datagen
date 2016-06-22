# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.datagen.translation.cs.help
   :platform: Unix
   :synopsis: Czech language translation for Datagen extension help generator
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""
language = {
  'name' : 'Čeština',
  'ISO-639-1' : 'cs'
} 

''' Datagen Commands '''
help_cmd = {
    'gen-asn1' : 'enkódovat textový soubor, dekódovat binární soubor podle ASN.1 specifikace',
    'gen-json' : 'generovat vzorový json soubor podle JSON specifikace',
    'gen-xml'  : 'generovat vzorový xml soubor podle WSDL/XSD specifikace',
    
    #standalone with option profile datagen 
    'asn1' : 'enkódovat textový soubor, dekódovat binární soubor podle ASN.1 specifikace',
    'json' : 'generovat vzorový json soubor podle JSON specifikace',
    'xml'  : 'generovat vzorový xml soubor podle WSDL/XSD specifikace'    
}

''' Datagen Options '''
help_opt = {             
   'gen-spec'     : { '{h}--gen-spec <cesta>{e}' : { 'description' : 'soubor se specifikací', 'commands' : ('gen-asn1', 'gen-json', 'gen-xml')}},
   'gen-input'    : { '{h}--gen-input <cesta>{e}' : { 'description' : 'vstupní soubor', 'commands' : ('gen-asn1')}},
   'gen-output'   : { '{h}[--gen-output <cesta>]{e}' : { 'description' : 'výstupní soubor, default vstupní soubor s jinou příponou nebo sample.json, sample.xml', 'commands' : ('gen-asn1', 'gen-json', 'gen-xml')}},
   'gen-action'   : { '{h}--gen-action encode|decode{e}' : { 'description' : 'akce', 'commands' : ('gen-asn1')}},
   'gen-element'  : { '{h}--gen-element <název>{e}' : { 'description' : 'název elementu ze specifikace', 'commands' : ('gen-asn1', 'gen-xml')}},
   'gen-envelope' : { '{h}[--gen-envelope]{e}' : { 'description' : 'generovat včetně SOAP obálky', 'commands' : ('gen-xml')}},
   
   #standalone with option profile datagen
   'spec'     : { '{h}--spec <cesta>{e}' : { 'description' : 'soubor se specifikací', 'commands' : ('asn1', 'json', 'xml')}},
   'input'    : { '{h}--input <cesta>{e}' : { 'description' : 'vstupní soubor', 'commands' : ('asn1')}},
   'output'   : { '{h}[--output <cesta>]{e}' : { 'description' : 'výstupní soubor, default vstupní soubor s jinou příponou nebo sample.json, sample.xml', 'commands' : ('asn1', 'json', 'xml')}},
   'action'   : { '{h}--action encode|decode{e}' : { 'description' : 'akce', 'commands' : ('asn1')}},
   'element'  : { '{h}--element <název>{e}' : { 'description' : 'název elementu ze specifikace', 'commands' : ('asn1', 'xml')}},
   'envelope' : { '{h}[--envelope]{e}' : { 'description' : 'generovat včetně SOAP obálky', 'commands' : ('xml')}}                
}