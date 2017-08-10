.. _tutor_datagen_tut1_asn1:

Tutorial 1: ASN.1
=================

ASN.1 codec provides methods for compiling, decoding, encoding, transcoding ASN.1 files according to specification (ASN.1 schema)
It uses external tool `ffasn1dump <https://bellard.org/ffasn1/ffasn1dump.html>`_ created by Fabrice Bellard. The tool must be downloaded and installed manually. 

Command line
^^^^^^^^^^^^

It is controlled via command gen-asn1 with following options.

Mandatory:

* --gen-action <name>: compile|decode|encode|transcode, compile specification, decode ASN.1 file, encode ASN.1 file, transcode to different format
* --gen-spec <path>: path to ASN.1 specification file
* --gen-element <name>: root element title
* --gen-input <path>: path to input file

Optional: 

* --gen-iformat <name>: ber|der|oer|aper|uper|xer|gser, default ber for action decode, gser for action encode
* --gen-oformat <name>: ber|der|oer|aper|uper|xer|gser, default ber for action encode, gser for action decode
* --gen-output <path>: path to output file, output is written to file <input> with changed suffix by default

Specification
^^^^^^^^^^^^^

First create file spec.asn with sample specification in ASN.1 format.

  .. code-block:: cfg
  
     Test1 DEFINITIONS AUTOMATIC TAGS ::=
     BEGIN
    
       TestInt ::= INTEGER {un(1), deux(2)} (0..100, ...)
       TestEnum ::= ENUMERATED {un , deux, trois}
       TestBitStr ::= BIT STRING (SIZE(12..24, ...))
       TestOctetStr ::= OCTET STRING (SIZE(2..10))
       TestChoice ::= CHOICE {
         a TestInt,
         b TestEnum,
         c TestBitStr
       }
       TestSeqOf ::= SEQUENCE SIZE (1..4) OF TestInt
       TestSeq ::= SEQUENCE {
         a TestInt,
         b TestEnum OPTIONAL,
         c TestBitStr
       }
       TestSeqSeq ::= SEQUENCE {
         a TestSeq,
         b SEQUENCE OF TestSeq,
         c TestChoice
       }
       TestSeq2 ::= SEQUENCE {
         a TestInt,
         b BOOLEAN,
         c SEQUENCE {
           d BOOLEAN OPTIONAL,
           e TestOctetStr
         },
         f SET {
           g TestInt,
           h BOOLEAN
         }
       }        
     END
     
  .. note::
  
     ASN.1 specifications used in industry are more complicated than our sample.
     For example TAP specification (used in telecommunications) has around 1600 lines.
     
Encoder
^^^^^^^

Now create JSON file input.json with sample record compliant with TestSeq2 definition.     

  .. code-block:: javascript
   
     {
       "a": 20,
       "b": true,
       "c": {
         "d": false,
         "e": "xyz"
       },
       "f": {
         "g": 128,
         "h": true
       }
     }
     
Encode the file using command gen-asn1.     
     
  .. code-block:: bash
  
     $ htk --gen-action encode --gen-spec spec.asn --gen-input input.json --gen-element TestSeq2 --gen-output output.bin gen-asn1  
     
     encode finished
     
File output.bin contains hex text. 

  .. code-block:: cfg
  
     30198001148101FFA208800100810378797AA307800200808101FF

  .. note::
  
    Option output is optional. If not provided the output filename is based on input filename (input.bin in example).
    
Decoder
^^^^^^^

Now let's try to decode generated file output.bin.

  .. code-block:: bash
  
     $ htk --gen-action decode --gen-spec spec.asn --gen-input output.bin --gen-element TestSeq2 gen-asn1
     
     decode finished
     
Generated file output.json has same content as original file input.json.

API
^^^

This section shows several examples how to use ASN.1 codec as API in your extensions/libraries.
API uses HydraTK core functionalities so it must be running.

Methods    

* compile: compile ASN.1 specification, params: spec
* decode: decode to readable format, params: spec, element, input, iformat, output
* encode: encode from readable format, params: spec, element, input, oformat, output   
* transcode: transcode format, params: spec, element, input, iformat, oformat, output

Examples

  .. code-block:: python
  
     # import codec
     from hydratk.extensions.datagen.asn1codec import ASN1Codec
     g = ASN1Codec()
     
     # compile specification
     spec = '/var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn'
     res = g.compile(spec)
     
     # decode
     res = res = g.decode(spec, 'TestSeq2', infile, 'ber', outfile) 
     
     # encode
     res = g.encode(spec, 'TestSeq2', infile, 'ber', outfile)   
     
     # transcode
     res = g.transcode(spec, 'TestSeq2', infile, 'ber', 'oer', outfile)    