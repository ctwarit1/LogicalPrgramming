"""
You bought a few bunches of fruit over the weekend.
Create a function that splits a bunch into singular
objects inside an array.
Examples
splitBunches([
  { name: "grapes", quantity: 2 }
]) ➞ [
  { name: "grapes", quantity: 1 },
  { name: "grapes", quantity: 1 }
]
splitBunches([
  { name: "currants", quantity: 1 },
  { name: "grapes", quantity: 2 },
  { name: "bananas", quantity: 2 }
]) ➞ [
  { name: "currants", quantity: 1},
  { name: "grapes", quantity: 1 },
  { name: "grapes", quantity: 1 },
  { name: "bananas", quantity: 1 },
  { name: "bananas", quantity: 1 }
]
Notes
The input array will never be empty.
Objects will always have a name and quantity over 0.
The returned object should have each fruit in the same order as the original.
"""


def split_bunches(bunches):
    result = []
    for bunch in bunches:
        name = bunch["name"]
        quantity = bunch["quantity"]
        for _ in range(quantity):
            result.append({"name": name, "quantity": 1})
    print(result)


split_bunches([
    {"name": "grapes", "quantity": 2}
])

split_bunches([
    {"name": "currants", "quantity": 1},
    {"name": "grapes", "quantity": 2},
    {"name": "bananas", "quantity": 2}
])
