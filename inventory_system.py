from copy import deepcopy

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """

    # initialize a dictionary
    inventory = {
        'Electronics':{
            'Laptop': { 'name':'Laptop', 'price':800, 'quantity':8  },
        },
        
    }

    # Adding a new category using dict() constructor
    inventory['Groceries'] = {}
    inventory['Groceries']['Carrot']  = dict(name='Carrot', price=2, quantity=200) 
    inventory['Groceries']['Apple']  = dict([('name','Apple'), ('price',7), ('quantity',80)]) 
    
    # Adding items using dictionary comprehension
    keys = ('name','price','quantity')
    values = [ ['Headset',100, 50] , ['Television',500, 20] ]

    electronics = { val[0]:dict(zip(keys, val))   for val in values   }

    # Adding items using update
    inventory['Electronics'].update(electronics)

    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    inventory[category][item_name].update(update_info)
    return

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data. (e.g., increasing stock, updating price)
    """
    merged_dict = deepcopy(inv1)
    for ckey, cvalue in inv2.items():
        d1 = merged_dict.get(ckey,None)
        if not d1:
            merged_dict[ckey] = cvalue
        else:
            for key, value in cvalue.items():
                d1 = merged_dict[ckey].get(key,None)
                if not d1:
                    merged_dict[ckey][key] = value
                else:
                    merged_dict[ckey][key]['quantity'] = max( value['quantity'] , d1['quantity'] )
                    merged_dict[ckey][key]['price'] = max( value['price'] , d1['price'] )

    return merged_dict

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory[category]

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    mx = 0
    mx_item = None
    for key in inventory:
        max_dict = max(inventory[key].items(), key=lambda x: x[1]['price'])[1]
        if max_dict['price'] > mx:
            mx = max_dict['price']
            mx_item = max_dict

    return mx_item

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for key in inventory:
        if item_name in inventory[key]:
            return inventory[key][item_name]
    
    return

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return inventory.keys()

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    l = []
    for key in inventory:
        l.extend([ i for i in inventory[key].values() ])

    return l

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return [ [ key, val] for key, val in inventory.items() ]
    

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if deep:
        return deepcopy(inventory)
    else:
        return inventory.copy()
