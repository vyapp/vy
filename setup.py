#! /usr/bin/env python

from distutils.core import setup

try:
   from distutils.command.build_py import build_py_2to3 \
        as build_py
except ImportError:
   from distutils.command.build_py import build_py

setup(name="vy",
      version="0.1",
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
      author_email="ioliveira@id.uff.br",
      cmdclass = {'build_py': build_py}
)
