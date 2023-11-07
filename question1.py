

#completed function
import json
from typing import List, Dict, Any



filepath = "shapes.json"


def read_json_array(FILEPATH: str) -> List[Dict[str, Any]]:
    shape_coordinates = []
    
    # Open the file at the specified FILEPATH
    with open(FILEPATH, 'r') as file:
        try:
            # Parse the entire file as a JSON array
            shape_coordinates = json.load(file)
        except json.JSONDecodeError:
            print("Error: The file does not contain a valid JSON array.")
    
    return shape_coordinates
print("worked")



read_json_array(filepath)
	