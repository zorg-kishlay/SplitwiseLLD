class BillController:
    def __init__(self, bill_service):
        self.bill_service = bill_service

    def add_bill(self, id, group_id, amount, paid_by, contribution):
        return self.bill_service.add_bill(id, group_id, amount, paid_by, contribution)

    def get_user_balance(self, userId):
        balance = 0
        for billId in self.bill_service.bill_details:
            bill = self.bill_service.bill_details.get(billId)
            if userId in bill.getContri():
                balance = balance - bill.getContri().get(userId)
            if userId in bill.getPaidBy():
                balance = balance + bill.getPaidBy().get(userId)

        return balance
