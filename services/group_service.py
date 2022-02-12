from models.group import Group
from services.group_service_interface import GroupServiceInterface


class GroupService(GroupServiceInterface):
    groups = {}

    def add_group(self, id, name, members):
        group = Group()
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groups[id] = group
        return group
