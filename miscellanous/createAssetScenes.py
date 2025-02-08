import os
import shutil

def copy_and_rename_files(template_path, output_dir,assetName,increment):

    asset_dir = os.path.join(output_dir, assetName,"maya","scenes","geo")

    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)

    new_name = f"MCH_itm_{assetName}_geo_E_{increment}.ma"
    new_file_path = os.path.join(asset_dir, new_name)
    shutil.copyfile(template_path, new_file_path)


def copy_and_rename_houdini_files(template_path, output_dir,assetName,increment):

    asset_dir = os.path.join(output_dir, assetName,"houdini","scenes","ldv")

    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)

    new_name = f"MCH_itm_{assetName}_ldv_E_{increment}.hipnc"
    new_file_path = os.path.join(asset_dir, new_name)
    shutil.copyfile(template_path, new_file_path)

if __name__ == "__main__":
    template_file = r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\MCH_Template\MCH_template_anim_P.ma"
    houdini_template_file=r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\MCH_Template\MCH_template_ldv_014.hipnc"
    output_directory = r"\\MINERVA\3d4_23_24\MECHA\04_asset\03_item"
    assetName="mgaScanIcelandicRock_caillou"
    increment="001"
    list=["sh190","sh195","sh185","sh201","sh202","sh205","sh210"]

    copy_and_rename_files(template_file, output_directory,assetName,increment)
    copy_and_rename_houdini_files(houdini_template_file, output_directory,assetName,increment)
    #for shot in list:
    #    copy_and_rename_files(template_file, output_directory,sequence,shot,increment)