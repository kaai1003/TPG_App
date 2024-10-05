#!/usr/bin/python3
"""test Models behaviour"""

from models.connectors import Connector
from models.testmodules import TestModule
from models.testprobes import TestProbe
from models.suppliers import Supplier

supplier1 = {'name': 'EMDEP', 'type': 'TestModules'}
supplier2 = {'name': 'Tyco', 'type': 'Connectors'}
supplier3 = {'name': 'Ingun', 'type': 'TestProbes'}
suppl1 = Supplier(**supplier1)
suppl2 = Supplier(**supplier2)
suppl3 = Supplier(**supplier3)
print(suppl1.to_dict())
print('----------------')
con1 = {'part_number': 'P00023432', 'terminals': 6, 'supplier_id': suppl2.id}
connector1 = Connector(**con1)
print(connector1.to_dict())
