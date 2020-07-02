#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="preki_funcmodels",
    version="3.0.1",
    author="Preki",
    author_email="david@gopreki.com",
    packages=['preki_funcmodels'],
    url='https://gopreki.com',
    download_url="https://github.com/GoPreki/FunctionUtilsHandler",
    license="MIT",
    description="Python library for Preki Functions usage with Neomodel Models",
    long_description="Python library for Preki Functions usage with Neomodel Models",
    install_requires=["neomodel >= 3.3.2"],
)
