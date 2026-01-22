import json
# Load data
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
# Main
def main():
    # Load the animal data
    animals_data = load_data('animals_data.json')

    # Iterate through the list of animals
    for animal in animals_data:
        # 1. Extract Name (Top level)
        name = animal.get("name")

        # 2. Extract Diet and Type (Nested inside 'characteristics')
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")

        # 3. Extract first Location (First item in 'locations' list)
        locations = animal.get("locations", [])
        if locations:
            first_location = locations[0]
        else:
            first_location = None

        # Printing logic: Only print if the field exists. Animal Type field sometimes doesn't exist
        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if first_location:
            print(f"Location: {first_location}")
        if animal_type:
            print(f"Type: {animal_type}")

        # Add a newline for better readability between animals
        print("")


if __name__ == "__main__":
    main()