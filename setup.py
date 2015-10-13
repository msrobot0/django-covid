import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-orb',
    version='2.0.0',
    packages=['orb',
              'orb.analytics',
              'orb.api',
              'orb.migrations', 
              'orb.fixtures',
              'orb.utils',
              'orb.profile',],
    include_package_data=True,
    license='GNU GPL v3 License',  # example license
    description='',
    long_description=README,
    url='http://oppia-mobile.org/',
    author='Alex Little, Digital Campus',
    author_email='alex@digital-campus.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django >= 1.7",
	    "django-tastypie >= 0.11.0",
        "django-tablib >= 0.9.11",
        "django-crispy-forms >= 1.4.0",
        "django-tinymce",
        "django-wysiwyg",
        "django-haystack",
        "pysolr",
        "pillow",
        "sorl-thumbnail",
        "textract >= 1.2.0",
        "pytz",
    ],
)
