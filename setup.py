import setuptools

with open("README.md") as fh:
	long_description = fh.read()

setuptools.setup(
	name="python-ex-san3107",
	version="1.0.0",
	author="sanjeev1992jha",
	author_email="sanjeev1992jha@gmail.com",
	description="A sample python package example",
	long_description=long_description,
	long_description_content_type="",
	url="https://github.com/Sanjeev139/test1",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming language :: Pyhton :: 3.5",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.5',
	)