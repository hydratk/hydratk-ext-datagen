.. _module_ext_datagen_selenium:

Adapter
=======

This sections contains module documentation of adapters/selenium/adapter module.

adapter
^^^^^^^

Module provides class Adapter for adapting Selenium scripts to Yoda format.
It uses external module lxml automatically installed together with hydratk-lib-network.
Unit tests available at hydratk/extensions/datagen/adapters/selenium/01_methods_ut.jedi

**Attributes** :

* _mh - MasterHead reference
* _suite - test suite metadata
* _tests - test cases metadata
* _browser - used browser, default Firefox
* _timeout - timeout for wait commands, default 10

**Properties (Getters)** :

* suite - returns _suite
* tests - returns _tests
* browser - returns _browser
* timeout - returns _browser

**Properties (Setters)**:

* browser - sets _browser
* timeout - sets _timeout

**Methods** :

* __init__

Method sets MasterHead reference.

* parse_test_suite

Method parses Selenium script (test suite file). First fires event adapter_before_parse_suite where parameters suite, outfile can be rewritten.
It uses lxml method fromstring to parse html file and stores metadata to attribute _suite. It uses method parse_test for each test specified in suite.
It prepares Yoda script content using method adapt_suite and creates output file. After that fires event adapter_after_parse_suite and returns bool.

* parse_test

Method parses Selenium script (test case file). First fires event adapter_before_parse_test where parameter test can be rewritten.
It uses lxml method fromstring to parse html file and stores metadata to attribute _tests. It uses method parse_test for each test specified in suite.
After that fires event adapter_after_parse_test and returns bool.

* adapt_suite

Method adapts Selenium suite to Yoda test scenario from template.

* adapt_test

Method adapts Selenium test case to Yoda test case from template.

* adapt_step

Method adapts Selenium test step to Yoda test condition from template.
It uses implemented methods from hydratk.lib.bridge.selen module.

* handle_command

Method prepares test condition content. Each Selenium command has configured handler method.

* cmd_alert

Method handles various commands for alert.

* cmd_close

Method handles command close.

* cmd_echo

Method handles command echo.

* cmd_go_back

Method handles command goBack.

* cmd_open

Method handles command open.

* cmd_pause

Method handles command pause.

* cmd_refresh

Method handles command refresh.

* cmd_set

Method handles various commands for element setting.

* cmd_store

Method handles various commands for data store.

* cmd_verify

Method handles various commands for element verification.

* cmd_wait

Method handles various commands for waiting.