import dax
from .abstract import RequestAbstract


class FileCommonTemplate(RequestAbstract):
    DAX_QUERY_STR = dax.FILE_COMMON_TEMPLATE

    def beautify(self):
        self.beautify_result = {}


class FileRefundLetterTemplate(RequestAbstract):
    DAX_QUERY_STR = dax.FILE_REFUND_LETTER_TEMPLATE

    def beautify(self):
        self.beautify_result = {}
