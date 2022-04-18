from setuptools import setup, find_packages

setup(
    name="rst",
    version='1.0.1',
    description="Reverse Shell Tool",
    author="MustansirG",
    author_email='me@mustansirg.in',
    packages=['rst'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rst = rst.rst:main',
        ],
    },
    install_requires=[
          "gnureadline==8.0.0",
          "keyboard==0.13.5",
          "rich==12.2.0",
          "setuptools==44.1.1",
          "simple_term_menu==1.4.1",
          "pyngrok"
    ],
)