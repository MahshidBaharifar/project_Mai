from data import stock


def update_id_func(stock):
        # Create a dictionary to store the result
    stock_dict = {}

    # Generate a unique ID for each item and create a new dictionary
    for i, item in enumerate(stock):
        item_id = i + 1  # Unique ID starting from 1
        stock_dict[item_id] = item
    # Write the resulting dictionary with the unique ID to the file
    for item_id, item in stock_dict.items():
             print(f"ID: {item_id}, Item: {item}")
    return 1


def revenue_func(stock):
    # add revenue key to each item 
    import random
    #because we have no data to add using the random mathod  
    for item in stock:
            item['revenue'] = random.randint(100, 1500)
            print(f"{item}")
    return 1



def update_func(stock):
    #update any category user want and determine which category should be changed
    categories = set(item['category'] for item in stock)
    #print(categories)
    category_mapping = {index + 1: category for index, category in enumerate(categories)}
    #print(category_mapping)

    print("Choose a category:")
    for num, category in category_mapping.items():
        print(f"{num}: {category}")
    category_num = int(input("Enter the number of the category: "))
    selected_category = category_mapping.get(category_num)

    print("Choose the change you want to make:")
    print("1: Change state")
    print("2: Change warehouse")

    change_num = int(input("Enter the number of the change: "))

    if change_num == 1:
        new_state = input("Enter the new state: ")
        change_key = 'state'
    elif change_num == 2:
        new_warehouse = int(input("Enter the new warehouse: "))
        change_key = 'warehouse'

    for item in stock:
        if item['category'] == selected_category:
            item[change_key] = new_state if change_key == 'state' else new_warehouse

    
    print("Updated stock:\n")
    for item in stock:
        print(f"{item}\n")

def sort_revenue_func(stock):
    #sort the stock data file by the revenue descendingly
    def sort_helper(item):
        #to return the revenue value for each item
        return item['revenue']
    stock_sorted=sorted(stock,key=sort_helper)
    for item in stock_sorted:
        print(item)


def sort_dt_func(stock):
    #sort the file and write it to the result_dt_sort
    from datetime import datetime  
    
    def sort_helper(item):
        return datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
    # Sort the stock list by date_of_stock
    sorted_stock = sorted(stock, key=sort_helper)
    #print out the output of the sorted list

    for item in sorted_stock:
        item["date_of_stock"] =datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        print(f"{item}" )
    return 1

def cate_occu_func(stock):
    category_dict = {}
    for item in stock:
        cat_type = item['category']
        if cat_type not in category_dict:
            category_dict[cat_type] = 0
        category_dict[cat_type] += 1

    print("Category Occurrence Report:")
    for item, count in category_dict.items():
        print(f"{item}: {count}")

def state_occu_func(stock):
    state_dict = {}
    for item in stock:
        state = item['state']
        if state not in state_dict:
            state_dict[state] = 0
        state_dict[state] += 1

    print("State Occurrence Report:")
    for item, count in state_dict.items():
        print(f"{item}: {count}")

def warehouse_occu_func(stock):
    warehouse_dict = {}
    for item in stock:
        warehouse = item['warehouse']
        if warehouse not in warehouse_dict:
            warehouse_dict[warehouse] = 0
        warehouse_dict[warehouse] += 1

    print("Warehouse Occurrence Report:")
    for item, count in warehouse_dict.items():
        print(f"{item}: {count}")

def category_on_warehouse(stock):
    cate_ware_dict = {}

    # Iterate through the stock items
    for item in stock:
        category_key = item['category']

        # Update the count for each category and warehouse
        if category_key not in cate_ware_dict:
            cate_ware_dict[category_key] = {}

        warehouse_key = f"warehouse {item['warehouse']}"
        if warehouse_key not in cate_ware_dict[category_key]:
            cate_ware_dict[category_key][warehouse_key] = 0

        cate_ware_dict[category_key][warehouse_key] += 1

    # Print the results
    for category, warehouses in cate_ware_dict.items():
        print(f"{category}:")
        for warehouse, count in warehouses.items():
            print(f"Warehouse {warehouse}: {count}")

def warehouse_on_category(stock):
    cate_ware_dict = {}

    # Iterate through the stock items
    for item in stock:
        warehouse_key = f"warehouse {item['warehouse']}"
        category_key = f"{item['category']} {item['warehouse']}"

        # Update the count for each warehouse
        if warehouse_key not in cate_ware_dict:
            cate_ware_dict[warehouse_key] = {}

        if category_key not in cate_ware_dict[warehouse_key]:
            cate_ware_dict[warehouse_key][category_key] = 0

        cate_ware_dict[warehouse_key][category_key] += 1

    # Print the results
    for warehouse, categories in cate_ware_dict.items():
        print(f"Warehouse {warehouse}:")
        for category, count in categories.items():
            #print(f"{category}: {count}")
            print("{: >20} {: >20}".format(category,count))

def category_state_warehouse_func(stock):
    report = {}

    # Iterate through the stock items
    for item in stock:
        category = item['category']
        state = item['state']
        warehouse = f"warehouse {item['warehouse']}"

        # Update the report dictionary
        if category not in report:
            report[category] = {}

        if state not in report[category]:
            report[category][state] = {}

        if warehouse not in report[category][state]:
            report[category][state][warehouse] = 0

        report[category][state][warehouse] += 1

    # Print the report
    for category, states in report.items():
        print(f"{category}:")
        for state, warehouses in states.items():
            print(f"\t{state}:")
            for warehouse, count in warehouses.items():
                print(f"\t\t{warehouse}: {count}")

def cate_reve_func(stock):
    cate_reve={}
    for item in stock:
        category=item['category']
        if category not in cate_reve:
            cate_reve[category]=0
        cate_reve[category]+=item['revenue']
        for category,revenue in cate_reve.items():
          print(f"{category}:{revenue}\n") 

def cate_ware_reve_func(stock):
    cate_ware_reve_dict = {}
    for item in stock:
        category = item['category']
        warehouse = item['warehouse']
        revenue = item['revenue']
        if category not in cate_ware_reve_dict:
            cate_ware_reve_dict[category] = {}
        if warehouse not in cate_ware_reve_dict[category]:
            cate_ware_reve_dict[category][warehouse] = 0
        cate_ware_reve_dict[category][warehouse] += revenue

    # Print the result
        for category, warehouses in cate_ware_reve_dict.items():
            print(f"{category}:\n")
            for warehouse, revenue in warehouses.items():
                print(f"Warehouse {warehouse}: {revenue}\n")



def filter_datetime_func(stock):
    #return the filtered data by the datetime
    from datetime import datetime
    def get_datetime_from_input(prompt):
        #changing the string format to date time 
        while True:
            try:
                datetime_str = input(prompt)
                datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
                return datetime_obj
            except ValueError:
                print("Invalid datetime format. Please enter in the format: YYYY-MM-DD HH:MM:SS")

    # Prompt the user for the start and end datetimes
    print("Please enter the start datetime (YYYY-MM-DD HH:MM:SS):")
    start_datetime = get_datetime_from_input("> ")

    print("Please enter the end datetime (YYYY-MM-DD HH:MM:SS):")
    end_datetime = get_datetime_from_input("> ")

    # Filter data within the specified interval
    filtered_data = []
    for entry in stock:
        entry_datetime = datetime.strptime(entry["date_of_stock"], "%Y-%m-%d %H:%M:%S")
        if start_datetime <= entry_datetime <= end_datetime:
            filtered_data.append(entry)

    # Print the filtered data
    print("Filtered Data:")
    for entry in filtered_data:
        print(entry)

def filter_warehouse_func(stock):
    #filter by the warehouse number
    warehouse_number=int(input("Enter the warehouse number:"))
    filtered_stock = [entry for entry in stock if entry["warehouse"] == warehouse_number]
    for item in filtered_stock:
        print(item)  

def filter_state_func(stock):
    #filter by the state
   state_list =[]
   for item in stock:
        if item['state'] not in state_list:
            state_list.append(item['state'])
   print(state_list) 
   state = input("Enter the state:")
   filtered_stock = [entry for entry in stock if entry["state"] == state]
   for item in filtered_stock:
        print(item)

def filter_category_func(stock):
    #filter by the category
    category_list=[]
    for item in stock:
        if item['category'] not in category_list:
            category_list.append(item['category'])
    print(category_list)    
    category = input("Enter the category:")
    filtered_stock = [entry for entry in stock if entry["category"] == category]
    for item in filtered_stock:
        print(item)








print("**************Report Generator *******************")
print("*************Step 1:initial file**********************")
name=input("What is your name: ")
print(f"Welcom {name} to the Stock Report Generator ")
print("let's have a look on initial data ")
input("Are you ready:Yes(y)/No(n)")
for item in stock:
      print(item)


print("****************step 2:Update*********************")
print("Do you want to update it with unique id")
answer=input("Yes(y)/No(n)")
if answer in 'yY':
    update_id_func(stock)
print("There is no financial information in your stock data:")
print("Do you want  update stock with revenue column?")
answer=input("Yes(y)/No(n)")
if answer in 'yY':
    revenue_func(stock)
print("Do you want to make any changes to the file")
answer=input("Yes(y)/No(n)")
if answer in 'yY':
    update_func(stock)


print("***************step 3: Sort********************")

while True :
    print("Do you want to sort the data file:")
    answer=input("Yes(y)/No(n)")
    if answer in 'Yy':
        print("what do you want to sort by:")
        print("1:revenue")
        print("2:Datetime")
        sort=input("Select the number: ")
        if sort==1:
             sort_revenue_func(stock)
        else:
             sort_dt_func(stock)
                          
    else: 
         break

print("****************step 4:Analysis Report*******************")

while True:
    print("Do you want to see the occurrence report?")
    answer = input("Yes(y)/No(n): ")
    if answer in 'Yy':
        print("Choose the title of your report:")
        print("1: Occurrence for 'category'")
        print("2: Occurrence for 'state'")
        print("3: Occurrence for 'Warehouse'")

        sort = int(input("Select the number: "))
        if sort == 1:
            cate_occu_func(stock)
        elif sort == 2:
            state_occu_func(stock)
        else:
            warehouse_occu_func(stock)
    else:
        break


print("**************Step 5: Hierarchical Report*********************")
while True:
    print("Do you want to see the Hierarchical report?")
    answer = input("Yes(y)/No(n): ")
    if answer in 'Yy':
        print("Choose the title of your report:")
        print("1: category inventory in warehouses")
        print("2: warehouse inventory for categories")
        print("3: warehouse inventory for categories regarding the states")
        sort = int(input("Select the number: "))
        if sort == 1:
            category_on_warehouse(stock)
        elif sort == 2:
            warehouse_on_category(stock)
        else:
            category_state_warehouse_func(stock)
    else:
        break

print("*************Step 6:Financial Report**************** ")
while True:
    print("Do you want to see the Financial report?")
    answer = input("Yes(y)/No(n): ")
    if answer in 'Yy':
        print("Choose the title of your report:")
        print("1: Sort the items by revenue ")
        print("2: Aggregated revenue for categories")
        print("3: Aggregated revenue for categories in each warehouses")
        sort = int(input("Select the number: "))
        if sort == 1:
            sort_revenue_func(stock)
        elif sort == 2:
            cate_reve_func(stock)
        else:
            cate_ware_reve_func(stock)
    else:
        break


print("*****************step 7: Filter*******************")
while True:
    print("Do you want to see the Filter data?")
    answer = input("Yes(y)/No(n): ")
    if answer in 'Yy':
        print("Choose the title of your report:")
        print("1: filter by datetime  ")
        print("2: filter by warehouse")
        print("3: filter by state")
        print("4: filter by category")
        sort = int(input("select the number"))
        if sort == 1:
            filter_datetime_func(stock)
        elif sort == 2:
            filter_warehouse_func(stock)
        elif sort==3:
            filter_state_func(stock)
        else:
           filter_category_func(stock)
    else:
        break
