
import random

class NeuralNetNomads:
    def __init__(self):
        self.player_health = 100
        self.player_code = 15  # Increased starting code
        self.player_energy = 10 # Increased starting energy
        self.inventory = {}
        self.location = "Core Node"
        self.network_map = {
            "Core Node": {"data": 10, "energy": 5, "enemies": 2},
            "Data Stream": {"data": 20, "energy": 10, "enemies": 5},
            "Edge Node": {"data": 5, "energy": 2, "enemies": 1}
        }
        # Create a lowercase version of the network map keys for robust lookup
        self.network_map_lower_keys = {k.lower(): k for k in self.network_map.keys()}

        self.known_recipes = {"basic_tool": {"code": 10, "energy": 5}}

        print("Welcome to Neural Net Nomads!")
        print("You are a digital consciousness uploaded to a vast neural network.")
        print("Gather data, energy, and craft tools to survive and explore!")

    def display_status(self):
        print(f"\n--- Current Status ---")
        print(f"Location: {self.location}")
        print(f"Health: {self.player_health}")
        print(f"Code Fragments: {self.player_code}")
        print(f"Energy: {self.player_energy}")
        print(f"Inventory: {self.inventory}")
        print(f"----------------------")

    def explore(self):
        print(f"Exploring {self.location}...")
        current_node = self.network_map.get(self.location, {})

        data_found = random.randint(0, current_node.get("data", 0))
        energy_found = random.randint(0, current_node.get("energy", 0))
        enemies_encountered = random.randint(0, current_node.get("enemies", 0))

        self.player_code += data_found
        self.player_energy += energy_found

        print(f"Found {data_found} Code Fragments and {energy_found} Energy.")

        if enemies_encountered > 0:
            print(f"Encountered {enemies_encountered} rogue algorithms!")
            # Simple combat: lose health based on enemies
            damage = enemies_encountered * 5
            self.player_health -= damage
            print(f"Lost {damage} health in combat. Current health: {self.player_health}")
            if self.player_health <= 0:
                print("Your digital consciousness has been corrupted. Game Over!")
                return False
        return True

    def craft(self, item_name):
        if item_name in self.known_recipes:
            recipe = self.known_recipes[item_name]
            if self.player_code >= recipe["code"] and self.player_energy >= recipe["energy"]:
                self.player_code -= recipe["code"]
                self.player_energy -= recipe["energy"]
                self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
                print(f"Successfully crafted {item_name}!")
            else:
                print(f"Not enough resources to craft {item_name}. Requires {recipe['code']} Code and {recipe['energy']} Energy.")
        else:
            print(f"Unknown recipe: {item_name}")

    def move(self, new_location_input):
        # Strip quotes and convert input to lowercase for lookup against our lowercase map
        cleaned_location_input = new_location_input.strip('"')
        new_location_lower = cleaned_location_input.lower()
        if new_location_lower in self.network_map_lower_keys:
            # Get the original (correctly cased) location name from our map
            actual_location_name = self.network_map_lower_keys[new_location_lower]
            self.location = actual_location_name
            print(f"Moved to {self.location}.")
        else:
            print(f"Cannot move to unknown location: {new_location_input}")

    def display_recipes(self):
        print("\n--- Known Recipes ---")
        for item, costs in self.known_recipes.items():
            cost_str = ", ".join([f"{count} {res.replace('code', 'Code Fragments').replace('energy', 'Energy')}" for res, count in costs.items()])
            print(f"{item}: {cost_str}")
        print("---------------------")

    def meditate(self):
        energy_cost = 5
        health_gain = 20
        if self.player_energy >= energy_cost:
            self.player_energy -= energy_cost
            self.player_health = min(100, self.player_health + health_gain)
            print(f"You meditate, regaining {health_gain} health at the cost of {energy_cost} energy. Current health: {self.player_health}")
        else:
            print(f"Not enough energy to meditate. Requires {energy_cost} energy.")


    def play(self):
        while self.player_health > 0:
            self.display_status()
            action = input("What do you want to do? (explore/craft [item]/move [Location Name]/recipes/meditate/quit): ").lower().strip()

            if action == "explore":
                if not self.explore():
                    break
            elif action.startswith("craft"):
                parts = action.split(" ", 1)
                if len(parts) > 1:
                    self.craft(parts[1])
                else:
                    print("Please specify an item to craft.")
            elif action.startswith("move"):
                parts = action.split(" ", 1)
                if len(parts) > 1:
                    # Pass the raw input for the location to the move method
                    self.move(parts[1])
                else:
                    print("Please specify a location to move to.")
            elif action == "recipes":
                self.display_recipes()
            elif action == "meditate":
                self.meditate()
            elif action == "quit":
                print("Exiting Neural Net Nomads. Until next time!")
                break
            else:
                print("Invalid action. Try again.")

if __name__ == "__main__":
    game = NeuralNetNomads()
    game.play()
