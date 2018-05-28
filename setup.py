import os
from setuptools import setup

install_requires = [
    'django'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django_singleton_model',
    version='0.2.3',
    description='Simple package for impleting models using singleton design pattern',
    url='https://github.com/icaropires/django-singleton-model',
    author='Ícaro Pires',
    author_email='icaropsa@gmail.com',
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    packages=['singleton_model'],
    install_requires=install_requires,
    long_description=read('README.rst'),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
