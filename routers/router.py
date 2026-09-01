from fastapi import APIRouter

from models.model import Product
from controllers import controller


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# CREATE
@router.post("/")
def create_product(product: Product):

    return controller.create_product(product)


# READ ALL
@router.get("/")
def get_products():

    return controller.get_products()


# READ BY ID
@router.get("/{product_id}")
def get_product_by_id(product_id: int):

    return controller.get_product_by_id(product_id)


# UPDATE
@router.put("/{product_id}")
def update_product(product_id: int, product: Product):

    return controller.update_product(product_id, product)


# DELETE
@router.delete("/{product_id}")
def delete_product(product_id: int):

    return controller.delete_product(product_id)