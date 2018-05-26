from setuptools import setup

install_requires = [
    'django'
]

setup(
    name='django_singleton_model',
    version='0.1',
    description='Simple package for impleting models using singleton design pattern',
    url='https://github.com/icaropires/django-singletonmodel',
    author='Ícaro Pires',
    author_email='icaropsa@gmail.com',
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    packages=['singleton_model'],
    install_requires=install_requires,
)
