# -*- coding: utf-8 -*-
"""Adapter for Selenium scripts to Yoda

.. module:: datagen.adapters.selenium.adapter
   :platform: Unix
   :synopsis: Adapter for Selenium scripts
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

"""
Events:
-------
adapter_before_parse_suite
adapter_after_parse_suite
adapter_before_parse_test
adapter_after_parse_test

"""

from hydratk.core.masterhead import MasterHead
from hydratk.core import event
import hydratk.extensions.datagen.adapters.selenium.config as cfg
from lxml.html import fromstring
from os import path
from sys import version_info


class Adapter(object):
    """Class Adapter
    """

    _mh = None
    _suite = None
    _tests = None
    _browser = 'Firefox'
    _timeout = 10

    def __init__(self):
        """Class constructor

        Called when object is initialized

        Args:
           browser (str): browser to be used
           timeout (str): timeout fow wait commands              

        """

        self._mh = MasterHead.get_head()

    @property
    def suite(self):
        """ suite property getter """

        return self._suite

    @property
    def tests(self):
        """ tests property getter """

        return self._tests

    @property
    def browser(self):
        """ browser property getter """

        return self._browser

    @browser.setter
    def browser(self, value):
        """ browser property setter """

        self._browser = value

    @property
    def timeout(self):
        """ timeout property getter """

        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """ timeout property setter """

        self._timeout = value

    def parse_test_suite(self, suite, outfile=None):
        """Method parses test suite file

        Args:
            suite (str): suite filename
            outfile (str): output filename, <test suite>.jedi

        Returns:
            bool: result

        Raises:
            event: adapter_before_parse_suite
            event: adapter_after_parse_suite     

        """

        try:

            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
                'datagen_adapter_parsing_suite', suite), self._mh.fromhere())
            ev = event.Event('adapter_before_parse_suite', suite, outfile)
            if (self._mh.fire_event(ev) > 0):
                suite = ev.argv(0)
                outfile = ev.argv(1)

            if (ev.will_run_default()):

                if (path.exists(suite)):
                    with open(suite, 'r') as f:
                        doc = fromstring(f.read()) if (version_info[0] == 2) else fromstring(
                            bytes(bytearray(f.read(), encoding='utf-8')))
                else:
                    raise ValueError('File {0} not found'.format(suite))

                rows = doc.xpath('//table/tbody/tr/td')
                self._suite = {
                    'file': suite, 'title': rows[0].xpath('b')[0].text}

                self._tests = []
                for row in rows[1:]:
                    elem = row.xpath('a')[0]
                    test = {'title': elem.text, 'file': elem.attrib['href']}
                    test['url'], test['steps'] = self.parse_test(
                        path.join(path.dirname(suite), test['file']))
                    self._tests.append(test)

                scenario = self.adapt_suite(self._suite, self._tests)
                outfile = outfile if (
                    outfile != None) else self._suite['title'] + '.jedi'
                with open(outfile, 'w') as f:
                    f.write(scenario)

            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
                'datagen_adapter_suite_parsed'), self._mh.fromhere())
            ev = event.Event('adapter_after_parse_suite')
            self._mh.fire_event(ev)

            return True

        except (Exception, ValueError) as ex:
            self._mh.dmsg(
                'htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False

    def parse_test(self, test):
        """Method parses test file

        Args:
            test (str): test filename

        Returns:
            tuple: url (str), steps (list)

        Raises:
            event: adapter_before_parse_test
            event: adapter_after_parse_test    

        """

        try:

            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
                'datagen_adapter_parsing_test', test), self._mh.fromhere())
            ev = event.Event('adapter_before_parse_test', test)
            if (self._mh.fire_event(ev) > 0):
                test = ev.argv(0)

            if (ev.will_run_default()):

                if (path.exists(test)):
                    with open(test, 'r') as f:
                        doc = fromstring(f.read()) if (version_info[0] == 2) else fromstring(
                            bytes(bytearray(f.read(), encoding='utf-8')))
                else:
                    raise ValueError('File {0} not found'.format(test))

                url = doc.xpath('//head/link')[0].attrib['href']
                rows = doc.xpath('//table/tbody/tr')
                steps = []

                for row in rows:
                    cols = row.xpath('td')
                    step = {'command': cols[0].text, 'target': cols[
                        1].text, 'value': cols[2].text}
                    steps.append(step)

            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg(
                'datagen_adapter_test_parsed'), self._mh.fromhere())
            ev = event.Event('adapter_after_parse_test')
            self._mh.fire_event(ev)

            return url, steps

        except (Exception, ValueError) as ex:
            self._mh.dmsg(
                'htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return None

    def adapt_suite(self, suite, tests):
        """Method adapts suite to scenario

        Args:
            suite (dict): suite
            tests (list): tests

        Returns:
            str   

        """

        cases = ''
        for i in range(0, len(tests)):
            cases += self.adapt_test(i, tests[i])

        scenario = cfg.tmpl_scenario.format(
            title=suite['title'], pre_req=cfg.tmpl_pre_req, cases=cases)

        return scenario

    def adapt_test(self, idx, test):
        """Method adapts test to case

        Args:
            idx (int): index
            test (dict): test

        Returns:
            str   

        """

        conditions = ''
        for i in range(0, len(test['steps'])):
            conditions += self.adapt_step(i, test['steps'][i], test['url'])

        case = '  ' if (idx > 0) else ''
        case += cfg.tmpl_case.format(idx=idx + 1,
                                     title=test['title'], conditions=conditions)

        return case

    def adapt_step(self, idx, step, url):
        """Method adapts step to condition

        Args:
            idx (int): index
            step (dict): step
            url (str): base url

        Returns:
            str   

        """

        condition = '    ' if (idx > 0) else ''
        test, validate = self.handle_command(step, url)
        condition += cfg.tmpl_condition.format(
            idx=idx + 1, title=step['command'], test=test, validate=validate)

        return condition

    def handle_command(self, step, url):
        """Method handles command

        Args:
            step (dict): step
            url (str): base url

        Returns:
            tuple: test (str), validate (str)   

        """

        handler = cfg.mapping[step['command']] if (
            step['command'] in cfg.mapping) else None
        if (handler == None):
            print(
                self._mh._trn.msg('datagen_adapter_cmd_unknown', step['command']))
            test, validate = """print('Unknown command: {0}')""".format(
                step['command']), """assert False"""
        elif (handler == 'cmd_dummy'):
            print(
                self._mh._trn.msg('datagen_adapter_cmd_dummy', step['command']))
            test, validate = """print('Not supported command: {0}')""".format(
                step['command']), """assert False"""
        else:
            test, validate = getattr(self, handler)(step, url)

        return test, validate

    def cmd_alert(self, step, *args):
        """Method handles commands alert

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        command = step['command']
        if (command in ['assertAlert', 'assertConfirmation', 'assertNotAlert', 'assertNotConfirmation',
                        'verifyAlert', 'verifyNotAlert', 'verifyNotConfirmation']):
            test = """res = c.check_alert()[1]"""
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'alert = {1}'""".format(
                        step['target'], step['target'])
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'alert != {1}'""".format(
                        step['target'], step['target'])
        elif (command in ['assertAlertNotPresent', 'assertAlertPresent', 'assertConfirmationNotPresent', 'assertConfirmationPresent',
                          'verifyAlertNotPresent', 'verifyAlertPresent', 'verifyConfirmation', 'verifyConfirmationNotPresent', 'verifyConfirmationPresent']):
            test = """res = c.check_alert()[0]"""
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (not res), 'alert present'"""
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res), 'alert not present'"""
        elif (command in ['chooseCancelOnNextConfirmation', 'chooseOkOnNextConfirmation', 'chooseOkOnNextConfirmationAndWait']):
            if ('Cancel' in command):
                test = """c.confirm_alert = True
        res = c.confirm_alert"""
                validate = cfg.tmpl_validate + \
                    """assert (res), 'confirm_alert != True'"""
            else:
                test = """c.confirm_alert = False
        res = c.confirm_alert"""
                validate = cfg.tmpl_validate + \
                    """assert (not res), 'confirm_alert != False'"""

        return test, validate

    def cmd_close(self, step, *args):
        """Method handles command close

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """res = c.close()"""
        validate = cfg.tmpl_validate + """assert (res), 'browser not closed'"""

        return test, validate

    def cmd_echo(self, step, *args):
        """Method handles command echo

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """print('{0}')""".format(step['target'])
        validate = """this.test_result = True
        assert (res), 'text not printed'"""

        return test, validate

    def cmd_go_back(self, step, *args):
        """Method handles command goBack

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """res = c.go_back()"""
        validate = cfg.tmpl_validate + \
            """assert (res), 'previous page not displayed'"""

        return test, validate

    def cmd_open(self, step, url, *args):
        """Method handles command open

        Args:
            step (dict): step
            url (str): base url
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """c = SeleniumBridge('{0}')
        res = c.open('{1}')""".format(self._browser, url + step['target'])
        validate = cfg.tmpl_validate + \
            """assert (res), 'page {0} not opened'""".format(
                url + step['target'])

        return test, validate

    def cmd_pause(self, step, *args):
        """Method handles command pause

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """sleep({0})""".format(float(step['target']) / 1000)
        validate = """this.test_result = True
        assert (this.test_result), 'processing not paused'"""

        return test, validate

    def cmd_refresh(self, step, *args):
        """Method handles command goBack

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        test = """res = c.refresh()"""
        validate = cfg.tmpl_validate + """assert (res), 'page not refreshed'"""

        return test, validate

    def cmd_set(self, step, *args):
        """Method handles various commands set

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        command, target = step['command'], step['target'].split(
            '=') if (step['target'] != None) else ''
        if (target != ''):
            if (target[0] in ['id', 'name', 'link', 'css'] or target[0][0] == '/'):
                if (target[0][0] == '/'):
                    method = 'xpath'
                elif (target[0] == 'link'):
                    method = 'text'
                else:
                    method = target[0]
                ident = target[1] if (method != 'xpath') else step['target']
            else:
                target = target[0]
        value = step['value'] if (step['value'] != None) else ''

        if (command in ['sendKeys', 'sendKeysAndWait', 'type', 'typeAndWait']):
            test = """res = c.set_element('{0}', '{1}', method='{2}')""".format(
                ident, value, method)
        elif (command in ['check', 'checkAndWait', 'uncheck', 'uncheckAndWait']):
            test = """res = c.set_element('{0}', method='{1}', el_type='checkbox')""".format(
                ident, method)
        elif (command in ['click', 'clickAndWait', 'submit', 'submitAndWait']):
            test = """res = c.set_element('{0}', method='{1}', el_type='submit')""".format(
                ident, method)
        elif (command in ['select', 'selectAndWait']):
            test = """res = c.set_element('{0}', '{1}', method='{2}', el_type='select')""".format(
                ident, value, method)

        validate = cfg.tmpl_validate + \
            """assert (res), 'element {0} not set'""".format(ident)

        return test, validate

    def cmd_store(self, step, *args):
        """Method handles various commands store

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        command, target = step['command'], step['target'].split(
            '=') if (step['target'] != None) else ''
        if (target != ''):
            if (target[0] in ['id', 'name', 'link', 'css'] or target[0][0] == '/'):
                if (target[0][0] == '/'):
                    method = 'xpath'
                elif (target[0] == 'link'):
                    method = 'text'
                else:
                    method = target[0]
                ident = target[1] if (method != 'xpath') else step['target']
            else:
                target = target[0]
        value = step['value'] if (step['value'] != None) else ''

        if (command in ['store']):
            test = """my.pocket.content['{0}'] = '{1}'""".format(value, target)
            validate = """this.test_result = True
        assert (res), 'value not stored'"""
        elif (command in ['storeText']):
            test = """res = c.read_element('{0}', '{1}')
        my.pocket.content['{2}'] = res""".format(ident, method, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'element not stored'"""
        elif (command in ['storeElementPresent']):
            test = """res = c.get_element('{0}', '{1}')
        my.pocket.content['{2}'] = res != None""".format(ident, method, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'element presence not stored'"""
        elif (command in ['storeAttribute']):
            target = ident.split('@')
            ident, attr = target[0], target[1]
            test = """res = c.get_element('{0}', '{1}').get_attribute('{2}')
        my.pocket.content['{3}'] = res""".format(ident, method, attr, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'attribute not stored'"""
        elif (command in ['storeAlert', 'storeConfirmation']):
            test = """res, value = c.check_alert()
        my.pocket.content['{0}'] = value""".format(target)
            validate = cfg.tmpl_validate + \
                """assert (res), 'alert not stored'"""
        elif (command in ['storeAlertPresent', 'storeConfirmationPresent']):
            test = """res = c.check_alert()[0]
        my.pocket.content['{0}'] = res""".format(target)
            validate = cfg.tmpl_validate + \
                """assert (res), 'alertPresent not stored'"""
        elif (command in ['storeBodyText']):
            test = """res = c.read_element('BODY', 'tag')
        my.pocket.content['{0}'] = res""".format(target)
            validate = cfg.tmpl_validate + \
                """assert (res), 'body not stored'"""
        elif (command in ['storeChecked']):
            test = """res = c.get_element('{0}', '{1}').is_selected()
        my.pocket.content['{2}'] = res""".format(ident, method, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'status not stored'"""
        elif (command in ['storeLocation']):
            test = """res = c.get_current_url()
        my.pocket.content['{0}'] = res""".format(target)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'location not stored'"""
        elif (command in ['storeTitle']):
            test = """res = c.get_title()
        my.pocket.content['{0}'] = res""".format(target)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'title not stored'"""
        elif (command in ['storeValue']):
            test = """res = c.get_element('{0}', '{1}').get_attribute('value')
        my.pocket.content['{2}'] = res""".format(ident, method, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'value not stored'"""
        elif (command in ['storeVisible']):
            test = """res = c.get_element('{0}', '{1}').is_displayed()
        my.pocket.content['{2}'] = res""".format(ident, method, value)
            validate = cfg.tmpl_validate + \
                """assert (res != None), 'visibility not stored'"""
        elif (command in ['storeXpathCount']):
            test = """res = c.get_element('{0}', 'xpath', False)  
        my.pocket.content['{1}'] = len(res) if (res != None) else 0""".format(ident, value)
            validate = """this.test_result = len(res) if (res != None) else 0 
        assert (res != None), 'count not stored'"""

        return test, validate

    def cmd_verify(self, step, *args):
        """Method handles various commands verify, assert

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        command, target = step['command'], step['target'].split(
            '=') if (step['target'] != None) else ''
        if (target != ''):
            if (target[0] in ['id', 'name', 'link', 'css'] or target[0][0] == '/'):
                if (target[0][0] == '/'):
                    method = 'xpath'
                elif (target[0] == 'link'):
                    method = 'text'
                else:
                    method = target[0]
                ident = target[1] if (method != 'xpath') else step['target']
            else:
                target = target[0]
        value = step['value'] if (step['value'] != None) else ''

        if (command in ['assertNotText', 'assertText', 'verifyNotText', 'verifyText']):
            test = """res = c.read_element('{0}', '{1}')""".format(
                ident, method)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'element {1} = {2}'""".format(
                        value, ident, value)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'element {1} != {2}'""".format(
                        value, ident, value)
        elif (command in ['assertElementPresent', 'assertElementNotPresent', 'verifyElementNotPresent', 'verifyElementPresent']):
            test = """res = c.get_element('{0}', '{1}')""".format(
                ident, method)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (res == None), 'element {0} present'""".format(
                        ident)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res != None), 'element {0} not present'""".format(
                        ident)
        elif (command in ['assertAttribute', 'assertNotAttribute', 'verifyAttribute', 'verifyNotAttribute']):
            target = ident.split('@')
            ident, attr = target[0], target[1]
            test = """res = c.get_element('{0}', '{1}').get_attribute('{2}')""".format(
                ident, method, attr)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'element {1} attribute {2} = {3}'""".format(
                        value, ident, attr, value)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'element {1} attribute {2} != {3}'""".format(
                        value, ident, attr, value)
        elif (command in ['assertBodyText', 'assertNotBodyText', 'verifyBodyText', 'verifyNotBodyText']):
            test = """res = c.read_element('BODY', 'tag')"""
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'body = {1}'""".format(
                        target, target)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'body != {1}'""".format(
                        target, target)
        elif (command in ['assertChecked', 'assertNotChecked', 'assertNotSelected',
                          'verifyChecked', 'verifyNotChecked']):
            test = """res = c.get_element('{0}', '{1}').is_selected()""".format(
                ident, method)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (not res), 'element {0} selected'""".format(
                        ident)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res), 'element {0} not selected'""".format(
                        ident)
        elif (command in ['assertLocation', 'assertNotLocation', 'verifyLocation', 'verifyNotLocation']):
            test = """res = c.get_current_url()"""
            if ('Not' in step['command']):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'URL = {1}'""".format(
                        target, target)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'URL != {1}'""".format(
                        target, target)
        elif (command in ['assertNotTitle', 'assertTitle', 'verifyNotTitle', 'verifyTitle']):
            test = """res = c.get_title()"""
            if ('Not' in step['command']):
                validate = cfg.tmpl_validate + \
                    """assert (res != '{0}'), 'title = {1}'""".format(
                        target, target)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res == '{0}'), 'title != {1}'""".format(
                        target, target)
        elif (command in ['assertNotValue', 'assertValue', 'verifyNotValue', 'verifyValue']):
            test = """res = c.get_element('{0}', '{1}').get_attribute('value')""".format(
                ident, method)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (not res), 'element {0} checked'""".format(ident)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res), 'element {0} not checked'""".format(ident)
        elif (command in ['assertNotVisible', 'assertVisible', 'verifyNotVisible', 'verifyVisible']):
            test = """res = c.get_element('{0}', '{1}').is_displayed()""".format(
                ident, method)
            if ('Not' in command):
                validate = cfg.tmpl_validate + \
                    """assert (not res), 'element {0} visible'""".format(ident)
            else:
                validate = cfg.tmpl_validate + \
                    """assert (res), 'element {0} not visible'""".format(ident)
        elif (command in ['assertNotXpathCount', 'assertXpathCount', 'verifyNotXpathCount', 'verifyXpathCount']):
            test = """res = c.get_element('{0}', 'xpath', False)""".format(
                ident)
            if ('Not' in command):
                validate = """this.test_result = len(res) if (res != None) else 0 
        assert (this.test_result != {0}), 'element {1} count = {2}'""".format(value, ident, value)
            else:
                validate = """this.test_result = len(res) if (res != None) else 0 
        assert (this.test_result == {0}), 'element {1} count != {2}'""".format(value, ident, value)

        return test, validate

    def cmd_wait(self, step, *args):
        """Method handles various commands wait

        Args:
            step (dict): step
            args (args): arguments

        Returns:
            tuple: test (str), validate (str)   

        """

        command, target = step['command'], step['target'].split(
            '=') if (step['target'] != None) else ''
        if (target != ''):
            if (target[0] in ['id', 'name', 'link', 'css'] or target[0][0] == '/'):
                if (target[0][0] == '/'):
                    method = 'xpath'
                elif (target[0] == 'link'):
                    method = 'text'
                else:
                    method = target[0]
                ident = target[1] if (method != 'xpath') else step['target']
            else:
                target = target[0]
        value = step['value'] if (step['value'] != None) else ''

        test = """res = False
        for i in range({0}): 
            try:
                if ({1}):
                    res = True
                    break
            except:
                pass
            sleep(1)"""

        if (command in ['waitForElementNotPresent', 'waitForElementPresent']):
            if ('Not' in command):
                cond = """c.get_element('{0}', '{1}') == None""".format(
                    ident, method)
            else:
                cond = """c.get_element('{0}', '{1}') != None""".format(
                    ident, method)
        elif (command in ['waitForNotText', 'waitForText']):
            if ('Not' in command):
                cond = """c.read_element('{0}', '{1}') != '{2}'""".format(
                    ident, method, value)
            else:
                cond = """c.read_element('{0}', '{1}') == '{2}'""".format(
                    ident, method, value)
        elif (command in ['waitForAlert', 'waitForConfirmation', 'waitForNotAlert', 'waitForNotConfirmation']):
            cond = """c.check_alert() == (True, '{0}')""".format(target)
        elif (command in ['waitForAlertNotPresent', 'waitForAlertPresent', 'waitForConfirmationNotPresent', 'waitForConfirmationPresent']):
            if ('Not' in command):
                cond = """c.check_alert()[0] == False"""
            else:
                cond = """c.check_alert()[0] == True"""
        elif (command in ['waitForAttribute', 'waitForNotAttribute']):
            target = ident.split('@')
            ident, attr = target[0], target[1]
            if ('Not' in command):
                cond = """c.get_element('{0}', '{1}').get_attribute('{2}') != '{3}'""".format(
                    ident, method, attr, value)
            else:
                cond = """c.get_element('{0}', '{1}').get_attribute('{2}') == '{3}'""".format(
                    ident, method, attr, value)
        elif (command in ['waitForBodyText', 'waitForNotBodyText']):
            if ('Not' in command):
                cond = """c.read_element('BODY', 'tag') != '{0}'""".format(
                    target)
            else:
                cond = """c.read_element('BODY', 'tag') == '{0}'""".format(
                    target)
        elif (command in ['waitForChecked', 'waitForNotChecked']):
            if ('Not' in command):
                cond = """c.get_element('{0}', '{1}').is_selected() == False""".format(
                    ident, method)
            else:
                cond = """c.get_element('{0}', '{1}').is_selected() == True""".format(
                    ident, method)
        elif (command in ['waitForLocation', 'waitForNotLocation']):
            if ('Not' in command):
                cond = """c.get_current_url() != '{0}'""".format(target)
            else:
                cond = """c.get_current_url() == '{0}'""".format(target)
        elif (command in ['waitForNotTitle', 'waitForTitle']):
            if ('Not' in command):
                cond = """c.get_title() != '{0}'""".format(target)
            else:
                cond = """c.get_title() == '{0}'""".format(target)
        elif (command in ['waitForNotValue', 'waitForValue']):
            if ('Not' in command):
                cond = """c.get_element('{0}', '{1}').get_attribute('value') == False""".format(
                    ident, method)
            else:
                cond = """c.get_element('{0}', '{1}').get_attribute('value') == True""".format(
                    ident, method)
        elif (command in ['waitForNotVisible', 'waitForVisible']):
            if ('Not' in command):
                cond = """c.get_element('{0}', '{1}').is_displayed() == False""".format(
                    ident, method)
            else:
                cond = """c.get_element('{0}', '{1}').is_displayed() == True""".format(
                    ident, method)
        elif (command in ['waitForNotXpathCount', 'waitForXpathCount']):
            if ('Not' in command):
                cond = """len(c.get_element('{0}', 'xpath', False)) != {1}""".format(
                    ident, value)
            else:
                cond = """len(c.get_element('{0}', 'xpath', False)) == {1}""".format(
                    ident, value)

        test = test.format(self._timeout, cond)
        validate = """this.test_result = res
        assert (this.test_result), 'timed out'"""

        return test, validate
