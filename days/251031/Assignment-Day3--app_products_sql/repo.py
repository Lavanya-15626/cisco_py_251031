from db_setup import session,Product
def read_all_products():
    products=session.query(Product).all()
    return products


def add_product(product):
       session.add(product)
       session.commit()
       print('Product Added Successfully')
    
def search_product(id): 
    product = session.query(Product).filter_by(id=id).first()
    return product
 
def update_product(id, price,stock):
    old_product=search_product(id)
    if not old_product: 
        print('Product Not Found.')
    if old_product:
        old_product.price=price
        old_product.stock=stock
        session.commit()
        print('Product Upated Successfully')
   
def delete_product(id):
    old_product=search_product(id)
    if not old_product: 
        print('Product Not Found.')
        return
    session.delete(old_product)
    session.commit()
    print("Product deleted Successfully")