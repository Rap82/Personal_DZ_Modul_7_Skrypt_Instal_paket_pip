from setuptools import setup , find_namespace_packages

setup (
    name='clean_folder',
    version='1.0.0',
    description='Sorted file s folder',
    url='https://github.com/Rap82',
    author='Rap82',
    author_email='andrewrizh@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts':['clean-folder = clean_folder.clean:sort'] }
)