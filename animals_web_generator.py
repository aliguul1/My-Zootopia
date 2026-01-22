import json


def load_data(file_path):
    """ Loads a JSON file with explicit UTF-8 encoding """
    # Added encoding="utf-8" here
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    # 1. Load data correctly
    animals_data = load_data('animals_data.json')

    # 2. Serialize data (Logic remains the same)
    output = ''
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")
        locations = animal.get("locations", [])

        output += '<li class="cards__item">\n'
        if name:
            output += f"  <div class='card__title'>{name}</div><br/>\n"
        if diet:
            output += f"  <strong>Diet:</strong> {diet}<br/>\n"
        if locations:
            output += f"  <strong>Location:</strong> {locations[0]}<br/>\n"
        if animal_type:
            output += f"  <strong>Type:</strong> {animal_type}<br/>\n"
        output += '</li>\n'

    # 3. Read template with UTF-8
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # 4. Replace placeholder
    final_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Write final file with UTF-8
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html_content)

    print("Success: file created successfully")


if __name__ == "__main__":
    main()
