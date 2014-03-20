from setuptools import setup, find_packages

VERSION = "1.0"
setup(
    name = "Navi-Notify",
    description= 'Get some ones attention!',
    author="Ryan Hunter", author_email="rhunter@etiometry.com",
    version = VERSION,
    packages = find_packages(),
    data_files=[('/opt/navi/' , ['sound/hey.wav', 'sound/listen.wav', 'sound/hello.wav', 'sound/look.wav'])],
    install_requires=['distribute','pygame'],
    scripts = ['bin/navi-notify','bin/notify']
)
