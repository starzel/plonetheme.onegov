from setuptools import setup, find_packages
import os

version = '3.3.1.dev0'

tests_require = [
    'plone.app.testing',
    'plone.resource',
    'pyquery',
    'plone.app.contenttypes',
    ]

setup(name='plonetheme.onegov',
      version=version,
      description="Theme package for OneGov",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Julian Infanger',
      author_email='julian.infanger@4teamwork.ch',
      url='http://www.4teamwork.ch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'plone.app.theming',
        'Products.CMFCore',
        'setuptools',
        'plone.batching',
        'PyScss',
        'plone.api',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
