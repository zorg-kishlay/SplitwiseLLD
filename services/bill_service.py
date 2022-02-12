from models.bill import Bill
from services.bill_service_interface import BillServiceInterface


class BillService(BillServiceInterface):
    bill_details = {}

    def add_bill(self, id, group_id, amount, paid_by, contribution):
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(group_id)
        bill.setAmount(amount)
        bill.setPaidBy(paid_by)
        bill.setContri(contribution)
        self.__class__.bill_details[id] = bill
        return bill
