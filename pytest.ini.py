from imghdr import tests

import contained as contained
import pytest
import self as self
from _pytest import reports

[pytest]
addopts = -n auto --html=reports/test_report.html --self-contained-html
testpaths = tests


