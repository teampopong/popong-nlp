# Deployment instructions
# 1. $ sudo make testpypi
# 2. $ sudo make pypi
# 3. Push tag
#

testpypi:
	python setup.py register -r pypitest
	python setup.py sdist --formats=gztar,zip upload -r pypitest
	pip install -i https://testpypi.python.org/pypi popong-nlp --upgrade

pypi:
	python setup.py register -r pypi
	python setup.py sdist --formats=gztar,zip upload -r pypi
	pip install konlpy --upgrade
