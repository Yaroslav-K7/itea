class Shop:
    total_number_of_items_sold = 0

    def __init__(self, name_of_shop, number_of_items_sold):
        self.name_of_shop = name_of_shop
        self.number_of_items_sold = number_of_items_sold

    def add_the_number_of_sold_items(self):
        Shop.total_number_of_items_sold += self.number_of_items_sold

    @staticmethod
    def print_total_number():
        return Shop.total_number_of_items_sold
