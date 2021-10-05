from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='fake_news',
    version='0.1',
    description='Detection of fake news articles',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],

    url='https://github.com/meleyka/Springboard/fake_news_detector',
    author='Meley Kifleyesus',
    author_email='meleysk.dev@gmail.com',
    license='MIT',
    packages=['fake_news'],
    install_requires=[
        'pypandoc>=1.6',
        'flask'
    ],
)
