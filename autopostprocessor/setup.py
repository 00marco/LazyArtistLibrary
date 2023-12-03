# setup.py

from setuptools import setup, find_packages

setup(
    name='autopostprocessor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your library may have
    ],
    entry_points={
        'console_scripts': [
            # Add any console scripts here if needed
        ],
    },
    author='Marco Pulido',
    author_email='marcopulido00@gmail.com',
    description='image processing base logic for Lazy Artist app',
    url='https://github.com/TODO',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
