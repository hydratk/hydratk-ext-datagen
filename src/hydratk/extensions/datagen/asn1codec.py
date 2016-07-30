# -*- coding: utf-8 -*-
"""Module for ASN.1 codec

.. module:: datagen.asn1codec
   :platform: Unix
   :synopsis: Module for ASN.1 codec
              Libraries for ASN.1 were taken from https://github.com/mitshell/libmich
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

"""
Events:
-------
asn1_before_import_spec
asn1_after_import_spec
asn1_before_encode
asn1_after_encode
asn1_before_decode
asn1_after_decode

"""

from hydratk.core.masterhead import MasterHead
from hydratk.core import event
from os import path
from simplejson import loads, dumps
from binascii import hexlify
from sys import version_info

if (version_info[0] == 2 and version_info[1] == 7):
    from asn1.asn1.processor import process_modules
    from asn1.asn1.ASN1 import ASN1Obj
    from asn1.asn1.BER import BER
    from collections import OrderedDict

class ASN1Codec(object):
    """Class ASN1Codec
    """
    
    _mh = None
    _path = None
    _spec = None
    _elements = None
    
    def __init__(self):
        """Class constructor
        
        Called when object is initialized
        
        Args:   
           none         
                
        """  
        
        if (not (version_info[0] == 2 and version_info[1] == 7)):
            raise NotImplementedError('ASN.1 codec is not supported for Python 3.x due to external library libmich')               
        
        self._mh = MasterHead.get_head()
    
    @property
    def path(self):
        """ path property getter """
        
        return self._path    
    
    @property
    def spec(self):
        """ spec property getter """
        
        return self._spec
    
    @property
    def elements(self):
        """ elements property getter """
        
        return self._elements
    
    def __str__(self):
        """Method overrides __str__
        
        Args:  
           none          
           
        Returns:
           str
                
        """         
        
        return self._spec._text_def 
    
    def import_spec(self, filename):
        """Method imports specification
        
        Args:
            filename (str): filename
            
        Returns:
            bool: result
        
        Raises:
            event: asn1_before_import_spec
            event: asn1_after_import_spec   
                
        """     
    
        try:
    
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_import_spec', filename), self._mh.fromhere()) 
            ev = event.Event('asn1_before_import_spec', filename)
            if (self._mh.fire_event(ev) > 0):
                filename = ev.argv(0)
                
            if (ev.will_run_default()):        
                if (path.exists(filename)):
                    with open(filename, 'r') as f:                                         
                        self._spec = process_modules(f.read())  
                        self._elements = self._spec[0]['TYPE']._dict
                        ASN1Obj._SAFE = True
                        ASN1Obj._RET_STRUCT = True
                        ASN1Obj.CODEC = BER    
                        self._path = path.abspath(filename)                                            
                else:
                    raise ValueError('File {0} not found'.format(filename))      
                
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_spec_imported'), self._mh.fromhere())   
            ev = event.Event('asn1_after_import_spec')
            self._mh.fire_event(ev)
                    
            return True                             
               
        except (Exception, ValueError) as ex:
            self._mh.dmsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())
            return False
        
    def encode(self, infile, element, outfile=None):
        """Method encodes json file to binary 
        
        Args:
            infile (str): input filename
            element (str): element name
            outfile (str): output filename, default infile with suffix bin
            
        Returns: 
            bool: result
        
        Raises: 
            event: asn1_before_encode
            event: asn1_after_encode  
                
        """         
        
        try:
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_encode', infile), self._mh.fromhere()) 
            
            if (self._spec == None):
                raise ValueError('Specification is not imported yet')             
            
            ev = event.Event('asn1_before_encode', infile, element, outfile)
            if (self._mh.fire_event(ev) > 0):
                infile = ev.argv(0)
                element = ev.argv(1)
                outfile = ev.argv(2)        
        
            if (ev.will_run_default()):
                if (element not in self._elements):
                    raise ValueError('Invalid element {0}'.format(element)) 
                
                if (path.exists(infile)):         
                    with open(infile, 'r') as f: 
                        objects = loads(f.read())
                        if (objects.__class__.__name__ == 'list'):
                            input = []
                            for record in objects:
                                input.append(self._update_datatypes(record))
                        else:                                     
                            input = [self._update_datatypes(objects)]            
                    outfile = path.abspath(infile).split('.')[0]+'.bin' if (outfile == None) else outfile               
                    with open(outfile, 'wb') as f:
                        for record in input:                      
                            output = self._elements[element].encode(record)
                            f.write(str(output()))                                                         
                else:
                    raise ValueError('File {0} not found'.format(infile))
                
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_encoded', outfile), self._mh.fromhere())   
            ev = event.Event('asn1_after_encode')
            self._mh.fire_event(ev)
                    
            return True                 
             
        except (Exception, ValueError) as ex:
            self._mh.dmsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())   
            return False     
        
    def decode(self, infile, element, outfile=None):
        """Method decodes binary file to json
        
        Args:
            infile (str): input filename
            element (str): element name
            outfile (str): output filename, default infile with suffix json
            
        Returns:
            bool: result
        
        Raises:
            event: asn1_before_decode
            event: asn1_after_decode     
                
        """         
        
        try:
        
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_decode', infile), self._mh.fromhere()) 
            
            if (self._spec == None):
                raise ValueError('Specification is not imported yet')             
            
            ev = event.Event('asn1_before_decode', infile, element, outfile)
            if (self._mh.fire_event(ev) > 0):
                infile = ev.argv(0)
                element = ev.argv(1)
                outfile = ev.argv(2)           
        
            if (ev.will_run_default()): 
                if (element not in self._elements):
                    raise ValueError('Invalid element {0}'.format(element))                
                
                if (path.exists(infile)):         
                    with open(infile, 'rb') as f:                                         
                        input = f.read()
                
                    outfile = path.abspath(infile).split('.')[0]+'.json' if (outfile == None) else outfile     
                    with open(outfile, 'w') as f:                      
                        records = self._split_records(input)

                        if (len(records) > 1):
                            output = []
                            for record in records:                                
                                self._elements[element].decode(record)
                                output.append(self._create_dict(self._elements[element]))
                        else:                                    
                            self._elements[element].decode(records[0])
                            output = self._create_dict(self._elements[element])
                        f.write(dumps(output, indent=4))                                                      
                else:
                    raise ValueError('File {0} not found'.format(infile)) 
            
            self._mh.dmsg('htk_on_debug_info', self._mh._trn.msg('datagen_asn1_decoded', outfile), self._mh.fromhere())   
            ev = event.Event('asn1_after_decode')
            self._mh.fire_event(ev)
                    
            return True              

        except (Exception, ValueError) as ex:
            self._mh.dmsg('htk_on_error', 'error: {0}'.format(ex), self._mh.fromhere())  
            return False             
        
    def _update_datatypes(self, obj):
        """Method updates datatypes
        
        It is used in encoder, some datatypes can't be encoded
        The object is traversed recursively
        
        Args:
            obj (json): particular json object  
            
        Returns:
            json: json object
                
        """           
        
        classname = obj.__class__.__name__
        if (classname == 'dict'):
            for key, value in obj.items():
                obj[key] = self._update_datatypes(obj[key])
        elif (classname == 'list'):
            items = []
            for item in obj:
                items.append(self._update_datatypes(item))    
            obj = items           
        elif (classname == 'long'):
            obj = int(obj) 
        elif (classname == 'unicode'):
            obj = str(obj)
           
        return obj  
    
    def _split_records(self, input):
        """Method splits records from input file
        
        Args:
            input (str): file contents
            
        Returns:
            list: list of records
                
        """           
        
        records = []
        input = bytearray(input)
        i = 0
        idx = None
        length = len(input)
        while (i < length):
            len_byte = input[i+1]
            if (len_byte < 128):
                idx = i+len_byte+2
            elif (len_byte == 128):
                idx = length
            else:
                size_bytes = len_byte-128
                rec_size = int(hexlify(input[i+2 : i+2+size_bytes]), 16)
                idx = i+2+size_bytes+rec_size
                
            records.append(str(input[i:idx]))
            i = idx
         
        return records
    
    def _create_dict(self, obj, val=None, output=None):
        """Method creates dictionary according to spec
        
        It is used in decoder, objects are ordered as specified
        The object is traversed recursively
        
        Args:
            obj (obj): particular ASN1 object
            val (obj): element value
            output (dict): particular output
            
        Returns:
            dict: ordered dictionary object 
                
        """          
        
        if (val == None):
            val = obj._val 
        if (output == None):
            output = OrderedDict()   
            
        if (obj._type in ('SEQUENCE', 'SET')):
            for key in obj._cont._index:
                if (key in val):           
                    output[key] = OrderedDict()
                    output[key] = self._create_dict(obj._cont._dict[key], val[key], output[key])
        elif (obj._type == 'SEQUENCE OF'):
            output = []
            for item in val:
                output.append(self._create_dict(obj._cont, item, None))                
        elif (obj._type == 'CHOICE'):
            key = val[0]
            output[key] = OrderedDict()
            output[key] = self._create_dict(obj._cont._dict[key], val[1], output[key])
        else:
            if (val.__class__.__name__ == 'str' and '\\x' in val.__repr__()):
                val = val.encode('hex')                
            output = val
            
        return output  