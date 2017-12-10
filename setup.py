from setuptools import setup

setup(
    name='nextbus_client',
    version='0.0.3',
    author="Adam Duston",
    author_email="adamduston@gmail.com",
    url="https://github.com/compybara/nextbus_client",
    license="BSD-3-Clause",
    packages=['nextbus_client'],
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ]
)