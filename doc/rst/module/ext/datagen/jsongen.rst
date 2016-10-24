.. _module_ext_datagen_jsongen:

JSONGen
=======

This sections contains module documentation of jsongen module.

jsongen
^^^^^^^

Module provides class JSONGen for generating JSON sample according to specification (JSON schema).
It uses external module simplejson automatically installed together with hydratk-lib-network.
Unit tests available at hydratk/extensions/datagen/jsongen/01_methods_ut.jedi

**Attributes** :

* _mh - MasterHead reference
* _path - directory path of specification file
* _schema - parsed specification

**Properties (Getters)** :

* path - returns _path
* schema - returns schema

**Methods** :

* __init__

Method sets MasterHead reference.

* import_schema

Method imports specification from file. First fires event jsongen_before_import_spec where parameter filename can be rewritten.
It imports file using simplejson method loads and sets _schema. After that fires event jsongen_after_import_spec and returns bool.

  .. code-block:: python
  
     from hydratk.extensions.datagen.jsongen import JSONGen 
     
     g = JSONGen()
     path = '/var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.json'
     g.import_schema(path)    
     
* tojson

Method generates sample according to JSON specification. First fires event jsongen_before_write where parameter outfile can be rewritten.
It uses method _tojson_rec (returns json string) and writes to file using simplejson method dumps (default filename sample.json).
After that fires event json_after_write and returns bool.

  .. code-block:: python
  
     res = g.tojson()
     
* _tojson_rec

Auxiliary method to generate JSON sample. It recursively goes through specification structure, processing is driven by element data type.

simple - set ? placeholder
array - set list with one item (recursive call)
object - process object via recursive call            

If schema references another schema it is imported using method _import_ref_schema.

* _import_ref_schema

Auxiliary method to import referenced schema. It supports local schemas (uri starts with file://) not remote (uri starts with http://).
It imports schema using simplejson method loads.