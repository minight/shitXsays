from setuptools import setup

setup(
    name='sjs',
    version='1.0',
    long_description=__doc__,
    packages=['lmao'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask_sqlalchemy']
)

