class Shop:
    total_number_of_items_sold = 0

    def __init__(self, name_of_shop, number_of_items_sold):
        self.name_of_shop = name_of_shop
        self.number_of_items_sold = number_of_items_sold
        Shop.total_number_of_items_sold += self.number_of_items_sold

    def add_sold_items_for_shop(self, number):
        self.number_of_items_sold += number
        Shop.total_number_of_items_sold += number

    def number_of_items_in_the_shop(self):
        return self.number_of_items_sold

    @staticmethod
    def total_number_of_items():
        return Shop.total_number_of_items_sold
