import hou
import json

# Set the frame range
start_frame = 1043
end_frame = 1053

# Get the selected node, assuming it's a SOP node
node = hou.selectedNodes()[0]

# Initialize an empty list to store data for each frame
frames_data = []

# Loop through the specified frame range
for frame_number in range(start_frame, end_frame + 1):
    # Set the current frame in Houdini
    hou.setFrame(frame_number)

    # Get the geometry at the current frame
    geo = node.geometry()

    # Prepare an empty list to store transform data for each point
    transforms_data = []

    # Iterate through each point in the geometry
    for point in geo.points():
        # Get the world transform (including position)
        world_position = point.position()

        # Prepare a dictionary for each point's transform data
        transform_info = {
            "point_number": point.number(),
            "position": {
                "x": world_position[0],
                "y": world_position[1],
                "z": world_position[2]
            }
        }

        # Append the transform data to the list
        transforms_data.append(transform_info)

    # Store data for the current frame in a structured way
    frame_data = {
        "frame": frame_number,  # Include the frame number as part of the data
        "points": transforms_data
    }
    
    # Append the frame data to the frames list
    frames_data.append(frame_data)

# Define the output file path (you can customize this)
output_file_path = "D:/guilhem/transforms_animated.json"

# Write the transform data to the JSON file
with open(output_file_path, 'w') as json_file:
    json.dump(frames_data, json_file, indent=4)

print(f"Transform data successfully written to {output_file_path}")