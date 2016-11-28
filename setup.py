# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sys import argv, version_info
from os import path
from subprocess import call

with open("README.rst", "r") as f:
    readme = f.read()
    
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "License :: Freely Distributable",
    "Operating System :: OS Independent",   
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",    
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Utilities"
] 

requires = [
            'hydratk',
            'hydratk-lib-network'
           ]
           
files = {
         'etc/hydratk/conf.d/hydratk-ext-datagen.conf' : '/etc/hydratk/conf.d'
        }  

packages = find_packages('src')   
if (not(version_info[0] == 2 and version_info[1] == 7)):
    exclude = [
               'hydratk.extensions.datagen.asn1',
               'hydratk.extensions.datagen.asn1.asn1',
               'hydratk.extensions.datagen.asn1.core',
               'hydratk.extensions.datagen.asn1.utils'
              ]
     
    for pck in exclude:
        del packages[packages.index(pck)] 

entry_points = {
                'console_scripts': [
                    'datagen = hydratk.extensions.datagen.bootstrapper:run_app'                               
                ]
               }          
                
setup(
      name='hydratk-ext-datagen',
      version='0.1.2a.dev1',
      description='Utilities for data generation',
      long_description=readme,
      author='Petr Rašek, HydraTK team',
      author_email='bowman@hydratk.org, team@hydratk.org',
      url='http://extensions.hydratk.org/datagen',
      license='BSD',
      packages=packages,
      install_requires=requires,
      package_dir={'' : 'src'},
      classifiers=classifiers,
      zip_safe=False,  
      entry_points=entry_points,
      keywords='hydratk,data generation,json,xml,asn.1',
      requires_python='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*',
      platforms='Linux' 
     )

if ('install' in argv or 'bdist_egg' in argv or 'bdist_wheel' in argv):
    
    for file, dir in files.items():    
        if (not path.exists(dir)):
            call('mkdir -p {0}'.format(dir), shell=True)
            
        call('cp {0} {1}'.format(file, dir), shell=True) 
        
    call('chmod -R a+r /etc/hydratk', shell=True)
    call('gzip -c doc/datagen.1 > /usr/share/man/man1/datagen.1', shell=True)