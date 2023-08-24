from rest_framework import serializers
from factory.constants import CONSTANTS
import random

class CreateOrderController:
    
    def create_order(self, data):
        total_price = 0
        components = data.get("components")
        description = []
        map = {
            "SCREEN": 0,
            "CAMERA": 0,
            "PORT": 0,
            "OS": 0,
            "BODY": 0
        }
        for item in components:
            item_list = CONSTANTS.MAP.get(item)
            map[item_list[0]] += 1
            total_price += item_list[1]
            description.append(item_list[2])
            
        all_values_are_one = all(value == 1 for value in map.values())
                
        if not all_values_are_one:
            error = CONSTANTS.GENERIC.BAD_REQUEST
            raise serializers.ValidationError({
                "status": error[0],
                "message": error[1]
            })
            
        response = {
            "order_id": random.randint(0,100),
            "total": total_price,
            "parts": description
        }
            
        return response