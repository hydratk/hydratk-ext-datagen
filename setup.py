# -*- coding: utf-8 -*-
from setuptools import setup as st_setup
from setuptools import find_packages as st_find_packages
from sys import argv, version_info
import hydratk.lib.install.task as task
import hydratk.lib.system.config as syscfg

try:
    os_info = syscfg.get_supported_os()
except Exception as exc:
    print(str(exc))
    exit(1)

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
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Utilities"
]

packages = st_find_packages('src')


def version_update(cfg, *args):

    if (not(version_info[0] == 2 and version_info[1] == 7)):
        exclude = [
            'hydratk.extensions.datagen.asn1',
            'hydratk.extensions.datagen.asn1.asn1',
            'hydratk.extensions.datagen.asn1.core',
            'hydratk.extensions.datagen.asn1.utils'
        ]

        for pck in exclude:
            del packages[packages.index(pck)]

config = {
    'pre_tasks': [
        version_update,
        task.install_modules
    ],

    'post_tasks': [
        task.set_config,
        task.set_manpage
    ],

    'modules': [
        {'module': 'hydratk', 'version': '>=0.5.0'},
        {'module': 'hydratk-lib-network', 'version': '>=0.2.0'}
    ],

    'files': {
        'config': {
            'etc/hydratk/conf.d/hydratk-ext-datagen.conf': '{0}/hydratk/conf.d'.format(syscfg.HTK_ETC_DIR)
        },
        'manpage': 'doc/datagen.1'
    }
}

task.run_pre_install(argv, config)

entry_points = {
    'console_scripts': [
        'datagen = hydratk.extensions.datagen.bootstrapper:run_app'
    ]
}

st_setup(
    name='hydratk-ext-datagen',
    version='0.1.2',
    description='Utilities for data generation',
    long_description=readme,
    author='Petr Rašek, HydraTK team',
    author_email='bowman@hydratk.org, team@hydratk.org',
    url='http://extensions.hydratk.org/datagen',
    license='BSD',
    packages=packages,
    package_dir={'': 'src'},
    classifiers=classifiers,
    zip_safe=False,
    entry_points=entry_points,
    keywords='hydratk,data generation,json,xml,asn.1',
    requires_python='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*',
    platforms='Linux'
)

task.run_post_install(argv, config)
