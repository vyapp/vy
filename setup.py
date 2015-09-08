#! /usr/bin/env python

from distutils.core import setup
setup(name="vy",
      version="0.1",
      description="A vim-like in python made from scratch.",
      packages=["vyapp", 
                "vyapp.plugins",
                "vyapp.plugins.syntax",
                "vyapp.plugins.omen",             
                "vyapp.plugins.syntax.themes",
		"vyapp.plugins.jdb",
		"vyapp.plugins.pdb"],
      #package_dir={'vyapp':'vyapp'},
      scripts=['vy'],
      package_data={'vyapp': ['vyrc', '/vyapp/vyrc']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")



















