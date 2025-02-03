import setuptools

setuptools.setup(
    name="metalpriceapi",
    version="1.1.1",
    url="https://github.com/metalpriceapi/metalpriceapi-python",

    license_files=('LICENSE'),

    author="MetalpriceAPI",
    author_email="contact@metalpriceapi.com",

    description="Official Python wrapper for metalpriceapi.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.31.0'],
    keywords=['currency', 'metal price', 'exchangerate', 'rates'],
)
