import json

DATA_FILE = 'animals_data.json'
TEMPLATE_FILE = 'animals_template.html'
OUTPUT_FILE = 'animals.html'


def load_data(file_path):
    """Loads the animal data with UTF-8 encoding."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_unique_skin_types(data):
    """Extracts unique skin types for the menu."""
    skin_types = set()
    for animal in data:
        skin = animal.get("characteristics", {}).get("skin_type")
        if skin:
            skin_types.add(skin)
    return sorted(list(skin_types))


def serialize_animal(animal_obj):
    """Serializes animal data into the professional HTML card format."""
    output = '<li class="cards__item">\n'
    name = animal_obj.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'
    char = animal_obj.get("characteristics", {})

    fields = {
        "Diet": char.get("diet"),
        "Location": animal_obj.get("locations", [None])[0],
        "Type": char.get("type"),
        "Skin Type": char.get("skin_type", "Not specified")
    }

    for label, value in fields.items():
        if value:
            output += f'      <strong>{label}:</strong> {value}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    animals_data = load_data(DATA_FILE)

    # 1. Display the Menu
    available_skins = get_unique_skin_types(animals_data)
    print("Available options:")
    print("- All (Show every animal)")
    print("- None (Show animals with missing skin type)")
    for skin in available_skins:
        print(f"- {skin}")

    # 2. Capture User Input
    user_choice = input("\nEnter your choice: ").strip().lower()

    # 3. Filter and Serialize
    full_animals_html = ""
    match_count = 0

    for animal in animals_data:
        animal_skin = animal.get("characteristics", {}).get("skin_type")

        # LOGIC: Determine if this animal should be included
        is_match = False

        if user_choice == "all":
            is_match = True
        elif user_choice == "none" and animal_skin is None:
            is_match = True
        elif animal_skin and animal_skin.lower() == user_choice:
            is_match = True

        if is_match:
            full_animals_html += serialize_animal(animal)
            match_count += 1

    # 4. Final Generation
    if match_count == 0:
        full_animals_html = f"<h2>No results found for: '{user_choice}'</h2>"
        print(f"No matches found.")
    else:
        print(f"Found {match_count} matches. Updating {OUTPUT_FILE}...")

    # Load template and write file
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", full_animals_html)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    print("Success!")


if __name__ == "__main__":
    main()