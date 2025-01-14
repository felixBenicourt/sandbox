




import unreal

metahuman_performance_path = "/Game/cali_christian/NewMetaHumanPerformance"
metahuman_performance = unreal.EditorAssetLibrary.load_asset(metahuman_performance_path)

export_range = unreal.PerformanceExportRange.WHOLE_SEQUENCE

if metahuman_performance:
    try:
        metahuman_performance.export_animation(export_range)
        unreal.log("Animation export initiated.")
    except Exception as e:
        unreal.log_error(f"Failed to export animation: {str(e)}")
else:
    unreal.log_error("Failed to load MetaHumanPerformance asset.")   





"""
import unreal

def create_animation_sequence(metahuman_skeletal_mesh_path, existing_animation_path, new_sequence_name, output_path):
    # Load the MetaHuman Skeletal Mesh
    skeletal_mesh = unreal.EditorAssetLibrary.load_asset(metahuman_skeletal_mesh_path)
    if not skeletal_mesh:
        unreal.log_error("Failed to load skeletal mesh: {}".format(metahuman_skeletal_mesh_path))
        return

    # Load the existing animation sequence
    existing_animation = unreal.EditorAssetLibrary.load_asset(existing_animation_path)
    if not existing_animation:
        unreal.log_error("Failed to load existing animation: {}".format(existing_animation_path))
        return

    # Retrieve the skeleton from the skeletal mesh
    skeleton = skeletal_mesh.get_editor_property('skeleton')
    if not skeleton:
        unreal.log_error("Failed to get skeleton from skeletal mesh: {}".format(metahuman_skeletal_mesh_path))
        return

    # Create an Animation Sequence Factory and set the skeleton
    animation_sequence_factory = unreal.AnimationSequenceFactory()
    animation_sequence_factory.set_editor_property('skeletal_mesh', skeletal_mesh)

    # Create a new animation sequence using the factory
    new_animation_sequence = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
        new_sequence_name,
        output_path,
        unreal.AnimSequence.static_class(),
        animation_sequence_factory
    )

    if not new_animation_sequence:
        unreal.log_error("Failed to create animation sequence: {}".format(new_sequence_name))
        return

    # Copy the existing animation data to the new animation sequence
    for track in existing_animation.get_transform_tracks():
        new_track = new_animation_sequence.add_new_bone_track(track.get_name())
        for time, transform in track.get_transforms():
            new_track.add_transform(time, transform)

    # Mark the new animation sequence as modified
    new_animation_sequence.mark_package_dirty()

    unreal.log("Successfully created animation sequence: {}".format(new_sequence_name))

# Example usage
create_animation_sequence(
    "/Game/MetaHumans/Ada/Face/Ada_FaceMesh.Ada_FaceMesh",
    "/Game/cali_christian/NewMetaHumanPerformance",
    "NewMetaHumanAnimation",
    "/Game/cali_christian/"  # Output path for the new animation
)
"""
