employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
#    emp_mod =  [ map(mod,emp) for emp in employee_list ]
#    return [ mod for mod in emp_mod]
    map_emp = map(mod,employee_list)
    print(map_emp)
    return [ emp for emp in map_emp ]


print(to_mod_list(employee_list))