.. _module_ext_datagen_main:

Main
====

This sections contains module documentation of main datagen modules.

bootstrapper
^^^^^^^^^^^^

Module provides bootstrapper (method run_app) for DataGen extension. 
You can run it in standalone mode using method command datagen (i.e. installed to /usr/local/bin/datagen).
Unit tests available at hydratk/extensions/datagen/bootstrapper/01_methods_ut.jedi

datagen
^^^^^^^

Modules provides class Extension inherited from class hydratk.core.extension.Extension.
Unit tests available at hydratk/extensions/datagen/datagen/01_methods_ut.jedi

**Methods** :

* _init_extension

Method sets extension metadata (id, name, version, author, year). 

* _check_dependencies

Method checks if all required modules are installed.

* _uninstall

Method returns additional uninstall data.

* _register_actions

Methods registers actions hooks according to profile htk (default mode) or datagen (standalone mode)

* _register_htk_actions

Method registers action hooks for default mode.

commands - gen-asn1, gen-json, gen-xml, gen-selenium
long options - gen-spec, gen-input, gen-output, gen-action, gen-element, gen-envelope, gen-browser, gen-timeout

* _register_standalone_actions

Method registers action hooks for standalone mode.

commands - asn1, json, xml, help
long options - spec, input, output, action, element, envelope
global options - config, debug, debug-channel, language, run-mode, force, interactive, home

* gen_json

Method handles command gen-json. It uses options gen-spec (specification filename, mandatory), gen-output (output filename, optional).
Creates JSONGen object instance, imports specification (method import_schema) and generates sample (method tojson).

  .. code-block:: bash
  
     htk --gen-spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.json --gen-output test.json gen-json
     
     datagen --spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.json --output test.json json
     
* gen_xml

Method handles command gen-xml. It uses options gen-spec (specification filename, mandatory), gen-element (generated element name, mandatory), 
gen-output (output filename, optinal), gen-envelope (include SOAP envelope, optional). Creates XMLGen object instance, imports specification 
(method import_spec) and generates sample (method toxml).

  .. code-block:: bash
  
     htk --gen-spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/crm.wsdl --gen-element create_service --gen-output test.xml 
         --gen-envelope gen-xml     
         
     datagen --spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/crm.wsdl --element create_service --output test.xml --envelope
     
* gen_asn1

Method handles command gen-asn1. It uses options gen-action (encode|decode, mandatory), gen-spec (specification filename, mandatory), gen-element 
(generated element name, mandatory), gen-input (input filename, mandatory), gen-output (output filename, optional).
Creates ASN1Codec object instance, imports specification (method import_spec) and generates record (method according to action, encode or decode).

  .. code-block:: bash
  
     # encoding
     htk --gen-action encode --gen-spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn --gen-element TestSeq2 
         --gen-input in.json --gen-output out.bin gen-asn1
         
     datagen --action encode --spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn --element TestSeq2 --input in.json
             --output out.bin
             
     #decoding
     htk --gen-action decode --gen-spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn --gen-element TestSeq2
         --gen-input in.bin --gen-output out.json gen-asn1
         
     datagen --action decode --spec /var/local/hydratk/yoda/helpers/yodahelpers/hydratk/extensions/datagen/spec.asn --element TestSeq2 --input in.bin
             --output out.json

* gen_selenium

Method handles command gen-selenium. It uses options gen-input (Selenium script filename, mandatory), gen-output (output filename, optional),
gen-browser (used browser, default Firefox, optional), gen-timeout (timeout for wait commands, default 10, optional).
Creates Adapter object instance and adapts Selenium script to Yoda format (method parse_test_suite).

  .. code-block:: bash
  
     htk --gen-input test.html --gen-output tes.jedi --gen-browser PhantomJS --gen-timeout 5 gen-selenium
     
     datagen --input test.html --output test.jedi --browser PhantomJS --timeout 5 selenium

configuration
^^^^^^^^^^^^^

Configuration is stored in /etc/hydratk/conf.dhydratk-ext-datagen.conf
Currently there are no specific options (extension enabling only).                  