from setuptools import setup, find_packages

setup(
    name='wrdscli',
    version='0.0.1',
    description='Cli for accessing WRDS',
    author='Xiaowen Zhang',
    author_email='seanxwzhang@gmail.com',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy>=1.3', 
        'click>=7.0',
        'psycopg2>=2.7.6',
        ],
    python_requires='>=3.7.4',
    entry_points='''
        [console_scripts]
        wrdscli=wrdscli.wrdscli:wrdscli
    ''',
)