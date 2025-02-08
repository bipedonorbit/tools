from moviepy.editor import VideoFileClip

def time_crop_video(input_video, output_video, start_time, end_time):
    # Load the video clip
    clip = VideoFileClip(input_video)
    
    # Crop the video based on time
    cropped_clip = clip.subclip(start_time, end_time)
    
    # Write the cropped video to a new file
    cropped_clip.write_videofile(output_video)

# Example usage
input_video = r"D:\refs mecha porn\Retours_RLO_04_03_24.mp4"
output_video = r"D:\refs mecha porn\RLOCropped.mp4"
start_time = 47  # Start time of the cropped segment in seconds
end_time = 90   # End time of the cropped segment in seconds

time_crop_video(input_video, output_video, start_time, end_time)