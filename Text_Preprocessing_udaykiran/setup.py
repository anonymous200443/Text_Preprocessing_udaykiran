# setup.py
import setuptools

with open('Read.md','r') as file:
	long_description=file.read()




setuptools.setup(
	name='Text_Preprocessing_udaykiran',
	version='0.0.1',
	author='Uday kiran',
	author_email='Udaykiran7615124@gmail.com',
	description='This is text_processing package',
	long_description=long_description,
	long_description_content_type=text/markdown,
	packages=setuptools.find_packages(),
	classifiers=[
	'programming Language:: Python:: 3',
	'License:: OSI Aproved :: MIT License',
	'Operating System::OS Independent'],
	python_requires='>=3.5'



	)
