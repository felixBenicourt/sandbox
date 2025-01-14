import unreal
import threading
import os

# Paths and asset names
full_path = "/Game/cali_christian"
asset_name = "NewMetaHumanPerformance"
video_path = "/Game/NewMetaHumanCaptureSource_Ingested/acting_3.acting_3"
ada_path = "/Game/MetaHumans/Ada/Face/Ada_FaceMesh.Ada_FaceMesh"  # Skeletal mesh path
meta_human_identity = "/Game/cali_felix/NewMetaHumanIdentity.NewMetaHumanIdentity"

# Desired file system export path (folder)
export_directory = r"C:\HOME\proj\template\chr\metahuman\rig\ada\test"  # Raw string for Windows paths

# Ensure the export directory exists
if not os.path.exists(export_directory):
    os.makedirs(export_directory)

# Function to retrieve skeleton from skeletal mesh
def get_skeleton_from_mesh(mesh_path):
    try:
        skeletal_mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)
        if not skeletal_mesh:
            unreal.log_error(f"Failed to load skeletal mesh from path: {mesh_path}")
            return None
        
        skeleton = skeletal_mesh.get_editor_property("skeleton")
        if skeleton:
            unreal.log(f"Successfully retrieved skeleton: {skeleton.get_name()} from skeletal mesh: {mesh_path}")
            return skeleton
        else:
            unreal.log_error(f"Failed to get skeleton from skeletal mesh: {mesh_path}")
            return None
    except Exception as e:
        unreal.log_error(f"Error retrieving skeleton from mesh: {str(e)}")
        return None


# Function to check if the baking process is complete
def check_pipeline_completion(asset=None, export_directory=None, time_check=3.0):
    def check():
        if asset.is_processing():
            unreal.log(f"Processing bake animation on: {asset.get_name()}")
            threading.Timer(time_check, check).start()  # Keep checking if the asset is still processing
        else:
            try:
                unreal.log(f"Processing completed for asset: {asset.get_name()}")
                if ada_skeleton:
                    unreal.log(f"Processing completed for asset: {ada_skeleton}")
                else:
                    unreal.log_warning(f"Failed to retrieve skeleton from mesh.")
            except Exception as e:
                unreal.log_error(f"Failed to create Animation Sequence: {str(e)}")

    check()

# Main execution
try:
    # Create directory if it doesn't exist
    if not unreal.EditorAssetLibrary.does_directory_exist(full_path):
        unreal.EditorAssetLibrary.make_directory(full_path)

    # Create MetaHumanPerformance asset
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    new_asset = asset_tools.create_asset(asset_name, full_path, unreal.MetaHumanPerformance, None)
    unreal.log(f"MetaHuman Performance asset '{asset_name}' created successfully in '{full_path}'.")

    # Load necessary assets
    footage_capture_data_instance = unreal.EditorAssetLibrary.load_asset(video_path)
    meta_human_identity_instance = unreal.EditorAssetLibrary.load_asset(meta_human_identity)
    
    # Set properties for the MetaHumanPerformance asset
    new_asset.set_editor_property("FootageCaptureData", footage_capture_data_instance)
    new_asset.set_editor_property("Identity", meta_human_identity_instance)
    new_asset.set_editor_property("HeadMovementMode", unreal.PerformanceHeadMovementMode.CONTROL_RIG)

    unreal.log("Successfully set FootageCaptureData, Identity, and HeadMovementMode.")

    # Start processing and checking
    if new_asset.can_process():
        new_asset.start_pipeline()
        unreal.log(f"Pipeline started for asset: {asset_name}.")
        ada_skeleton = get_skeleton_from_mesh(ada_path)  # Retrieve skeleton
        check_pipeline_completion(asset=new_asset, export_directory=export_directory)  # Remove character_skeleton parameter
    else:
        unreal.log_warning("Cannot process the asset.")

except Exception as e:
    unreal.log_error(f"Failed to set properties or export asset: {str(e)}")
