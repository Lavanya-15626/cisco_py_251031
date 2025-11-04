from product import Product
import repo

def menu():
    option_str = '''Options are
1 - Create Product
2 - Search Product
3 - Update Cost and Stock 
4 - Delete Product
5 - List All Products
6 - Exit
Your Choice:'''
    choice = int(input(option_str))

    if choice == 1:
        id = input('ID:')
        name = input('Name:')
        description = input('Description:')
        price = input('Price:')
        stock = input("Stock:")
        tags = input("Tags:")
        old_product = repo.search_product(id)
        if old_product:
            print('ID already exist.')
        else:
            repo.add_product(Product(id=id, name=name, description=description, price=price, stock=stock,tags=tags))
            print(f'Product {name} added successfully')
    elif choice == 2:
        id = input('ID:')
        old_product = repo.search_product(id)
        if not old_product:
            print('Product Not Found.')
        else:
            print(old_product)
    elif choice == 3:
        id = input('ID:')
        old_product = repo.search_product(id)
        if not old_product:
            print('Product Not Found.')
        else:
            print(old_product)
            new_price = input('New Price:')
            new_stock = input("New Stock:")
            repo.update_product(id, new_price,new_stock)
            print(f'Product {old_product.name} price and stock updated successfully')
    elif choice == 4:
        id = input('ID:')
        old_product = repo.search_product(id)
        if not old_product:
            print('Product Not Found.')
        else:
            print(old_product)
            if input('Are you sure to delete(y/n)?').upper() == 'Y':
                repo.delete_product(id)
                print(f'Product deleted successfully')
    elif choice == 5:
        products = repo.read_all_products()
        if len(products) == 0:
            print('No product exist.')
        else:
            print('List of Products:')
            for product in products:
                print(product)
    elif choice == 6:
        print('Thank you for using the application')
    else:
        print('No such option is available. Give proper option.')

    return choice 

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()
    print('End of application.')

menu()