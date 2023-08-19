  GNU nano 6.2                                                                                                                        extract2.py                                                                                                                                  
import json

def extract_keys(obj, seen_keys=None, seen_structures=None):
    if seen_keys is None:
        seen_keys = set()

    if seen_structures is None:
        seen_structures = []

    if isinstance(obj, dict):
        key_structure = {}
        for key, value in obj.items():
            if key not in seen_keys:
                seen_keys.add(key)
                key_structure[key] = extract_keys(value, seen_keys, seen_structures)
            else:
                key_structure[key] = "..."
        return key_structure

    elif isinstance(obj, list):
        key_structure = []
        for item in obj:
            temp_structure = extract_keys(item, seen_keys.copy(), seen_structures)
            if temp_structure not in seen_structures:
                seen_structures.append(temp_structure)
                key_structure.append(temp_structure)
        return key_structure

    else:
        return "..."


if __name__ == "__main__":
    with open("YOUR_FILE_TO_PARSE.json", "r") as f:
        data = json.load(f)

    keys_structure = extract_keys(data)

    with open("output_keys_structure.json", "w") as out_file:
        json.dump(keys_structure, out_file, indent=4)

    print("Keys structure saved to output_keys_structure.json")
