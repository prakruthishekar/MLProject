# End to End ML Project

Create environment:
    conda create -p venv python=3.9.13 -y

Activate env
    conda activate venv/


Add setup.py and setup.py will be responsible for ml project as a packag and deploy in python pi pi     


install requirement.txt

    pip install -r requirements.txt

-e . = present in requirement.txt will automatically trigger the setup.py

setup.py: The setup.py file is typically run when you want to install a Python package on your system using the pip package manager or when you want to create a distribution package for your Python project.

When you run the command pip install <package_name> in your terminal, pip looks for the package on the Python Package Index (PyPI) and downloads it to your system. The setup.py file is used to build the package and install any necessary dependencies during the installation process.

You can also use the setup.py file to create a distribution package for your Python project using the python setup.py sdist command. This command will create a source distribution package in a .tar.gz or .zip format that can be uploaded to PyPI or distributed to other users.

In summary, the setup.py file is run during the installation or distribution process of a Python package.



Components - These are modules that we are gonne use in the project