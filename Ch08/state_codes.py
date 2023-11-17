
state_codes = {}

state_codes["OH"] = "Ohio"
state_codes["IN"] = "Indiana"
state_codes["KY"] = "Kentucky"

print(f"The key 'IN' points to the value of {state_codes['IN']}")
print(f"The key 'KY' points to the value of {state_codes['KY']}")

customers_in_state = dict()
cust1 = "MAX", "OH"
cust2 = "Childrens Hospital", "OH"

if "OH" not in customers_in_state:
    customers_in_state["OH"] = 0

customers_in_state["OH"] += 1