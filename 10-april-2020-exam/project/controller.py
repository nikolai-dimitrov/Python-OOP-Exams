from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def add_player(self, *args):
        # add option to check if player.name in added_players do not add player before for-a.
        added_player_names = []
        for player in args:  # check if player exists it will return empty list!!
            if not any([p.name == player.name for p in self.players]):
                self.players.append(player)
                added_player_names.append(player.name)
        return f"Successfully added: {', '.join(added_player_names)}"

    def add_supply(self, *args):
        for supp in args:
            self.supplies.append(supp)  # extend or self.supplies + args but must make args to list first.

    def find_supply(self, sustenance_type: str):
        for supp in reversed(self.supplies):
            if supp.__class__.__name__ == sustenance_type:
                return supp
        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")
        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        allowed_types = ["Drink", "Food"]
        if sustenance_type not in allowed_types:
            return  # maybe could remove this return and write if sustanance in allower and player :
        supply = self.find_supply(sustenance_type)
        player = self.find_player(player_name)
        if player:
            if player.stamina == 100:
                return f"{player_name} have enough stamina."
            player._sustain_player(supply)
            self.supplies.remove(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def attack(p1, p2):
        reduce_stamina = (p1.stamina / 2)
        if p2.stamina - reduce_stamina <= 0:
            p2.stamina = 0
        else:
            p2.stamina -= reduce_stamina
        return p1.stamina  # try without return and , in duel try without first_player_stamina variable

    @staticmethod
    def check_stamina_negative(*args):
        result = []
        for p in args:
            if p.stamina == 0:
                result.append(f"Player {p.name} does not have enough stamina.")
        return result

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self.find_player(first_player_name)
        player_2 = self.find_player(second_player_name)
        ready_for_duel = self.check_stamina_negative(player_1, player_2)
        if ready_for_duel:
            return '\n'.join(ready_for_duel)
        player_1, player_2 = sorted([player_1, player_2], key=lambda x: x.stamina)
        first_player_stamina = self.attack(player_1, player_2)
        if first_player_stamina == 0:
            return f"Winner: {player_2.name}"
        second_player_stamina = self.attack(player_2, player_1)
        if first_player_stamina < second_player_stamina:
            return f"Winner: {player_2.name}"
        if first_player_stamina > second_player_stamina:
            return f"Winner: {player_1.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        result += '\n'.join([str(x) for x in self.players]) + '\n'
        result += '\n'.join([x.details() for x in self.supplies])
        return result.strip()




controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
