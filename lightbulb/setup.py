from setuptools import setup, find_packages

setup(
    name='lightpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA functions to generate various metrics python package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/Ndu3000/Eskom-Data-Functions/tree/master/lightbulb', 
    author='Selebogo Mosoeu, Nompilo Nhlabathi, Caryn Pialat, Nduduzo Phili',
    author_email='scmosoeu@gmail.com, nompilomapilos@gmail.com, caryn.oates@gmail.com, nduduzo.phili@gmail.com'
)