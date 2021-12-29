#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="preki_funcmodels",
    version="1.0.0",
    author="Preki",
    author_email="david@gopreki.com",
    packages=['preki_funcmodels'],
    url='https://gopreki.com',
    download_url="https://github.com/GoPreki/FunctionUtilsModels",
    license="MIT",
    description="Python library for Preki Functions usage with Neomodel Models",
    long_description="Python library for Preki Functions usage with Neomodel Models",
    install_requires=[
        "neomodel @ git+git://github.com/neo4j-contrib/neomodel@4.0.8",
        "preki_funcutils @ git+git://github.com/GoPreki/FunctionUtilsHandler@ffcfcde54a251117350afc527586978fb29483c0"
    ],
)
