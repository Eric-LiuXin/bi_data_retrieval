import dax
from .abstract import RequestAbstract


class InformationComplaintProgress(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_COMPLAINT_PROGRESS

    def beautify(self):
        self.beautify_result = {}


class InformationCustomerGroup(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_CUSTOMER_GROUP

    def beautify(self):
        self.beautify_result = {}


class InformationCustomerId(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_CUSTOMER_ID

    def beautify(self):
        self.beautify_result = {}


class InformationCustomerProduct(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_CUSTOMER_PRODUCT

    def beautify(self):
        self.beautify_result = {}


class InformationCustomerStatus(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_CUSTOMER_STATUS

    def beautify(self):
        self.beautify_result = {}


class InformationFactoryMailingDocAddress(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_FACTORY_MAILING_DOC_ADDRESS

    def beautify(self):
        self.beautify_result = {}


class InformationFactoryPickupAddress(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_FACTORY_PICKUP_ADDRESS

    def beautify(self):
        self.beautify_result = {}


class InformationGlbYqqNotEnableList(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_GLB_YQQ_NOT_ENABLE_LIST

    def beautify(self):
        self.beautify_result = {}


class InformationLdcshReceiveBankAccount(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_LDCSH_RECEIVE_BANK_ACCOUNT

    def beautify(self):
        self.beautify_result = {}


class InformationPoaNotReturnList(RequestAbstract):
    DAX_QUERY_STR = dax.INFORMATION_POA_NOT_RETURN_LIST

    def beautify(self):
        self.beautify_result = {}
