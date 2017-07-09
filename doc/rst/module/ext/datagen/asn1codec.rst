.. _module_ext_datagen_asn1codec:

ASN1Codec
=========

This sections contains module documentation of asn1codec module.

asn1codec
^^^^^^^^^

Module provides class ASN1Codec for compiling, decoding, encoding, transcoding ASN.1 files according to specification (ASN.1 schema).
It uses external tool `ffasn1dump <https://bellard.org/ffasn1/ffasn1dump.html>`_ created by Fabrice Bellard. 
Unit tests available at hydratk/extensions/datagen/asn1codec/01_methods_ut.jedi

**Attributes** :

* _mh - MasterHead reference
* _path - path to ffasn1dump

**Properties (Getters)** :

* path - returns _path

**Methods** :

* __init__

Method sets MasterHead reference and parses configuration.

* compile

Method compiles specification from file for validation. First it fires event asn1_before_compile where parameter spec can be rewritten. 
It calls ffasn1dump, fires event asn1_after_compile and returns bool.

  .. code-block:: python
  
     from hydratk.extensions.datagen.asn1codec import ASN1Codec
     
     g = ASN1Codec()
     spec = '/var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn'
     res = g.compile(spec)
     
* decode

Methods decodes ASN.1 file to file with readable format GSER. First it fires event asn1_before_decode where parameters (spec, element, input, iformat, output) can be rewritten.
It calls ffasn1dump, fires event asn1_after_decode and returns bool.

  .. code-block:: python
  
     res = g.decode(spec, 'TestSeq2', infile, 'ber', outfile)         
     
* encode

Methods encodes file with GSER format to ASN.1 file. First it fires event asn1_before_encode where parameters (spec, element, input, oformat, output) can be rewritten.
It calls ffasn1dump, fires event asn1_after_encode and returns bool.

  .. code-block:: python
  
     res = g.encode(spec, 'TestSeq2', infile, 'ber', outfile)     
     
* transcode

Methods transcodes ASN.1 file to file with different format. First it fires event asn1_before_transcode where parameters (spec, element, input, iformat, oformat, output) can be rewritten.
It calls ffasn1dump, fires event asn1_after_transcode and returns bool.

  .. code-block:: python
  
     res = g.transcode(spec, 'TestSeq2', infile, 'ber', 'oer', outfile)                   