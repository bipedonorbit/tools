import os
import shutil

def copy_and_rename_files(template_path, output_dir,sequence,shot,increment):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over shots
    seq_dir = os.path.join(output_dir, sequence)
    shot_dir = os.path.join(seq_dir, shot,"renderSetup")

    if not os.path.exists(shot_dir):
        os.makedirs(shot_dir)
    # Copy and rename template file
    template_name = os.path.basename(template_path)

    new_name = f"MCH_{sequence}_{shot}_renderSetup_E_{increment}.hipnc"
    new_file_path = os.path.join(shot_dir, new_name)
    shutil.copyfile(template_path, new_file_path)
    print(f"creating : {new_file_path}")

if __name__ == "__main__":
    template_file = r"\\MINERVA\3d4_23_24\MECHA\02_ressource\@LOUIS\MCH_Template\MCH_template_renderSetup_P.hipnc"
    output_directory = r"\\MINERVA\3d4_23_24\MECHA\06_shot"
    sequence="seq030"
    shot="sh210"
    increment="003"
    list=["sh010",
          "sh020",
          "sh025",
          "sh030",
          "sh035",
          "sh040",
          "sh060",
          "sh085",
          "sh098",
          "sh099",
          "sh105",
          "sh110",
          "sh170",
          "sh190",
          "sh200",
          "sh210",
          "sh230",
          "sh240",
          "sh250",
          "sh255",
          "sh260",
          "sh065",
          "sh270",
          "sh280",
          "sh290",
          "sh300",
          "sh305",
          "sh310",
          
          
          
          
          
          
          ]

    #copy_and_rename_files(template_file, output_directory,sequence,shot,increment)

    #for shot in list:
    #    copy_and_rename_files(template_file, output_directory,sequence,shot,increment)