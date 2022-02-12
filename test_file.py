from controllers.bill_controller import BillController
from controllers.group_controller import GroupController
from controllers.user_controller import UserController
from services.bill_service import BillService
from services.group_service import GroupService
from services.user_service import UserService

user_controller = UserController(UserService())
group_controller = GroupController(GroupService())
bill_controller = BillController(BillService())

user1 = user_controller.add_user('User-1', 'Test_User1')
user2 = user_controller.add_user('User-2', 'Test_User2')
user3 = user_controller.add_user('User-3', 'Test_User3')
user4 = user_controller.add_user('User-4', 'Test_User4')

group_members = [user1, user2, user3, user4]

group1 = group_controller.add_group('Group-1', 'Group', group_members)
paid_by = {'User-1': 200, 'User-2': 300, 'User-3': 0, 'User-4': 50}
contri = {'User-1': 100, 'User-2': 200, 'User-3': 100, 'User-4': 150}

bill = bill_controller.add_bill('bill1', group1.getId(), 550, paid_by, contri)
balance = bill_controller.get_user_balance('User-3')

print(balance)