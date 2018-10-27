from setuptools import setup, find_packages


requires = ["numpy>=1.15.3"]


setup(
    name='reversi_board',
    version='0.1.1',
    description='reversi board',
    url='https://github.com/naari3/reversi_board-py',
    author='naari3',
    author_email='naari.named@gmail.com',
    license='MIT',
    keywords='reversi othero',
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
