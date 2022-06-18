# region Exercise 1
def id_to_fruit(fruit_id, fruits):
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")


# The fruits are passed to the function as a set, which causes an error
# because the set does not have access to the elements through the index.
# As a result, the fruits must be sent to the function as a list or tuple.

# name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
# name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
# name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"})

name1 = id_to_fruit(1, ("apple", "orange", "melon", "kiwi", "strawberry"))
name3 = id_to_fruit(3, ("apple", "orange", "melon", "kiwi", "strawberry"))
name4 = id_to_fruit(4, ("apple", "orange", "melon", "kiwi", "strawberry"))

print(name1)
print(name3)
print(name4)
# endregion
