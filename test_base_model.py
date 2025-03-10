#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()

my_model.name = "My First Model"
my_model.my_number = 89

#-------------------------
print("Printing before model\n")
print(my_model)
print()

my_model.save()

#-------------------------
print("Printing After model\n")
print(my_model)
print()

my_model_json = my_model.to_dict()

# --------Printing my_model_json---------
print(my_model_json)

print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("-----A-----")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("-----B------")
print(my_model is my_new_model)

