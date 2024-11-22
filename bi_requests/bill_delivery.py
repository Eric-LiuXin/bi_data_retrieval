import dax
from .abstract import RequestAbstract


class BillDeliveryAssignableBillQuantity(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_ASSIGNABLE_BILL_QUANTITY

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryBillDetail(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_BILL_DETAIL

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryBillIssuedNotPickup(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_BILL_ISSUED_NOT_PICKUP

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryBillNotice(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_BILL_NOTICE

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryBoundBillTransferCount(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_BOUND_BILL_TRANSFER_COUNT

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryContractAvailableBill(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_CONTRACT_AVAILABLE_BILL

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryContractHasSentOut(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_CONTRACT_HAS_SENT_OUT

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryCustomerAvailableBill(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_CUSTOMER_AVAILABLE_BILL

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryDeliveryOrderState(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_DELIVERY_ORDER_STATE

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryInOutBoundData(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_IN_OUT_BOUND_DATA

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryLadingBillStatusDetail(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_LADING_BILL_STATUS_DETAIL

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryLimitedPickupPlanQuantity(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_LIMITED_PICKUP_PLAN_QUANTITY

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryLoadingPrepare(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_LOADING_PREPARE

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryLoadingTime(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_LOADING_TIME

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryOutboundDetail(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_OUTBOUND_DETAIL

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryTankerStandard(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_TANKER_STANDARD

    def beautify(self):
        self.beautify_result = {}


class BillDeliveryVehicleQueueStatus(RequestAbstract):
    DAX_QUERY_STR = dax.BILL_DELIVERY_VEHICLE_QUEUE_STATUS

    def beautify(self):
        self.beautify_result = {}
