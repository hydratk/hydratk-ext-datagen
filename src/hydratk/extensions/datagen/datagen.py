# -*- coding: utf-8 -*-
"""Extension for data generators

.. module:: datagen.datagen
   :platform: Unix
   :synopsis: Extension for data generators
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

from sys import exit
from hydratk.core import extension, bootstrapper
from hydratk.lib.console.commandlinetool import CommandlineTool
import hydratk.lib.system.config as syscfg

dep_modules = {
    'hydratk': {
        'min-version': '0.5.0',
        'package': 'hydratk'
    },
    'hydratk.lib.network': {
        'min-version': '0.2.0',
        'package': 'hydratk-lib-network'
    }
}


class Extension(extension.Extension):
    """Class Extension
    """

    def _init_extension(self):
        """Method initializes extension

        Args:            
           none

        Returns:
           void    

        """

        self._ext_id = 'datagen'
        self._ext_name = 'DataGen'
        self._ext_version = '0.1.2'
        self._ext_author = 'Petr Rašek <bowman@hydratk.org>, HydraTK team <team@hydratk.org>'
        self._ext_year = '2016-2017'

        if (not self._check_dependencies()):
            exit(0)

    def _check_dependencies(self):
        """Method checks dependent modules

        Args:            
           none

        Returns:
           bool    

        """

        return bootstrapper._check_dependencies(dep_modules, 'hydratk-ext-datagen')

    def _uninstall(self):
        """Method returns additional uninstall data 

        Args:            
           none

        Returns:
           tuple: list (files), list (modules)  

        """

        files = [
            '/usr/share/man/man1/datagen.1',
            '{0}/hydratk/conf.d/hydratk-ext-datagen.conf'.format(syscfg.HTK_ETC_DIR)
        ]

        return files, dep_modules

    def _register_actions(self):
        """Method registers actions

        Args:
           none            

        Returns:
           void    

        """

        if (self._mh.cli_cmdopt_profile == 'datagen'):
            self._register_standalone_actions()
        else:
            self._register_htk_actions()

    def _register_htk_actions(self):
        """Method registers command hooks

        Args:  
           none        

        Returns:
           void

        """

        self._mh.match_cli_command('gen-asn1')
        self._mh.match_cli_command('gen-json')
        self._mh.match_cli_command('gen-xml')
        self._mh.match_cli_command('gen-selenium')

        hook = [
            {'command': 'gen-asn1', 'callback': self.gen_asn1},
            {'command': 'gen-json', 'callback': self.gen_json},
            {'command': 'gen-xml', 'callback': self.gen_xml},
            {'command': 'gen-selenium', 'callback': self.gen_selenium}
        ]
        self._mh.register_command_hook(hook)

        self._mh.match_long_option('gen-spec', True, 'gen-spec')
        self._mh.match_long_option('gen-input', True, 'gen-input')
        self._mh.match_long_option('gen-output', True, 'gen-output')
        self._mh.match_long_option('gen-action', True, 'gen-action')
        self._mh.match_long_option('gen-element', True, 'gen-element')
        self._mh.match_long_option('gen-envelope', False, 'gen-envelope')
        self._mh.match_long_option('gen-browser', True, 'gen-browser')
        self._mh.match_long_option('gen-timeout', True, 'gen-timeout')

    def _register_standalone_actions(self):
        """Method registers command hooks for standalone mode

        Args:  
           none        

        Returns:
           void

        """

        option_profile = 'datagen'
        help_title = '{h}' + self._ext_name + ' v' + self._ext_version + '{e}'
        cp_string = '{u}' + "(c) " + self._ext_year + \
            " " + self._ext_author + '{e}'
        self._mh.set_cli_appl_title(help_title, cp_string)

        self._mh.match_cli_command('asn1', option_profile)
        self._mh.match_cli_command('json', option_profile)
        self._mh.match_cli_command('xml', option_profile)
        self._mh.match_cli_command('selenium', option_profile)

        hook = [
            {'command': 'asn1', 'callback': self.gen_asn1},
            {'command': 'json', 'callback': self.gen_json},
            {'command': 'xml', 'callback': self.gen_xml},
            {'command': 'selenium', 'callback': self.gen_selenium}
        ]
        self._mh.register_command_hook(hook)

        self._mh.match_cli_command('help', option_profile)

        self._mh.match_long_option(
            'spec', True, 'gen-spec', False, option_profile)
        self._mh.match_long_option(
            'input', True, 'gen-input', False, option_profile)
        self._mh.match_long_option(
            'output', True, 'gen-output', False, option_profile)
        self._mh.match_long_option(
            'action', True, 'gen-action', False, option_profile)
        self._mh.match_long_option(
            'element', True, 'gen-element', False, option_profile)
        self._mh.match_long_option(
            'envelope', False, 'gen-envelope', False, option_profile)
        self._mh.match_long_option(
            'browser', True, 'gen-browser', False, option_profile)
        self._mh.match_long_option(
            'timeout', True, 'gen-timeout', False, option_profile)

        self._mh.match_cli_option(
            ('c', 'config'), True, 'config', False, option_profile)
        self._mh.match_cli_option(
            ('d', 'debug'), True, 'debug', False, option_profile)
        self._mh.match_cli_option(
            ('e', 'debug-channel'), True, 'debug-channel', False, option_profile)
        self._mh.match_cli_option(
            ('l', 'language'), True, 'language', False, option_profile)
        self._mh.match_cli_option(
            ('m', 'run-mode'), True, 'run-mode', False, option_profile)
        self._mh.match_cli_option(
            ('f', 'force'), False, 'force', False, option_profile)
        self._mh.match_cli_option(
            ('i', 'interactive'), False, 'interactive', False, option_profile)
        self._mh.match_cli_option(
            ('h', 'home'), False, 'home', False, option_profile)

    def gen_asn1(self):
        """Method handles command gen-asn1

        Encode text file, decode binary file according to ASN.1 specification

        Args:
           none

        Returns:
           void                 

        """

        self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
            'datagen_received_cmd', 'gen-asn1'), self._mh.fromhere())

        action = CommandlineTool.get_input_option('gen-action')
        spec = CommandlineTool.get_input_option('gen-spec')
        element = CommandlineTool.get_input_option('gen-element')
        input = CommandlineTool.get_input_option('gen-input')
        output = CommandlineTool.get_input_option('gen-output')

        if (not action):
            print('Missing option action')
        elif (action not in ['encode', 'decode']):
            print('Action not in encode|decode')
        elif (not spec):
            print('Missing option spec')
        elif (not element):
            print('Missing option element')
        elif (not input):
            print('Missing option input')
        else:

            from hydratk.extensions.datagen.asn1codec import ASN1Codec

            codec = ASN1Codec()
            if (codec.import_spec(spec)):
                output = None if (not output) else output
                if (action == 'encode'):
                    result = codec.encode(input, element, output)
                elif (action == 'decode'):
                    result = codec.decode(input, element, output)

                if (not result):
                    print('{0} error'.format(action))
                else:
                    print('{0} finished'.format(action))
            else:
                print('Import specification error')

    def gen_json(self):
        """Method handles command gen-json

        Generate sample JSON file according to JSON specification  

        Args:
           none

        Returns:
           void                 

        """

        self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
            'datagen_received_cmd', 'gen-json'), self._mh.fromhere())

        spec = CommandlineTool.get_input_option('gen-spec')
        output = CommandlineTool.get_input_option('gen-output')

        if (not spec):
            print('Missing option spec')
        else:

            from hydratk.extensions.datagen.jsongen import JSONGen

            gen = JSONGen()
            if (gen.import_schema(spec)):
                output = None if (not output) else output
                if (not gen.tojson(output)):
                    print('Generation error')
                else:
                    print('Sample generated')
            else:
                print('Import specification error')

    def gen_xml(self):
        """Method handles command gen-xml

        Generate sample XML file according to WSDL/XSD specification 

        Args:
           none

        Returns:
           void                  

        """

        self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
            'datagen_received_cmd', 'gen-xml'), self._mh.fromhere())

        spec = CommandlineTool.get_input_option('gen-spec')
        element = CommandlineTool.get_input_option('gen-element')
        output = CommandlineTool.get_input_option('gen-output')
        envelope = CommandlineTool.get_input_option('gen-envelope')

        if (not spec):
            print('Missing option spec')
        elif (not element):
            print('Missing option element')
        else:

            from hydratk.extensions.datagen.xmlgen import XMLGen

            gen = XMLGen()
            if (gen.import_spec(spec)):
                output = None if (not output) else output
                if (not gen.toxml(element, output, envelope)):
                    print('Generation error')
                else:
                    print('Sample generated')
            else:
                print('Import specification error')

    def gen_selenium(self):
        """Method handles command gen-selenium

        Adapt Selenium script to Yoda format

        Args:
           none

        Returns:
           void                  

        """

        self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
            'datagen_received_cmd', 'gen-selenium'), self._mh.fromhere())

        input = CommandlineTool.get_input_option('gen-input')
        output = CommandlineTool.get_input_option('gen-output')
        browser = CommandlineTool.get_input_option('gen-browser')
        timeout = CommandlineTool.get_input_option('gen-timeout')

        if (not input):
            print('Missing option input')
        else:

            from hydratk.extensions.datagen.adapters.selenium.adapter import Adapter

            a = Adapter()
            if (browser):
                a.browser = browser
            if (timeout):
                a.timeout = timeout

            output = None if (not output) else output
            if (a.parse_test_suite(input, output)):
                print('Script adapted')
            else:
                print('Script adaption error')
