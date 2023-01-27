import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='jalapeno',
    author='Jesse Wiles',
    author_email='jesse.wiles@gmail.com',
    description='Jalapeno PyPI (Python Package Index) Package',
    keywords='jalapeno, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jessewiles/jalapeno',
    project_urls={
        'Documentation': 'https://github.com/jessewiles/jalapeno',
        'Bug Reports':
        'https://github.com/tomchen/jalapeno/issues',
        'Source Code': 'https://github.com/tomchen/jalapeno',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=jalapeno:main',
    # You can execute `run` in bash to run `main()` in src/jalapeno/__init__.py
    #     ],
    # },
)
