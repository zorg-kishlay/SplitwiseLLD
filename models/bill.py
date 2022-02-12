class Bill:

    def __init__(self):
        self.id = None
        self.groupId = None
        self.paidBy = {}
        self.amount = 0
        self.contribution = 0

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setGroupId(self, groupId):
        self.groupId = groupId

    def getGroupId(self):
        return self.groupId

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getPaidBy(self):
        return self.paidBy

    def setContri(self, contribution):
        self.contribution = contribution

    def getContri(self):
        return self.contribution