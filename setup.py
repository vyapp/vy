#! /usr/bin/env python2

from distutils.core import setup

setup(name="vy",
      version="1.0.2",
      description="A vim-like in python made from scratch.",
      packages=["vyapp", 
                "vyapp.plugins",
                "vyapp.plugins.syntax",
                "vyapp.plugins.syntax.styles",
                "vyapp.plugins.jdb",
                "vyapp.plugins.pdb"],
      scripts=['vy', 'askpass'],
      package_data={'vyapp': ['vyrc'], 'vyapp.plugins':['tern-config']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/iogf/vy',
      download_url='https://github.com/iogf/vy/releases',
      keywords=['vy', 'vi', 'vim', 'emacs', 'sublime', 'atom', 'nano', 'vim-like'],
      classifiers=[])



































