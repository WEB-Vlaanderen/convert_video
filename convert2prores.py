import os
import argparse
import subprocess
import glob

def convert_videos(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all video files in the input folder (assuming the input is .mov, adjust as needed)
    video_files = glob.glob(os.path.join(input_folder, '*.mov')) + glob.glob(os.path.join(input_folder, '*.MOV')) + glob.glob(os.path.join(input_folder, '*.mp4')) + glob.glob(os.path.join(input_folder, '*.MP4'))
    
    
    for video_file in video_files:
        # Extract the filename without extension
        filename = os.path.basename(video_file).split('.')[0]
        
        # Define the output file path
        output_file = os.path.join(output_folder, f"{filename}.mov")
        
        # ffmpeg command to convert the video
        if not os.path.exists(output_file):
            command = [
                'ffmpeg',
                '-n',
                '-i', video_file,
                '-c:v', 'prores_ks',
                '-profile:v', '4',
                '-c:a', 'pcm_s16le',
                '-pix_fmt', 'yuva444p10le',
                output_file
            ]
            
            # Run the ffmpeg command
            print(f"Converting {video_file} to {output_file}")
            subprocess.run(command, check=True)

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Convert all videos in the input folder to MOV format using ffmpeg.')
    parser.add_argument('--input_folder', type=str, help='Path to the input folder containing video files')
    parser.add_argument('--output_folder', type=str, help='Path to the output folder where converted videos will be saved')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the conversion function with the provided folders
    convert_videos(args.input_folder, args.output_folder)

if __name__ == '__main__':
    main()