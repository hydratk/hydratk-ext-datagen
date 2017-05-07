# -*- coding: utf-8 -*-
"""Module for class serialization

.. module:: datagen.serializer
   :platform: Unix
   :synopsis: Module for class serialization
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

from collections import Sequence
from lxml.etree import fromstring, tostring
from simplejson import dumps
from sys import version_info

try:
    from collections import OrderedDict
except ImportError:
    pass


class Serializer(object):
    """Class Serializer
    """

    @staticmethod
    def tostr(obj):
        """Method serializes class instance to string

        By default the serializer gets all instance attributes (set in constructor) and writes them in default order.
        Class can have special class attributes (not set in constructor)
        _order - list of instance attributes names, it defines serialization order, missing attributes are omitted (not serialized)
        _naming - dictionary (key - attribute name, value - new name used in serialization) 

        Args:
            obj (obj): class instance

        Returns:
            str

        """

        s = Serializer._tostr(obj)

        return s

    @staticmethod
    def toxml(obj, xml_declaration=False):
        """Method serializes class instance to xml string

        Args:
            obj (obj): class instance
            xml_declaration (bool): include XML declaration

        Returns:
            str

        """

        s = Serializer._toxml(obj)
        s = tostring(fromstring(s), xml_declaration=xml_declaration,
                     encoding='UTF-8', pretty_print=True)

        return s if (version_info[0] == 2) else s.decode()

    @staticmethod
    def tojson(obj):
        """Method serializes class instance to json string

        Method is not supported for Python 2.6

        Args:
            obj (obj): class instance

        Returns:
            str

        Raises:
           error: NotImplementedError

        """

        if (version_info[0] == 2 and version_info[1] == 6):
            raise NotImplementedError(
                'Method tojson is not supported for Python 2.6')

        s = Serializer._tojson(obj)
        s = dumps(s, indent=2)

        return s

    @staticmethod
    def _get_attrs(obj):
        """Method returns class instance attributes

        Args:
            obj (obj): class instance

        Returns:
            dict

        """

        return obj.__dict__

    @staticmethod
    def _has_attrs(obj):
        """Method checks if object has instance attributes

        Args:
            obj (obj): class instance

        Returns:
            bool

        """

        return (hasattr(obj, '__dict__') and len(obj.__dict__.keys()) > 0)

    @staticmethod
    def _tostr(obj, level=1):
        """Method serializes given object to string

        It is used in recursive traversal
        Processing per object type (class instance, list, dictionary, simple type) 

        Args:
            obj (obj): object of any type (not just class instance)
            level (int): indentation level

        Returns:
            str

        """

        s = ''
        if (Serializer._has_attrs(obj)):
            s += obj.__class__.__name__ + ':'
            attrs = Serializer._get_attrs(obj)
            order = obj._order if (hasattr(obj, '_order')) else attrs.keys()
            naming = obj._naming if (hasattr(obj, '_naming')) else {}
            for key in order:
                if (key in attrs):
                    title = naming[key] if (key in naming) else key
                    if (not Serializer._has_attrs(attrs[key])):
                        s += '\n{0}{1}:  {2}'.format(
                            '  ' * level, title, Serializer._tostr(attrs[key], level=level + 1))
                    else:
                        s += '\n{0}{1}:\n{2}{3}'.format('  ' * level, title, '  ' * (
                            level + 1), Serializer._tostr(attrs[key], level=level + 2))
        elif (isinstance(obj, Sequence) and not isinstance(obj, str)):
            for value in obj:
                s += '\n{0}{1}'.format('  ' * level,
                                       Serializer._tostr(value, level=level + 1))
        elif (isinstance(obj, dict)):
            for key, value in obj.items():
                if (not Serializer._has_attrs(value)):
                    s += '\n{0}{1}:  {2}'.format('  ' * level, key,
                                                 Serializer._tostr(value, level=level + 1))
                else:
                    s += '\n{0}{1}:\n{2}{3}'.format(
                        '  ' * level, key, '  ' * (level + 1), Serializer._tostr(value, level=level + 2))
        else:
            s += str(obj)

        return s

    @staticmethod
    def _toxml(obj, title=None):
        """Method serializes given object to xml string

        It is used in recursive traversal
        Processing per object type (class instance, list, dictionary, simple type) 

        Args:
            obj (obj): object of any type (not just class instance)
            title (str): item title for list elements (multiple cardinality)

        Returns:
            str

        """

        s = ''
        if (Serializer._has_attrs(obj)):
            s += '<' + obj.__class__.__name__ + '>'
            attrs = Serializer._get_attrs(obj)
            order = obj._order if (hasattr(obj, '_order')) else attrs.keys()
            naming = obj._naming if (hasattr(obj, '_naming')) else {}
            for key in order:
                if (key in attrs):
                    value = attrs[key]
                    title = naming[key] if (key in naming) else key
                    if (isinstance(value, Sequence) and not isinstance(value, str)):
                        s += Serializer._toxml(value, title)
                    else:
                        s += '<{0}>{1}</{2}>'.format(title,
                                                     Serializer._toxml(value), title)
            s += '</' + obj.__class__.__name__ + '>'
        elif (isinstance(obj, Sequence) and not isinstance(obj, str)):
            title = title if (title != None) else 'item'
            for value in obj:
                s += '<{0}>{1}</{2}>'.format(title,
                                             Serializer._toxml(value), title)
        elif (isinstance(obj, dict)):
            for key, value in obj.items():
                s += '<{0}>{1}</{2}>'.format(key,
                                             Serializer._toxml(value), key)
        else:
            s += str(obj)

        return s

    @staticmethod
    def _tojson(obj):
        """Method serializes given object to ordered dictionary

        It is used in recursive traversal
        Processing per object type (class instance, list, dictionary, simple type) 

        Args:
            obj (obj): object of any type (not just class instance)

        Returns:
            dict

        """

        s = None
        if (Serializer._has_attrs(obj)):
            s = OrderedDict()
            attrs = Serializer._get_attrs(obj)
            order = obj._order if (hasattr(obj, '_order')) else attrs.keys()
            naming = obj._naming if (hasattr(obj, '_naming')) else {}
            for key in order:
                if (key in attrs):
                    value = attrs[key]
                    title = naming[key] if (key in naming) else key
                    s[title] = Serializer._tojson(value)
        elif (isinstance(obj, Sequence) and not isinstance(obj, str)):
            s = []
            for value in obj:
                s.append(Serializer._tojson(value))
        elif (isinstance(obj, dict)):
            s = OrderedDict()
            for key, value in obj.items():
                s[key] = Serializer._tojson(value)
        else:
            s = obj

        return s
