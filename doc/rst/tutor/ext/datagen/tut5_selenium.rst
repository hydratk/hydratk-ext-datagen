.. _tutor_datagen_tut5_selenium:

Tutorial 5: Selenium
====================

Adapter of Selenium scripts (used by Firefox IDE plugin) to Yoda format

Command line
^^^^^^^^^^^^

It is controlled via command gen-selenium with following options. 

Mandatory:

* --input <path>: path to Selenium script

Optional:

* --gen-output <path>: path to output file, default <test suite>.jedi
* --gen-browser <title>: browser to be used, default Firefox
* --gen-timeout <number>: timeout for wait commands, default 10

Adapter
^^^^^^^

  .. code-block:: bash
  
     $ htk --gen-input test.html --gen-output test.jedi gen-selenium 
     
     Script adapted
     
     $ htk --gen-input test.html --gen-browser PhantomJS --gen-timeout 5 gen-selenium 
     
     Script adapted     
     
Adapter supports the commands which are currently supported by plugin export capability to Python unittest.
See file hydratk.extensions.datagen.adapters.selenium.config for full list of supported commands (dictionary mapping, value != cmd_dummy).
If adapter detects not supported command the info is printed. Adapt generated file or remove the command from original file. 