import os
import shutil

def copy_and_rename_files(template_path, output_dir,sequence,shot,increment):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over shots
    seq_dir = os.path.join(output_dir, sequence)
    shot_dir = os.path.join(seq_dir, shot,"anim")

    if not os.path.exists(shot_dir):
        os.makedirs(shot_dir)
    # Copy and rename template file
    template_name = os.path.basename(template_path)

    new_name = f"MCH_{sequence}_{shot}_anim_E_{increment}.ma"
    new_file_path = os.path.join(shot_dir, new_name)
    shutil.copyfile(template_path, new_file_path)

if __name__ == "__main__":
    template_file = r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\MCH_Template\MCH_template_anim_P.ma"
    output_directory = r"\\MINERVA\3d4_23_24\MECHA\06_shot"
    sequence="seq030"
    shot="sh099"
    increment="002"
    list=["sh190","sh195","sh185","sh201","sh202","sh205","sh210"]

    copy_and_rename_files(template_file, output_directory,sequence,shot,increment)
    #for shot in list:
    #    copy_and_rename_files(template_file, output_directory,sequence,shot,increment)