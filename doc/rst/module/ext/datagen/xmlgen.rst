.. _module_ext_datagen_xmlgen:

XMLGen
======

This sections contains module documentation of xmlgen module.

xmlgen
^^^^^^

Module provides class XMLGen for generating XML sample according to specification (WSDL/XSD schema).
It uses external modules suds, lxml automatically installed together with hydratk-lib-network.
Unit tests available at hydratk/extensions/datagen/xmlgen/01_methods_ut.jedi

**Attributes** :

* _mh - MasterHead reference
* _path - specification file path
* _client - suds client object instance

**Properties (Getters)** :

* path - returns _path
* client - returns _client

**Methods** :

* __init__ 

Method sets MasterHead reference.

* import_spec

Method imports specification from file. First it fires event xmlgen_before_import_spec where parameter filename can be rewritten.
When specification is WSDL file it creates suds client (constructor Client) which imports local file.
When specification is XSD file it calls _create_dummy_wsdl and instances suds Client to import generated wsdl file (not possible to load xsd file only)..

After that it fires event xmlgen_after_import_spec and returns bool.

  .. code-block:: python
  
     from hydratk.extensions.datagen.xmlgen import XMLGen
     
     g = XMLGen()
     file = '/var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/crm.wsdl'
     res = g.import_spec(file) 
     
* toxml

Method generates sample according to JSON specification. First fires event xmlgen_before_write where parameters (root, outfile, envelope) can be rewritten.
It uses method _toxml_rec (returns xml object) and writes to file using lxml method tostring (default filename sample.xml). 
root is name of generated element (it mustn't be the root element). When envelope is request, the method prepares standard SOAP envelope.

After that it fires event xmlgen_after_write and returns bool.

  .. code-block:: python
  
     # element create_service
     res = g.toxml('create_service')
     
     # include SOAP envelope
     res = g.toxml('create_service', outfile, envelope=True) 
     
* _toxml_rec

Auxiliary method to generate XML sample. It recursively goes through specification structure, processing is driven by element type.
It creates xml object using suds method factory.create when root element is generated.
It element type and namespace using methods _get_element_type, _get_element_ns.

simple - set ? placeholder
array - set list with one item (recursive call)
complex - process process via recursive call             

* _get_element_type

Auxiliary method to determine element type (simple or complex). The information is stored in schema metadata.

* _get_element_ns

Auxiliary method to determine element namespace. The information is stored in schema metadata.

* _create_dummy_wsdl

Auxiliary method the generate dummy WSDL which references given XSD. It reads target namespace from xsd and prepares
simple wsdl file from template. wsdl can already be imported by suds client.    