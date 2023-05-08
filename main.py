import json

print("-------------------------------")
print("-----CRUD System on Python-----")
print("-------------------------------")

def create_data():
    with open("product.json", "r") as getdata:
        data = json.load(getdata)

    id = input("Enter product ID: ")
    if id == "":
        print("ERROR: Please try again")
        return
    
    if id in [m["Product ID:"] for m in data.values()]:
        print("ERROR: Product ID already exists")
        return

    name = input("Enter Product name: ")
    diagonal = float(input("Enter diagonal: "))

    dic = {
        "Product ID:": id,
        "Product Name:": name,
        "Diagonal:": diagonal,
    }

    data[id] = dic

    with open("product.json", "w") as save:
        json.dump(data, save)
        print("Added!")

def read_data():

    with open("product.json", "r") as view:
        data = json.load(view)
        
        for i, m in data.items():
            for x, n in m.items():
                print(x, n)
            print()

def sort_data():
    print("\n1. Sort with ID")
    print("\n2. Sort with Name")
    print("\n3. Sort with Diagonal\n")

    enter_sort = int(input("Enter Choice: "))

    with open("product.json", "r") as view:
        data = json.load(view)
        if enter_sort == 1:
            sorted_data = sorted(data.items(), key=lambda x: int(x[1]['Product ID:']))
        elif enter_sort == 2:
            sorted_data = sorted(data.items(), key=lambda x: x[1]['Product Name:'])
        elif enter_sort == 3:
            sorted_data = sorted(data.items(), key=lambda x: float(x[1]['Diagonal:']))
        else:
            print("ERROR: Try Again")
            return
        
        for i, m in sorted_data:
            for x, n in m.items():
                print(x, n)
            print()

def update_data():
    id = input("Enter product ID: ")

    with open("product.json", "r") as getdata:
        data = json.load(getdata)

        if id in data:
            name = input("Enter new Name: ")
            diagonal = input("Enter new Diagonal: ")

            dic = {
                "Product ID: " : id,
                "Product Name: " : name,
                "Diagonal: " : diagonal
            }

            data[id] = dic
            with open("product.json", "w") as update:
                json.dump(data, update)
                print("Updated!")

def delete_data():
    id = input("Enter product ID: ")

    with open("product.json", "r") as getdata:
        data = json.load(getdata)

        if id in data:
            data.pop(id)

            with open("product.json", 'w') as delete:
                data1 = json.dump(data, delete)
                print("Deleted!") 

def main():
    print("\n1. Create Data")
    print("\n2. Read Data")
    print("\n3. Update Data")
    print("\n4. Delete Data")
    print("\n5. Sort Data")
    print("\n6. Exit\n")

    enter = int(input("Enter Choice: "))

    if enter == 1:
        create_data()
        main()
    elif enter == 2:
        read_data()
        main()
    elif enter == 3:
        update_data()
        main()
    elif enter == 4:
        delete_data()
        main()
    elif enter == 5:
        sort_data()
        main()
    elif enter == 6:
        exit()
    else:
        print("ERROR: Try Again")

main()