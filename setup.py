from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_cmsmanagement/__init__.py
from erp_cmsmanagement import __version__ as version

setup(
	name="erp_cmsmanagement",
	version=version,
	description="Erp Cms Management APP",
	author="biswa",
	author_email="biswa4u85@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
