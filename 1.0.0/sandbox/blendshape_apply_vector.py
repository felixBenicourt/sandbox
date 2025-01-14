

import json
import tensorflow

file_path_disp = "C://HOME//proj//template//lib//data//vertex_displacements.json"
file_path_target_neutral = "C://HOME//proj//template//lib//data//target_neutral_position.json"
output_file_path = "C://HOME//proj//template//lib//data//target_blendshape_initial.json"


with open(file_path_disp, "r") as json_file:
    data_vector = json.load(json_file)


with open(file_path_target_neutral, "r") as json_file:
    data_target_neutral = json.load(json_file)


target_blendshape_initial = {}


for key, displacement_vectors in data_vector.items():
    neutral_vectors = data_target_neutral["neutral"]
    blendshape_vectors = []

    for disp, neutral in zip(displacement_vectors, neutral_vectors):
        blendshape = [
            disp[0] + neutral[0],
            disp[1] + neutral[1],
            disp[2] + neutral[2], 
        ]
        blendshape_vectors.append(blendshape)

    target_blendshape_initial[key] = blendshape_vectors


with open(output_file_path, "w") as json_file:
    json.dump(target_blendshape_initial, json_file, indent=4)

print(f"Target blendshape initial saved to: {output_file_path}")


