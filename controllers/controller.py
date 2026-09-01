from models.model import Product

products = []

product_id = 0


# CREATE
def create_product(product: Product):

    global product_id

    product_id += 1

    product.id = product_id

    products.append(product)

    return {
        "success": True,
        "message": "Product created successfully",
        "product": product
    }


# READ ALL
def get_products():

    return {
        "success": True,
        "message": "Products fetched successfully",
        "products": products
    }


# READ BY ID
def get_product_by_id(product_id: int):

    for product in products:

        if product.id == product_id:

            return {
                "success": True,
                "message": "Product fetched successfully",
                "product": product
            }

    return {
        "success": False,
        "message": "Product not found"
    }


# UPDATE
def update_product(product_id: int, updated_product: Product):

    for i in range(len(products)):

        if products[i].id == product_id:

            updated_product.id = product_id

            products[i] = updated_product

            return {
                "success": True,
                "message": "Product updated successfully",
                "product": updated_product
            }

    return {
        "success": False,
        "message": "Product not found"
    }


# DELETE
def delete_product(product_id: int):

    for i in range(len(products)):

        if products[i].id == product_id:

            products.pop(i)

            return {
                "success": True,
                "message": "Product deleted successfully"
            }

    return {
        "success": False,
        "message": "Product not found"
    }