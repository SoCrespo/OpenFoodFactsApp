# -*- coding: utf-8 -*-


#######################################
# API PARAMETERS
#######################################

# CATEGORIES
#
# To change / add / update a category, use the following syntax:
# 'API_CATEGORY_NAME': 'CUSTOM_NAME'
# The API_CATEGORY_NAME MUST be a name provided by the API,
# The CUSTOM_NAME is a user-friendly version of API_CATEGORY_NAME.

# Choose categories that do not overlapp one another
# in OpenFoodFacts database.

CATEGORIES = {
    'pates-a-tartiner': 'Pâtes à tartiner',
    'matieres-grasses-a-tartiner': 'Matières grasses à tartiner',
    'pates-a-tartiner-a-base-de-levures': "Pâtes à tartiner à base de levures",
    'confitures-de-fruits': 'Confitures de fruits',
    'confiture-de-lait': 'Confitures de lait',
}

# NUMBER OF RETRIEVED PRODUCTS
#
# MAX_PRODUCT_NB is the maximum number of products that must be returned
# by each API call for a category.
# Given that some products informations are incomplete, ensure that this limit
# is at least 20 to get enough complete products, but not too high, for
# readability and connection time reasons (50 to 100 are a good limit).

MAX_PRODUCTS_NB = 50


#######################################
# DATABASE PARAMETERS
#######################################

# These parameters must be those of an existing database, emprty, with
# all privileges granted to mentioned user.

USER = 'offuser'
PASSWORD = 'my!pass1worD'
HOST = 'localhost'
DATABASE = 'offdb2020p5'
