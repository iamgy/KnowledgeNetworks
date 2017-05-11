from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Topic :: Scientific/Engineering",
    ]

LONG_DESCRIPTION = """
KnowledgeNetworks
====================
KnowledgeNetworks is a software that reads in metadata of published papers in
Nuclear Science and Technology from 2000 to 2016 and creates a Knowledge Network
based on the location of the authors' countries.
To get started, please go to the repository README.
.. _README: https://github.com/ksakloth/KnowledgeNetworks/blob/master/README.md
License
=======
``KnowledgeNetworks`` is licensed under the terms of the MIT license. See the
file "LICENSE" for information on the history of this software, terms &
conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""
NAME = 'knetwork'
MAINTAINER = "Rahul Avadhoot"
MAINTAINER_EMAIL = "rahulavd@uw.edu"
AUTHOR = "Rahul Avadhoot"
AUTHOR_EMAIL = "rahulavd@uw.edu"
DESCRIPTION = "KnowledgeNetworks",
LICENSE = "MIT",
URL = "https://github.com/ksakloth/KnowledgeNetworks.git",
DOWNLOAD_URL = "https://github.com/ksakloth/KnowledgeNetworks.git"
PLATFORMS = "OS Independent"
REQUIRES = ["numpy", "pandas", "sklearn"]

setup(name=NAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      classifiers=CLASSIFIERS,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      platforms=PLATFORMS,
      version=1.0,
      packages=find_packages(),
      install_requires=REQUIRES,
      requires=REQUIRES,
      include_package_data=TRUE
)
