from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ProTaska-GPT',
    version='0.0.8',
    description='Unleash the Potential of Datasets with Intelligent Tasks, Tutorials, and Algorithm Recommendations.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Aman Priyanshu, Supriti Vijay',
    author_email='amanpriyanshusms2001@gmail.com',
    packages=find_packages(exclude=["notebooks", "docs"]),
    url='https://github.com/AmanPriyanshu/protaska-gpt',
    install_requires=[
        'langchain',
        'numpy',
        'pandas',
        'colorama',
        'wikipedia',
        'openai',
        'datasets',
        'tiktoken'
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
