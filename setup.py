from setuptools import setup, find_packages

setup(
    name = 'mlproject',
    version = '0.0.1',
    description = 'first end to end machine learning project',
    author = 'shobhit',
    author_email = 'shobhitgpt28@gmail.com',
    package_dir = {"": "src"},
    packages = find_packages(where = "src")
)

# -e . in requirements.txt will figure out this setup.py file and will create and install local packages along with requirements.txt
# package_dir : it maps package names to directories. In this case, it specifies that package should be found in 'src' dir
# packages = this parameter specifies which packages should be included in distribution

# find_packages() function is used to automatically discover packages under the 'src' dir and include them in distribution
# there is mlproject inside 'src' which is having __init__ so it will create mlproject as local package
# don't think like that inside there are many folders the why there are also not made local packages?
# bcoz whatever inside 'mlproject' is accessible if we can access 'mlproject'
# thats why we give dir as 'src' not 'mlproject' otherwise it will create all the folders in mlproject also local packages which is unnecessary

# we don't need to explicitly use package_dir argument
# and we don't have to explicitly pass where = "src" inside find_packages() as it will search whole root directory