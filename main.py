# -*- coding: utf-8 -*-

import local_db_manager
import openfoodfacts_client
import config as cf


schema = cf.DB_SCHEMA
categories = cf.CATEGORIES
nb = cf.MAX_PRODUCTS_NB
db_fields = cf.DB_PRODUCT_FIELDS.keys()

# ##################################################
# Database creation
# ##################################################
db = local_db_manager.LocalDBManager()
db.connect_to_database()
db.create_tables(schema)
db.fill_category_table(categories)

# ##################################################
# Data retrieving from API as Product objects
# ##################################################
off_client = openfoodfacts_client.OpenFoodFactsClient()
products = off_client.get_Products_from_API(categories, nb)


for product in products:
    print(f'{product.brand} {product.name}'
          f', {product.quantity}, Nutriscore : {product.nutriscore.upper()}')

# db.fill_database(products)
