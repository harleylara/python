def add_to_defult(my_list=[]):
    my_list.append(4)
    return my_list

def add_to_defult_return(my_list=[]):
    return my_list.append(4)

first_call = add_to_defult()
print(f"first_call (add_to_defult): {first_call = }")

second_call = add_to_defult()
print(f"second_call (add_to_defult): {second_call = }")

first_call_return = add_to_defult_return()
print(f"first_call (add_to_defult_return): {first_call_return = }")

second_call_return = add_to_defult_return()
print(f"second_call (add_to_defult_return): {second_call_return = }")

def mutable_default(my_list=None):
    my_list = my_list or []
    my_list.append(4)
    return my_list
