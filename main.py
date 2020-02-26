# -*- coding: utf-8 -*-
import os
import custom_db_manager
import openfoodfacts_client
import menu
import option
import mysql.connector.errors


class Main():

    def __init__(self):

        self.db = custom_db_manager.CustomDBManager()
        self.menu = menu.Menu()
        if self.db.is_empty:
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.set_database(self.off_client.products)

    def clear_screen(self):
        os.system('cls||clear')

    def choose_in_main_menu(self):
        return self.menu.choose_in_main_menu()

    def select_product(self):
        category = self._select_category()
        products_list = self.db.get_products_from_category(category)
        products_set = self.menu.remove_duplicates(products_list)
        products_option = option.Option(
                f'Produits de la catégorie {category} :', products_set)
        selected_product = self.menu.choose(products_option)
        input(f'Produit sélectionné : {selected_product.brand} - '
              f'{selected_product.name}, '
              f'nutriscore : {selected_product.nutriscore.upper()}. \n'
              f'Appuyez sur Entrée pour voir les substituts '
              f'(meilleur nutriscore) : ')
        return selected_product

    def select_substitute(self, product):
        substitutes_list = self.db.get_products_with_better_nutriscore(product)
        if substitutes_list:
            substitutes_option = option.Option(
                f'Substituts avec un nutriscore meilleur '
                f'que {product.nutriscore.upper()} :',
                substitutes_list)
            selected_substitute = self.menu.choose(substitutes_option)
            return selected_substitute
        else:
            print("Il n'existe aucun substitut avec un meilleur nutriscore.")
            self._press_enter()
            return None

    def save_substitution(self, origin, substitute):
        try:
            self.db.save_substitution(origin, substitute)
        except mysql.connector.errors.IntegrityError:
            print("L'enregistrement existe déjà.")
        else:
            print(
                f"La substitution du produit {origin.brand} - {origin.name} "
                f"par {substitute.brand} - {substitute.name} a bien été "
                f"enregistrée."
            )
        finally:
            self._press_enter()

    def reset_app(self):
        warning = ("\nATTENTION : Cette opération réinitialisera "
                   "la base de données.\nToutes les substitutions "
                   "enregistrées seront DEFINITIVEMENT effacées. "
                   "\nVoulez-vous continuer ?\n"
                   "Tapez 'oui' + Entrée pour confirmer, ou "
                   "appuyez sur Entrée pour annuler : ")
        confirmation = input(warning)

        if confirmation.lower() == 'oui':
            print('Réinitialisation en cours...')
            self.db.empty_database()
            self.off_client = openfoodfacts_client.OpenFoodFactsClient()
            self.db.set_database(self.off_client.products)
            message = ('Réinitialisation terminée.')
        else:
            message = ('Opération annulée.')
        print(message)
        self._press_enter()

    def quit_app(self):
        self.db.close_database()
        print('Au revoir !')
        quit()

    def _select_category(self):
        '''
        Ask user to choose a category of products. Returns category object.
        '''
        categories_options = option.Option('CATEGORIES',
                                           self.db.get_categories())
        selected_category = self.menu.choose(categories_options)
        return selected_category

    def _press_enter(self):
        input("Appuyez sur ENTREE pour revenir au menu principal :")


if __name__ == '__main__':
    app = Main()
    quit_app = False
    while not quit_app:
        app.clear_screen()
        result = app.choose_in_main_menu()
        if result == 1:
            app.clear_screen()
            product = app.select_product()
            substitute = app.select_substitute(product)
            if substitute:
                substitute.display()
                save = ''
                while save.lower() not in ('s', 'm'):
                    save = input('Entrez S pour sauvegarder la substitution '
                                 'ou M pour revenir au menu principal : ')
                    if save.lower() == "s":
                        app.save_substitution(product, substitute)
                    else:
                        pass

        elif result == 2:
            app.show_substitutions()
        elif result == 3:
            app.reset_app()
        elif result == 4:
            quit_app = True
    app.quit_app()
