from setuptools import setup, find_packages

with open("README.md", "r") as f:
        long_description=f.read()

version = '0.0.2'

setup(
  name='esx',
  version=version,
  author="@byteface",
  author_email="byteface@gmail.com",
  license="MIT",
  url='https://github.com/byteface/esx',
  download_url='https://github.com/byteface/esx/archive/' + version + ' .tar.gz',
  description='A port of Javascript API to python. Useful for interoperability, porting js code and more...',
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords=['Javascript', 'JavaScript', 'js', 'html', 'json', 'web', 'javascript', 'es6', 'es7', 'es8', 'es9'],
  python_requires='>=3.6',
  classifiers=[
      "Programming Language :: Python :: 3",
      "Programming Language :: JavaScript",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Intended Audience :: Developers",
      "Intended Audience :: Other Audience",
      "License :: OSI Approved :: MIT License",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Topic :: Internet",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Multimedia :: Graphics :: Presentation",
      "Topic :: Software Development",
      "Topic :: Software Development :: Code Generators",
      "Topic :: Terminals",
      "Topic :: Utilities",
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Text Processing :: Markup :: HTML',
  ],
  install_requires=[
          'requests', 'python-dateutil', 'urllib3'
  ],
  packages=find_packages(),
  include_package_data=True,
)
