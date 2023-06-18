from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ProTaska-GPT',
    version='0.1.0',
    description='Your AI-powered data companion for intelligent tasks, tutorials, and algorithm recommendations.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Aman Priyanshu, Supriti Vijay',
    author_email='amanpriyanshusms2001@gmail.com',
    packages=find_packages(exclude=["notebooks", "docs"]),
    url='https://github.com/AmanPriyanshu/protaska-gpt',
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='data-companion AI machine-learning data-science tutorials tasks',
    project_urls={
        'Documentation': 'https://github.com/AmanPriyanshu/protaska-gpt',
        'Source': 'https://github.com/AmanPriyanshu/protaska-gpt',
        'Bug Tracker': 'https://github.com/AmanPriyanshu/protaska-gpt/issues',
    },
    license='MIT',
)
