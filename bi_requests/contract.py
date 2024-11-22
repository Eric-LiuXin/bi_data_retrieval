import json

import dax
from .abstract import RequestAbstract


class ContractCloseDetail(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_CLOSE_DETAIL

    def beautify(self):
        self.beautify_result = {}


class ContractCompanyDetail(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_COMPANY_DETAIL

    def beautify(self):
        self.beautify_result = {}


class ContractExeOrder(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_EXE_ORDER

    def beautify(self):
        self.beautify_result = {}


class ContractExeProgress(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_EXE_PROGRESS

    def beautify(self):
        self.beautify_result = {}


class ContractLateState(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_LATE_STATE

    def beautify(self):
        self.beautify_result = {}


class ContractNotReturnedList(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_NOT_RETURNED_LIST

    def beautify(self):
        self.beautify_result = {}


class ContractTodayQuotation(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_TODAY_QUOTATION

    def beautify(self):
        self.beautify_result = {}


class ContractTodayStatusDetail(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_TODAY_STATUS_DETAIL

    def beautify(self):
        self.beautify_result = {}


class ContractToBePaidDetail(RequestAbstract):
    DAX_QUERY_STR = dax.CONTRACT_TO_BE_PAID_DETAIL

    def beautify(self):
        self.beautify_result = {}
