from setuptools import setup

setup(
    name='ProTaska-GPT',
    version='0.0.0',
    description='Unleash the Potential of Datasets with Intelligent Tasks, Tutorials, and Algorithm Recommendations.',
    author='Aman Priyanshu, Supriti Vijay',
    author_email='amanpriyanshusms2001@gmail.com',
    packages=['protaska'],
    url='https://github.com/AmanPriyanshu/protaska-gpt',
    install_requires=[
        'langchain',
        'numpy',
        'pandas',
        'colorama',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
