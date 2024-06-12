from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ReactView(APIView):
    def get(self,request):
        output = 'hi all'
        return Response(output)
    
    def post(self,request):
        result = {'update added to json request'}
        response_data = {
                        'explanation': 
                                """
1. We start by creating an empty dictionary called `shopping_list` to store our shopping items and their quantities.
2. We use a `while` loop to repeatedly ask the user for items until they type "done" to finish.
3. Inside the loop, we first ask the user to enter an item. If the user types "done", the program exits the loop.
4. If the user enters an item, we then ask for the quantity of that item and store it in the `shopping_list` dictionary using the item as the key and the quantity as the value.
5. After the user finishes entering items, the program prints the final shopping list.""",

                        'output': """
shopping_list = {}
while True:
    item = input('Enter an item or type 'done' to finish: ')
    if item == 'done': break
    quantity = input(f'Enter the quantity for {item}: ')
    shopping_list[item] = quantity
print(f'Your shopping list: {shopping_list}')""",

                        'pseudo_code': """
Initialize an empty shopping list

Repeat:
    Display "Enter an item or type 'done' to finish:"
    Get user input for the item

    If the item is "done":
        Break out of the loop

    Display "Enter the quantity for [item]:"
    Get user input for the quantity

    Add the item and quantity to the shopping list

Display the final shopping list"""}
        return Response(response_data)
    