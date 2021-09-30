import setuptools
from subprocess import check_call
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import os
import shutil

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()


cmds_to_run = [
	"apt-get update",
    "apt-get update && apt-get install libnspr4 libnss3 libnss3-tools libfontconfig1 libglib2.0"
]

# "cd /home/app/",
#     "git clone https://github.com/facebookresearch/mmf.git mmf && cd mmf",
#     "sed -i '/torch/d' requirements.txt && pip install -e .",
#     "cd /home/app && git clone https://github.com/rohanricky0609/vqa-maskrcnn-benchmark.git && cd vqa-maskrcnn-benchmark",
#     "python setup.py build && python setup.py develop",

class PostInstallCommand(install):
	def run(self):
		install.run(self)
		for cmd in cmds_to_run:
			check_call(cmd,shell=True)


class CustomDevelopCommand(develop):
	def run(self):
	   develop.run(self)
	   for cmd in cmds_to_run:
		   check_call(cmd,shell=True)

class CustomEggInfoCommand(egg_info):
	def run(self):
		egg_info.run(self)
		for cmd in cmds_to_run:
			check_call(cmd,shell=True)

setuptools.setup(
	name="startup_playstorereviews",
	version="0.0.1",
	author="Example Author",
	author_email="author@example.com",
	description="A small example package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	# url="https://github.com/pypa/sampleproject",
	# project_urls={
	#     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
	# },
	# classifiers=[
	#     "Programming Language :: Python :: 3",
	#     "License :: OSI Approved :: MIT License",
	#     "Operating System :: OS Independent",
	# ],
	# package_dir={"": "src"},
	# packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
	cmdclass= {
		'install' : PostInstallCommand,
	}
)