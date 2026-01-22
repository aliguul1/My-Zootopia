import json


def load_data(file_path):
    """ Loads the animal data with UTF-8 encoding to handle special characters. """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    # 1. Load the animal data
    animals_data = load_data('animals_data.json')

    # 2. Generate the serialized HTML string
    output = ''
    for animal in animals_data:
        # Extract data
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")
        locations = animal.get("locations", [])

        # Start the Card Item
        output += '<li class="cards__item">\n'

        # Add the Professional Title
        if name:
            output += f'  <div class="card__title">{name}</div>\n'

        # Start the Text Block
        output += '  <p class="card__text">\n'

        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'
        if locations:
            output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
        if animal_type:
            # Note: We keep the field name as "Type" for the label
            output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

        # Close tags
        output += '  </p>\n'
        output += '</li>\n'

    # 3. Read the template with UTF-8
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # 4. Replace the placeholder
    final_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Write the final production file with UTF-8
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html_content)

    print("Success! Your professional 'animals.html' repository is ready and improved.")


if __name__ == "__main__":
    main()