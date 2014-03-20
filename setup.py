from setuptools import setup, find_packages

VERSION = "1.0"
setup(
    name = "Navi-Notify",
    description= 'Get some ones attention!',
    author="Ryan Hunter", author_email="rhunter@etiometry.com",
    version = VERSION,
    packages = find_packages(),
    data_files=[('/etc/init.d/',['daemon/navi-notifyd'])],
    install_requires=['distribute','pygame'],
    scripts = ['bin/navi-notify','bin/notify']
)
