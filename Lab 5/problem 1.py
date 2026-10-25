resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(resource_list):
    if not resource_list:
        print("No resources available in the system.")
        return
    
    print(f"{'ID':<5} | {'Name':<15} | {'Category':<15} | {'Quantity'}")
    print("-" * 50)
    for res in resource_list:
        print(f"{res[0]:<5} | {res[1]:<15} | {res[2]:<15} | {res[3]}")

def search_by_category(resource_list, category):
    print(f"\n--- Searching for category: '{category}' ---")
    found = False
    for res in resource_list:
        if res[2].lower() == category.lower():
            print(f"ID: {res[0]:<5} | Name: {res[1]:<15} | Qty: {res[3]}")
            found = True
            
    if not found:
        print(f"No resources found in the '{category}' category.")

def find_unavailable(resource_list):
    print("\n--- Unavailable Resources ---")
    if not resource_list:
        print("Resource list is empty.")
        return

    unavailable = [res for res in resource_list if res[3] <= 0]
    
    if not unavailable:
        print("All resources are currently available.")
    else:
        for res in unavailable:
            print(f"ID: {res[0]:<5} | Name: {res[1]:<15} | Qty: {res[3]}")

def search_by_id(resource_list, res_id):
    for res in resource_list:
        if res[0] == res_id:
            return res
    return None

display_resources(resources)
search_by_category(resources, "Electronics")
find_unavailable(resources)