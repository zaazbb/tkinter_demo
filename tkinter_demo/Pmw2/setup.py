#!/usr/bin/env python
# setup.py
from distutils.core import setup


setup(name="Pmw",
      version='2.0.0',
      description = 'Python Mega Widgets',
      author="Telstra Corporation Limited, Australia",
      author_email="",
      url='http://pmw.sourceforge.net/',

      package_dir = { "Pmw":"Pmw"},

      packages=['Pmw', 'Pmw.Pmw_2_0_0',
                'Pmw.Pmw_2_0_0.lib',],

      package_data={'Pmw': ['Pmw_2_0_0/lib/Pmw.def',
                            'Pmw_2_0_0/doc/*',
                            'Pmw_2_0_0/contrib/*',
                            'Pmw_2_0_0/demos/*',
                            'Pmw_2_0_0/tests/*',
                            'Pmw_2_0_0/bin/*',
                           ]
                   },

      license='BSD',
      long_description='''Pmw is a toolkit for building high-level compound widgets, or megawidgets,
        constructed using other widgets as component parts. It promotes consistent look and feel within
         and between graphical applications, is highly configurable to your needs and is easy to use.''',
      classifiers = [
          'Development Status :: alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: BSD',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: GUI',
          ],
     )
