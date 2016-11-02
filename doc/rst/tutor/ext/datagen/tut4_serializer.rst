.. _tutor_datagen_tut4_serializer:

Tutorial 4: Serializer
======================

Module supports class serialization to various formats (string, xml, json).

example
^^^^^^^

**Sample classes** :

  .. code-block:: python
  
     class tst():
    
         _order = ['_a', '_b', '_c', '_d', '_e', '_f', '_g', '_h', '_i']
         _naming = {'_a':'a', '_b':'b', '_c':'c', '_d':'d', '_e':'e', '_f':'f', '_g':'g', '_h':'h', '_i':'i'}
    
         def __init__(self):
        
             self._a = 'a'
             self._b = 'b'
             self._c = 1
             self._d = tst2() 
             self._e = [1, 2, 3]
             self._f = ('a', 'b')   
             self._g = {'a':'1'}    
             self._h = [tst2(), tst2()]
             self._i = {'test1': tst2()}
    
     class tst2():
    
         _order = ['_y', '_x']
         _naming = {'_x':'x', '_y':'y'}
    
         def __init__(self):
        
             self._x = 'x'
             self._y = 2 
             
**string** :

  .. code-block:: python
  
     from hydratk.extensions.datagen.serializer import Serializer
     
     res = Serializer.tostr(tst()) 
     
     tst:
       a:  a
       b:  b
       c:  1
       d:
         tst2:
           y:  2
           x:  x
       e:  
         1
         2
         3
       f:  
         a
         b
       g:  
         a:  1
       h:  
         tst2:
           y:  2
           x:  x
         tst2:
           y:  2
           x:  x
       i:  
         test1:
           tst2:
             y:  2
             x:  x    
             
**xml** :

  .. code-block:: python
  
     from hydratk.extensions.datagen.serializer import Serializer
     
     res = Serializer.toxml(tst(), xml_declaration=True)  
     
     <?xml version='1.0' encoding='UTF-8'?>
     <tst>
       <a>a</a>
       <b>b</b>
       <c>1</c>
       <d>
         <tst2>
           <y>2</y>
           <x>x</x>
         </tst2>
       </d>
       <e>1</e>
       <e>2</e>
       <e>3</e>
       <f>a</f>
       <f>b</f>
       <g>
         <a>1</a>
       </g>
       <h>
         <tst2>
           <y>2</y>
           <x>x</x>
         </tst2>
       </h>
       <h>
         <tst2>
           <y>2</y>
           <x>x</x>
         </tst2>
       </h>
       <i>
         <test1>
           <tst2>
             <y>2</y>
               <x>x</x>
           </tst2>
         </test1>
       </i>
     </tst>           
     
**json** :

  .. code-block:: python
  
     from hydratk.extensions.datagen.serializer import Serializer
     
     res = Serializer.tojson(tst())  
     
     {
       "a": "a",
       "b": "b",
       "c": 1,
       "d": {
         "y": 2,
         "x": "x"
       },
       "e": [
         1,
         2,
         3
       ],
       "f": [
         "a",
         "b"
       ],
       "g": {
         "a": "1"
       },
       "h": [
         {
           "y": 2,
           "x": "x"
         },
         {
           "y": 2,
           "x": "x"
         }
       ],
       "i": {
         "test1": {
           "y": 2,
           "x": "x"
         }
       }
     }                       