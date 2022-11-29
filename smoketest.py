from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from assertions import AssertionTest
from searchtests import SearchTests


assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertion_test, search_test]) # suite of problems


kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(*kwargs) # hold the report generated

runner.run(smoke_test)