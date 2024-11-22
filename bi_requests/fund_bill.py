import dax
from .abstract import RequestAbstract


class FundBillAccountAvailablePayment(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_ACCOUNT_AVAILABLE_PAYMENT

    def beautify(self):
        self.beautify_result = {}


class FundBillAccountBalance(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_ACCOUNT_BALANCE

    def beautify(self):
        self.beautify_result = {}


class FundBillComBreachOfContract(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_COM_BREACH_OF_CONTRACT

    def beautify(self):
        self.beautify_result = {}


class FundBillComReceiptProgress(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_COM_RECEIPT_PROGRESS

    def beautify(self):
        self.beautify_result = {}


class FundBillContractPaymentProgress(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_CONTRACT_PAYMENT_PROGRESS

    def beautify(self):
        self.beautify_result = {}


class FundBillDepositPayable(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_DEPOSIT_PAYABLE

    def beautify(self):
        self.beautify_result = {}


class FundBillDepositPaymentDetail(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_DEPOSIT_PAYMENT_DETAIL

    def beautify(self):
        self.beautify_result = {}


class FundBillDepositPerfBondRelease(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_DEPOSIT_PERF_BOND_RELEASE

    def beautify(self):
        self.beautify_result = {}


class FundBillGoodsPay(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_GOODS_PAY

    def beautify(self):
        self.beautify_result = {}


class FundBillInvoiceHasBeenIssued(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_INVOICE_HAS_BEEN_ISSUED

    def beautify(self):
        self.beautify_result = {}


class FundBillIssuedInvoiceDetail(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_ISSUED_INVOICE_DETAIL

    def beautify(self):
        self.beautify_result = {}


class FundBillMonthlyStatement(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_MONTHLY_STATEMENT

    def beautify(self):
        self.beautify_result = {}


class FundBillNotIssuedInvoiceDetail(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_NOT_ISSUED_INVOICE_DETAIL

    def beautify(self):
        self.beautify_result = {}


class FundBillPayablePaymentDetail(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_PAYABLE_PAYMENT_DETAIL

    def beautify(self):
        self.beautify_result = {}


class FundBillPaymentDetail(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_PAYMENT_DETAIL

    def beautify(self):
        self.beautify_result = {}


class FundBillPerformanceBondPayable(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_PERFORMANCE_BOND_PAYABLE

    def beautify(self):
        self.beautify_result = {}


class FundBillTransferRequestProgress(RequestAbstract):
    DAX_QUERY_STR = dax.FUND_BILL_TRANSFER_REQUEST_PROGRESS

    def beautify(self):
        self.beautify_result = {}
