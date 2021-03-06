from setuptools import setup


setup(
    zip_safe=True,
    name='flow-manager-tools',
    version='1.0',
    author='jcastro',
    author_email='jcastro@brocade.com',
    packages=[
        'docopt',
        'fmtopo'
    ],
    description='Flow Manager tools',
    license='LICENSE',
    install_requires=[
        "pyyaml","requests",'pexpect'
    ],
    entry_points={
        'console_scripts': [
            'fmcheck = fmtopo.shell:main'
        ]
    }

)
