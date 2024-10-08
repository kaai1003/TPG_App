#!/usr/bin/python3
"""test Models behaviour"""

from models.connectors import Connector
from models.testmodules import TestModule
from models.testprobes import TestProbe
from models.suppliers import Supplier
from models.users import User
from models import storage

print('-------------Create new User------------')
user = {'user': 'kacem', 'password': 'abcd1234', 'role': 'admin'}
new_user = User(**user)
storage.new(new_user)
storage.save()
print(user)
print('-------------Create suppliers------------')
supplier1 = {'name': 'EMDEP', 'type': 'TestModules', 'user_id': new_user.id}
supplier2 = {'name': 'Tyco', 'type': 'Connectors', 'user_id': new_user.id}
supplier3 = {'name': 'Ingun', 'type': 'TestProbes', 'user_id': new_user.id}
suppl1 = Supplier(**supplier1)
storage.new(suppl1)
suppl2 = Supplier(**supplier2)
storage.new(suppl2)
suppl3 = Supplier(**supplier3)
storage.new(suppl3)
storage.save()
print('suppliers added succesfully')
print('-------------Create Connector------------')
con1 = {'part_number': 'P00023432', 'terminals': 6, 'supplier_id': suppl2.id, 'user_id': new_user.id}
connector1 = Connector(**con1)
storage.new(connector1)
print(connector1)
print('-------------Create TestProbe------------')
tb1 = {'serial_number': 'FZ0002',
       'stock_location': 'A23',
       'pushback': False,
       'supplier_id': suppl3.id,
       'user_id': new_user.id}
probe1 = TestProbe(**tb1)
storage.new(probe1)
storage.save()
print(probe1)
print('-------------Create Test Module------------')
tm1 = {'serial_number': 'P00023432',
       'terminals': 6,
       'pushback': False,
       'supplier_id': suppl1.id,
       'connector_id': connector1.id,
       'probeid_1': probe1.id,
       'user_id': new_user.id}
testmodule1 = TestModule(**tm1)
storage.new(testmodule1)
print(testmodule1)
storage.save()