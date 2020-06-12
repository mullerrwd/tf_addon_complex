import io
import os
import re
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="tf_addon_complex",
    version="0.0.1",
    url="https://github.com/mullerrwd/tf_addon_complex",
    license='MIT',

    author="Robert Muller",
    author_email="mullerrwd@gmail.com",

    description="A tf addon that aims to provide the necessary components for implementing complex-valued deep neural networks.",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=Path('requirements.txt').read_text().splitlines(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
