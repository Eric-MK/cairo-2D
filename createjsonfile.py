import json

shapes = [
    {"shape": "rectangle", "x": 100, "y": 100, "width": 200, "height": 100},
    {"shape": "circle", "center_x": 300, "center_y": 300, "radius": 50},
    {"shape": "line", "x1": 50, "y1": 50, "x2": 250, "y2": 250},
]

file_path = "shapes.json"

with open(file_path, "w") as file:
    json.dump(shapes, file, indent=4)  # Serialize the list of shapes


