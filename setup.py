import setuptools

setuptools.setup(
    name='wqp',
    version='1.0.0',
    author='fmoncaut@email.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn>=1.0.0",
        "pandas>=1.3.0"
    ]
)
