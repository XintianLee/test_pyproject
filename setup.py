from setuptools import setup
import sys

setup(
    name='foo',
    version='0.0.1',
    description='foo foo',
    #long_description=long_description,
    #url='https://github.com/biocatiit/Chiplot-analyze',
    #author='BioCAT',
    #author_email='biocat@lethocerus.biol.iit.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Intended Audience :: Developers',
        # 'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    #keywords='chiplot analyze',
    # project_urls={},
    py_modules=['foo']+(['linux'] if sys.platform == 'linux2' else []),
    #install_requires=['matplotlib'],
)














