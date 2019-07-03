import codecs
import os
import re

from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

version = '0.0.0'
changes = os.path.join(here, 'CHANGES.rst')
match = r'^#*\s*(?P<version>[0-9]+\.[0-9]+(\.[0-9]+)?)$'
with codecs.open(changes, encoding='utf-8') as changes:
    for line in changes:
        res = re.match(match, line)
        if res:
            version = res.group('version')
            break

# Get the long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get version
with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changelog = f.read()


install_requirements = []
tests_requirements = []


class VersionCommand(Command):
    description = 'print library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


if __name__ == '__main__':
    setup(
        name='django-simple-form',
        description='Django-simple-form is a simple way to build your forms in HTML-level',
        version=version,
        long_description=long_description,
        long_description_content_type='text/x-rst',
        author='Daniel Bastos',
        author_email='danielfloresbastos@gmail.com',
        url='https://github.com/daniellbastos/django-simple-form/',
        install_requires=install_requirements,
        tests_require=tests_requirements,
        keywords=['django', 'widget', 'form', 'field'],
        packages=['simple_form', 'simple_form.templatetags'],
        include_package_data=True,
        zip_safe=False,
        classifiers=[
            'Framework :: Django',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development :: Libraries',
        ],
        cmdclass={'version': VersionCommand},
    )
