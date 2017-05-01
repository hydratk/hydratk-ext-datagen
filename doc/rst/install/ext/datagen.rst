.. install_ext_datagen:

DataGen
=======

You have 2 options how to install DataGen extension.

Package
^^^^^^^

Install it via Python package managers PIP or easy_install.

  .. code-block:: bash
  
     $ sudo pip install --no-binary :all: hydratk-ext-datagen
     
  .. code-block:: bash
  
     $ sudo easy_install hydratk-ext-datagen
     
  .. note::
  
     PIP needs option --no-binary to run setup.py install.
     Otherwise it runs setup.py bdist_wheel.     

Source
^^^^^^

Download the source code from GitHub or PyPi and install it manually.
Full PyPi URL contains MD5 hash, adapt sample code.

  .. code-block:: bash
  
     $ git clone https://github.com/hydratk/hydratk-ext-datagen.git
     $ cd ./hydratk-ext-datagen
     $ sudo python setup.py install
     
  .. code-block:: bash
  
     $ wget https://python.org/pypi/hydratk-ext-datagen -O hydratk-ext-datagen.tar.gz
     $ tar -xf hydratk-ext-datagen.tar.gz
     $ cd ./hydratk-ext-datagen
     $ sudo python setup.py install
     
  .. note::
  
     Source is distributed with Sphinx (not installed automatically) documentation in directory doc. 
     Type make html to build local documentation however is it recommended to use up to date online documentation.     
     
Requirements
^^^^^^^^^^^^     
     
The extension requires hydratk, hydratk-lib-network. 

.. note::
 
   ASN.1 codec is supported for Python 2.7 only.    
     
Installation
^^^^^^^^^^^^

See installation example, Python 2.7.

  .. code-block:: bash
  
     running install
     running bdist_egg
     running egg_info
     creating src/hydratk_ext_datagen.egg-info
     writing requirements to src/hydratk_ext_datagen.egg-info/requires.txt
     writing src/hydratk_ext_datagen.egg-info/PKG-INFO
     writing top-level names to src/hydratk_ext_datagen.egg-info/top_level.txt
     writing dependency_links to src/hydratk_ext_datagen.egg-info/dependency_links.txt
     writing entry points to src/hydratk_ext_datagen.egg-info/entry_points.txt
     writing manifest file 'src/hydratk_ext_datagen.egg-info/SOURCES.txt'
     reading manifest file 'src/hydratk_ext_datagen.egg-info/SOURCES.txt'
     reading manifest template 'MANIFEST.in'
     writing manifest file 'src/hydratk_ext_datagen.egg-info/SOURCES.txt'
     installing library code to build/bdist.linux-x86_64/egg
     running install_lib
     running build_py
     creating build
     creating build/lib.linux-x86_64-2.7
     creating build/lib.linux-x86_64-2.7/hydratk
     copying src/hydratk/__init__.py -> build/lib.linux-x86_64-2.7/hydratk
     creating build/lib.linux-x86_64-2.7/hydratk/extensions
     copying src/hydratk/extensions/__init__.py -> build/lib.linux-x86_64-2.7/hydratk/extensions
     creating build/lib.linux-x86_64-2.7/hydratk/extensions/datagen
     ...

     creating dist
     creating 'dist/hydratk_ext_datagen-0.1.1-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
     removing 'build/bdist.linux-x86_64/egg' (and everything under it)
     Processing hydratk_ext_datagen-0.1.1-py2.7.egg
     creating /usr/local/lib/python2.7/dist-packages/hydratk_ext_datagen-0.1.1-py2.7.egg
     Extracting hydratk_ext_datagen-0.1.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
     Adding hydratk-ext-datagen 0.1.1 to easy-install.pth file
     Installing datagen script to /usr/local/bin

     Installed /usr/local/lib/python2.7/dist-packages/hydratk_ext_datagen-0.1.1-py2.7.egg
     Processing dependencies for hydratk-ext-datagen==0.1.1
     Searching for hydratk-lib-network==0.2.0
     Best match: hydratk-lib-network 0.2.0
     Processing hydratk_lib_network-0.2.0-py2.7.egg
     hydratk-lib-network 0.2.0 is already the active version in easy-install.pth

     Using /usr/local/lib/python2.7/dist-packages/hydratk_lib_network-0.2.0-py2.7.egg
     Searching for hydratk==0.4.0
     Best match: hydratk 0.4.0
     Processing hydratk-0.4.0-py2.7.egg
     hydratk 0.4.0 is already the active version in easy-install.pth
     Installing htkprof script to /usr/local/bin
     Installing htk script to /usr/local/bin

     Using /usr/local/lib/python2.7/dist-packages/hydratk-0.4.0-py2.7.egg
     Finished processing dependencies for hydratk-ext-datagen==0.1.1 
  
Application installs following (paths depend on your OS configuration)

* datagen command in /usr/local/bin/datagen
* modules in /usr/local/lib/python2.7/dist-packages/hydratk_ext_datagen-0.1.1-py2.7.egg
* configuration file in /etc/hydratk/conf.d/hydratk-ext-datagen.conf   
     
Run
^^^

When installation is finished you can run the application.

Check hydratk-ext-datagen module is installed.   

  .. code-block:: bash
  
     $ pip list | grep hydratk-ext-datagen
     
     hydratk-ext-datagen (0.1.1)
     
Check installed extensions

  .. code-block:: bash
  
     $ htk list-extensions
     
     DataGen: DataGen v0.1.1 (c) [2016 Petr Rašek <bowman@hydratk.org>, HydraTK team <team@hydratk.org>] 
     
Type command htk help and detailed info is displayed.
Type man datagen to display manual page. 

  .. code-block:: bash
  
     $ htk help
     
     Commands:    
        gen-asn1 - encode text file, decode binary file according to ASN.1 specification
           Options:
              --gen-action encode|decode - action
              --gen-element <title> - element title from specification
              --gen-input <path> - input filename
              --gen-spec <path> - specification filename
             [--gen-output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml

        gen-json - generate sample json file according to JSON specification
           Options:
              --gen-spec <path> - specification filename
             [--gen-output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml

        gen-selenium - adapt Selenium script to Yoda format
           Options:
              --gen-input <path> - input filename
              [--gen-browser <title>] - browser to be used, default Firefox
              [--gen-output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml
              [--gen-timeout <number>] - timeout for wait commands, default 10

        gen-xml - generate sample xml file according to WSDL/XSD specification
           Options:
              --gen-element <title> - element title from specification
              --gen-spec <path> - specification filename
             [--gen-envelope] - generate including SOAP envelope
             [--gen-output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml                          

           
You can run DataGen also in standalone mode.  

  .. code-block:: bash
  
     $ datagen help
     
     DataGen v0.1.1
     (c) 2016 Petr Rašek <bowman@hydratk.org>, HydraTK team <team@hydratk.org>
     Usage: datagen [options] command

     Commands:
        asn1 - encode text file, decode binary file according to ASN.1 specification
           Options:
              --action encode|decode - action
              --element <title> - element title from specification
              --input <path> - input filename
              --spec <path> - specification filename
              [--output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml

        help - prints help
        json - generate sample json file according to JSON specification
           Options:
              --spec <path> - specification filename
              [--output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml
              
        selenium - adapt Selenium script to Yoda format
           Options:
              --input <path> - input filename
              [--browser <title>] - browser to be used, default Firefox
              [--output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml
              [--timeout <number>] - timeout for wait commands, default 10              

        xml - generate sample xml file according to WSDL/XSD specification
           Options:
              --element <title> - element title from specification
              --spec <path> - specification filename
              [--envelope] - generate including SOAP envelope
              [--output <path>] - output filename, default input filename with changed suffix or sample.json, sample.xml

     Global Options:
        -c, --config <file> - reads the alternate configuration file
        -d, --debug <level> - debug turned on with specified level > 0
        -e, --debug-channel <channel number, ..> - debug channel filter turned on
        -f, --force - enforces command
        -i, --interactive - turns on interactive mode
        -l, --language <language> - sets the text output language, the list of available languages is specified in the docs
        -m, --run-mode <mode> - sets the running mode, the list of available modes is specified in the docs
                                
Upgrade
=======

Use same procedure as for installation. Use command option --upgrade for pip, easy_install, --force for setup.py.
If configuration file differs from default settings the file is backuped (extension _old) and replaced by default. Adapt the configuration if needed.

Uninstall
=========    

Run command htkuninstall datagen Use option -y if you want to uninstall also dependent Python modules (for advanced user).                                