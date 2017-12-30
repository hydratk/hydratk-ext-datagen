# -*- coding: utf-8 -*-
"""Module for ASN.1 codec

.. module:: datagen.asn1codec
   :platform: Unix
   :synopsis: Module for ASN.1 codec
              Uses tool ffasn1dump (created by Fabrice Bellard) from https://bellard.org/ffasn1/ffasn1dump.html
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

"""
Events:
-------
asn1_before_compile
asn1_after_compile
asn1_before_decode
asn1_after_decode
asn1_before_encode
asn1_after_encode
asn1_before_transcode
asn1_after_transcode

"""

from hydratk.core.masterhead import MasterHead
from hydratk.core import event
from subprocess import Popen, PIPE
from os import path

class ASN1Codec(object):
    """Class ASN1Codec
    """

    _mh = None
    _path = None

    def __init__(self):
        """Class constructor

        Called when object is initialized

        Args:   
           none         

        Raises:
           ValueError

        """

        self._mh = MasterHead.get_head()
        self._path = self._mh.cfg['Extensions']['DataGen']['ffasn1dump_path']

        if (not path.exists(self._path)):
            raise ValueError('File {0} not found'.format(self._path))

    @property
    def path(self):
        """ path property getter """

        return self._path

    def compile(self, spec):
        """Method compiles ASN.1 specification for validation

        Args:
            spec (str): specification filename

        Returns: 
            bool: result

        Raises: 
            event: asn1_before_compile
            event: asn1_after_compile

        """

        try:
            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_compile', spec), self._mh.fromhere())
            ev = event.Event('asn1_before_compile', spec)
            if (self._mh.fire_event(ev) > 0):
                spec = ev.argv(0)

            if (ev.will_run_default()):
                if (path.exists(spec)):
                    cmd = '{0} {1}'.format(self._path, spec)
                    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
                    out, err = p.communicate()
                    if (err != None and len(err) > 0):
                        raise ValueError(err)
                else:
                    raise ValueError('File {0} not found'.format(spec))

            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_compiled'), self._mh.fromhere())
            ev = event.Event('asn1_after_compile')
            self._mh.fire_event(ev)

            return True

        except (Exception, ValueError) as ex:
            self._mh.demsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False

    def decode(self, spec, element, input, iformat='ber', output=None):
        """Method decodes ASN.1 file to readable GSER format

        Args:
            spec (str): specification filename
            element (str): element title
            input (str): input filename
            iformat (str): input format ber|der|oer|aper|uper|xer
            output (str): output filename

        Returns:
            bool: result

        Raises:
            event: asn1_before_decode
            event: asn1_after_decode

        """

        try:
            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_decode', input, iformat, element, spec), self._mh.fromhere())
            ev = event.Event('asn1_before_decode', spec, element, input, iformat, output)
            if (self._mh.fire_event(ev) > 0):
                spec = ev.argv(0)
                element = ev.argv(1)
                input = ev.argv(2)
                iformat = ev.argv(3)
                output = ev.argv(4)

            if (ev.will_run_default()):
                if (path.exists(spec)):
                    if (path.exists(input)):
                        output = (input.split('/')[-1]).split('.')[0] + '.gser' if (output == None) else output
                        cmd = '{0} -I {1} -O gser {2} {3} {4} {5}'.format(self._path, iformat, spec, element, input, output)
                        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                        out, err = p.communicate()
                        if (err != None and len(err) > 0):
                            raise ValueError(err)                        
                    else:
                        raise ValueError('File {0} not found'.format(input))
                else:
                    raise ValueError('File {0} not found'.format(spec))

            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_decoded', output), self._mh.fromhere())
            ev = event.Event('asn1_after_decode')
            self._mh.fire_event(ev)

            return True

        except (Exception, ValueError) as ex:
            self._mh.demsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False

    def encode(self, spec, element, input, oformat='ber', output=None):
        """Method encodes ASN.1 file from readable GSER format

        Args:
            spec (str): specification filename
            element (str): element title
            input (str): input filename
            oformat (str): output format ber|der|oer|aper|uper|xer
            output (str): output filename

        Returns:
            bool: result

        Raises:
            event: asn1_before_encode
            event: asn1_after_encode

        """

        try:
            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_encode', input, oformat, element, spec), self._mh.fromhere())
            ev = event.Event('asn1_before_encode', spec, element, input, oformat, output)
            if (self._mh.fire_event(ev) > 0):
                spec = ev.argv(0)
                element = ev.argv(1)
                input = ev.argv(2)
                oformat = ev.argv(3)
                output = ev.argv(4)

            if (ev.will_run_default()):
                if (path.exists(spec)):
                    if (path.exists(input)):
                        output = (input.split('/')[-1]).split('.')[0] + '.' + oformat if (output == None) else output
                        cmd = '{0} -I gser -O {1} {2} {3} {4} {5}'.format(self._path, oformat, spec, element, input, output)
                        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                        out, err = p.communicate()
                        if (err != None and len(err) > 0):
                            raise ValueError(err)                        
                    else:
                        raise ValueError('File {0} not found'.format(input))
                else:
                    raise ValueError('File {0} not found'.format(spec))

            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_encoded', output), self._mh.fromhere())
            ev = event.Event('asn1_after_encode')
            self._mh.fire_event(ev)

            return True

        except (Exception, ValueError) as ex:
            self._mh.demsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False

    def transcode(self, spec, element, input, iformat, oformat, output=None):
        """Method transcodes ASN.1 file to different format

        Args:
            spec (str): specification filename
            element (str): element title
            input (str): input filename
            iformat (str): input format ber|der|oer|aper|uper|xer|gser
            oformat (str): output format ber|der|oer|aper|uper|xer|gser
            output (str): output filename

        Returns:
            bool: result

        Raises:
            event: asn1_before_transcode
            event: asn1_after_transcode

        """

        try:
            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_transcode', input, iformat, oformat, element, spec), self._mh.fromhere())
            ev = event.Event('asn1_before_transcode', spec, element, input, iformat, oformat, output)
            if (self._mh.fire_event(ev) > 0):
                spec = ev.argv(0)
                element = ev.argv(1)
                input = ev.argv(2)
                iformat = ev.argv(3)
                oformat = ev.argv(4)
                output = ev.argv(5)

            if (ev.will_run_default()):
                if (path.exists(spec)):
                    if (path.exists(input)):
                        output = (input.split('/')[-1]).split('.')[0] + '.' + oformat if (output == None) else output
                        cmd = '{0} -I {1} -O {2} {3} {4} {5} {6}'.format(self._path, iformat, oformat, spec, element, input, output)
                        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                        out, err = p.communicate()
                        if (err != None and len(err) > 0):
                            raise ValueError(err)
                    else:
                        raise ValueError('File {0} not found'.format(input))
                else:
                    raise ValueError('File {0} not found'.format(spec))

            self._mh.demsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_transcoded', output), self._mh.fromhere())
            ev = event.Event('asn1_after_transcode')
            self._mh.fire_event(ev)

            return True

        except (Exception, ValueError) as ex:
            self._mh.demsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False
