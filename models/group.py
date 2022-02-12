class Group:

    def __init__(self):
        self.id = None
        self.members = []
        self.name = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMembers(self, members):
        self.members = members

    def getMembers(self):
        return self.members