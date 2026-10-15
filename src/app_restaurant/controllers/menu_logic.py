from ..models import base_models as BaseModel

def logic_get_all_dishes():
    """Return the entire dictionary of dishes"""
    return BaseModel.DISHES_DATA

def logic_add_dish(dish_id, name, cost):
    """Add a new dish to the menu"""
    # Convert dish_id to string in case the JSON keys are strings
    dish_id = str(dish_id) 
    
    if dish_id in BaseModel.DISHES_DATA:
        return False, f"Dish ID '{dish_id}' already exists!"
    
    if cost < 0:
        return False, "Invalid price!"

    BaseModel.DISHES_DATA[dish_id] = BaseModel.Dishes(name, cost)
    return True, f"Successfully added dish '{name}'!"

def logic_update_dish(dish_id, new_name=None, new_cost=None):
    """Update dish information"""
    dish_id = str(dish_id)
    
    if dish_id not in BaseModel.DISHES_DATA:
        return False, "Dish does not exist!"
        
    dish = BaseModel.DISHES_DATA[dish_id]
    
    if new_name:
        dish.name = new_name
    if new_cost is not None:
        if new_cost < 0:
            return False, "Invalid price!"
        dish.cost = new_cost
        
    return True, "Successfully updated dish!"

def logic_delete_dish(dish_id):
    """Remove a dish from the menu"""
    dish_id = str(dish_id)
    
    if dish_id in BaseModel.DISHES_DATA:
        dish = BaseModel.DISHES_DATA.pop(dish_id)
        return True, f"Successfully removed dish '{dish.name}'!"
        
    return False, "Dish does not exist!"
