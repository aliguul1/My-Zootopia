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

        # # 2. Extract Diet and Type (Nested inside 'characteristics')
        # characteristics = animal.get("characteristics", {})
        # diet = characteristics.get("diet")
        # animal_type = characteristics.get("type")
        #
        # # 3. Extract first Location (First item in 'locations' list)
        # locations = animal.get("locations", [])
        # if locations:
        #     first_location = locations[0]
        # else:
        #     first_location = None
        #
        # # Printing logic: Only print if the field exists. Animal Type field sometimes doesn't exist
        # if name:
        #     print(f"Name: {name}")
        # if diet:
        #     print(f"Diet: {diet}")
        # if first_location:
        #     print(f"Location: {first_location}")
        # if animal_type:
        #     print(f"Type: {animal_type}")
        #
        # # Add a newline for better readability between animals
        # print("")
        # 2. Generate a string with the animals' data
        output = ''
        for animal in animals_data:
            # Use .get() to avoid errors with missing data
            name = animal.get("name")
            characteristics = animal.get("characteristics", {})
            diet = characteristics.get("diet")
            animal_type = characteristics.get("type")
            locations = animal.get("locations", [])
            if locations:
                first_location = locations[0]
            else:
                first_location = None
            # Build the string for this specific animal
            if name:
                output += f"Name: {name}\n"
            if diet:
                output += f"Diet: {diet}\n"
            if locations:
                output += f"Location: {locations[0]}\n"
            if animal_type:
                output += f"Type: {animal_type}\n"

            # Add a newline after each animal for spacing
            output += "\n"
    # 3. Read the content of the template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # 4. Replace the placeholder with the generated string
    final_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Write the new HTML content to a new file
    with open("animals.html", "w") as output_file:
        output_file.write(final_html_content)

    print("Success: 'animals.html' has been created.")

if __name__ == "__main__":
    main()