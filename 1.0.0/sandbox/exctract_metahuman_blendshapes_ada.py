

import maya.cmds as cmds
import json


def list_custom_attributes(node_name):
    if not cmds.objExists(node_name):
        return []
    return cmds.listAttr(node_name, userDefined=True) or []

def disconnect_and_set_value(node_name, attribute_name, value):
    full_attr = "{}.{}".format(node_name, attribute_name)
    if cmds.connectionInfo(full_attr, isDestination=True):
        source_attr = cmds.connectionInfo(full_attr, sourceFromDestination=True)
        cmds.disconnectAttr(source_attr, full_attr)
    cmds.setAttr(full_attr, value)

def get_vertex_positions(mesh_name):
    if not cmds.objExists(mesh_name):
        return []
    vertex_count = cmds.polyEvaluate(mesh_name, vertex=True)
    positions = [tuple(cmds.xform("{}.vtx[{}]".format(mesh_name,i), query=True, translation=True, worldSpace=True))
                 for i in range(vertex_count)]
    return positions


node = "Ada_full_rig_CTRL_expressions"
mesh = "Ada_full_rig_head_lod0_mesh"
custom_attrs = list_custom_attributes(node)

dict_vtxPos = {}

neutral_vertex_positions = get_vertex_positions(mesh)
dict_vtxPos['neutral'] = neutral_vertex_positions

if custom_attrs:
    for attr in custom_attrs:
        disconnect_and_set_value(node, attr, 1)
        vertex_positions = get_vertex_positions(mesh)
        dict_vtxPos[attr] = vertex_positions
        cmds.setAttr("{}.{}".format(node, attr), 0)


output_file = "C:/pipeline/LOCAL/sandbox/1.0.0/sandbox/vertex_positions.json"

with open(output_file, "w") as json_file:
    json.dump(dict_vtxPos, json_file, indent=4)

print("Data saved to:", output_file)
