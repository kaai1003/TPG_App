#!/usr/bin/python3
from models.users import User
from models import storage


user1 = {
    'user': 'aimad',
    'password': 'abcd1234',
    'role': 'admin'
}
new_user = User(**user1)
print(new_user)
storage.new(new_user)
storage.save()