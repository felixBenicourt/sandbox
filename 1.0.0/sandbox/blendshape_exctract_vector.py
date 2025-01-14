

import json


file_path = "C://HOME//proj//template//lib//data//vertex_positions.json"
output_file = "C://HOME//proj//template//lib//data//vertex_displacements.json"


with open(file_path, "r") as json_file:
    data = json.load(json_file)


neutral_vertices = data.pop("neutral")  

blendshapes = data

displacements = {}

for blendshape_name, blendshape_vertices in blendshapes.items():
    displacements[blendshape_name] = [
        [
            blendshape_vertex[0] - neutral_vertex[0],
            blendshape_vertex[1] - neutral_vertex[1],
            blendshape_vertex[2] - neutral_vertex[2],
        ]
        for neutral_vertex, blendshape_vertex in zip(neutral_vertices, blendshape_vertices)
    ]


with open(output_file, "w") as json_file:
    json.dump(displacements, json_file, indent=4)

print(f"Displacements have been saved to {output_file}")



