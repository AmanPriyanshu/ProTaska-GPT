from setuptools import setup

setup(
    name='ProTaska-GPT',
    version='0.0.1',
    description='Unleash the Potential of Datasets with Intelligent Tasks, Tutorials, and Algorithm Recommendations.',
    long_description='ProTaska-GPT is an open-source Python library that empowers data scientists and researchers to unleash the potential of datasets with intelligent tasks, tutorials, and algorithm recommendations. It seamlessly integrates with popular dataset sources like Kaggle and Hugging Face, allowing users to easily import and work with diverse datasets. With ProTaska-GPT, you can visualize and explore datasets, gain insights into data distributions, correlations, and missing values, and generate customized tasks and algorithm suggestions based on your dataset characteristics. Whether you are a beginner or an experienced practitioner, ProTaska-GPT provides a collection of beginner-friendly tutorials that guide you through common data science workflows, fostering practical learning and skill development.',
    author='Aman Priyanshu, Supriti Vijay',
    author_email='amanpriyanshusms2001@gmail.com',
    packages=['protaska'],
    url='https://github.com/AmanPriyanshu/protaska-gpt',
    install_requires=[
        'langchain',
        'numpy',
        'pandas',
        'colorama',
        'gradio',
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
