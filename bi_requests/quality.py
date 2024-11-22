import dax
from .abstract import RequestAbstract


class QualityQualityTestReport(RequestAbstract):
    DAX_QUERY_STR = dax.QUALITY_QUALITY_TEST_REPORT

    def beautify(self):
        self.beautify_result = {}


class QualityTestReport(RequestAbstract):
    DAX_QUERY_STR = dax.QUALITY_TEST_REPORT

    def beautify(self):
        self.beautify_result = {}
