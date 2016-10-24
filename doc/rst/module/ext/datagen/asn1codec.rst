.. _module_ext_datagen_asn1codec:

ASN1Codec
=========

This sections contains module documentation of asn1codec module.

asn1codec
^^^^^^^^^

Module provides class ASN1Codec for encode and decode ASN.1 files according to specification (ASN.1 schema).
It uses necessary parts of external module `libmich <https://github.com/mitshell/libmich>`_. 
Unit tests available at hydratk/extensions/datagen/asn1codec/01_methods_ut.jedi

When Python2.6 or Python3 is used the module is not supported (raises NotImplementedError).

**Attributes** :

* _mh - MasterHead reference
* _path - specification file path
* _spec - parsed specification
* _elements - parsed elements

**Properties (Getters)** :

* path - returns _path
* spec - returns _spec
* elements - returns _elements

**Methods** :

* __init__

Method sets MasterHead reference.

* import_spec

Method imports specification from file. First it fires event asn1_before_import_spec where parameter filename can be rewritten. 
It uses libmich method process_modules and sets _spec, _elements. Sets some libmich attributes (BER format).
After that fires event asn1_after_import_spec and returns bool.

  .. code-block:: python
  
     from hydratk.extensions.datagen.asn1codec import ASN1Codec
     
     g = ASN1Codec()
     file = '/var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn'
     res = g.import_spec(file)
     
* encode

Method encodes JSON file to binary file. First it fires event asn1_before_encode where parameters (infile, element, outfile) can be rewritten.   
It reads JSON file using simplejson methods loads. File can contains single (dictionary) or multiple records (list of dictionary).
element is name of encoded element.

libmich codec requires some data type modifications (using method _update_datatypes).
It uses libmich method encode and writes to file (default input filename with extension bin instead of json).
After that if fires event asn1_after_encode and returns bool.

  .. code-block:: python
  
     res = g.encode(infile, 'TestSeq2')  
     
* decode

Methods decodes binary file to JSON file. First it fires event asn1_before_decode where parameters (infile, element, outfile) can be rewritten.
It reads binary file and if there are multiple records they are splitted (using method _split_records).

It uses libmich method decode, the result is stored to ordered dictionary according to specification order (using method _create_dict).
Method writes to file using simplejson method dumps (default input filename with extension json instead of bin).
After that it fires event asn1_after_decode and returns bool.

  .. code-block:: python
  
     res = g.decode(infile, 'TestSeq2')
     
* __str__

Method returns parsed ASN.1 specification in human readable format.

* _update_datatypes

Auxiliary method. It updates some parameter datatypes of input json file to be compatible with libmich method encode.
It recursively goes through dictionary structure. long -> int, unicode -> str.

* _split_records

Auxiliary method. It splits binary records. The record size can be derived from ASN.1 content (initial bytes).
The method finds start of each record in byte array.
                 
* _create_dict

Auxiliary method. It transforms decoded data to ordered dictionary (it respects ordering in specification).
It recursively goes through result structure and reorders it. It detects complex ASN.1 types (SEQUENCE, SET, CHOICE).                 