#! /usr/bin/env python2

from setuptools import setup


install_requires = []
for line in open('requirements.txt', 'r'):
    install_requires.append(line.strip())


setup(name="vy",
      version="2.2.0",
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
      classifiers=[],
      install_requires=install_requires)
