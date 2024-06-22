import psutil
import colorsys
import time
from PIL import Image
import os
import subprocess
import traceback

def get_color_info(cpu_percentage):
    # Transition from green (0.33) to red (0.0)
    hue = 0.33 - (cpu_percentage / 100) * 0.33
    
    # Increase saturation and value for more vibrant colors
    saturation = 0.8
    value = 0.9

    # Map the hue to a color word
    if hue > 0.275:
        color_word = 'Green'
    elif hue > 0.165:
        color_word = 'Yellow-Green'
    elif hue > 0.055:
        color_word = 'Yellow'
    elif hue > 0.025:
        color_word = 'Orange'
    else:
        color_word = 'Red'

    return color_word, hue, saturation, value


def apply_tint(image_path, tint_color, intensity=0.7):
    original = Image.open(image_path).convert('RGB') 
    tint = Image.new('RGB', original.size, tint_color)
    tinted = Image.blend(original, tint, intensity)
    return tinted.convert('RGB')  # Ensure the image is in RGB mode

#Using AppleScript to set the wallpaper
def set_wallpaper(image_path):
    try:
        subprocess.run([
            "osascript",
            "-e",
            f'tell application "System Events" to set picture of every desktop to "{image_path}"'
        ], check=True)
        print(f"Wallpaper set to {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set wallpaper: {e}")

def simulate_cpu_usage():
    # This will cycle through the full range of CPU usage every 100 seconds
    return (time.time() % 100)

if __name__ == '__main__':
    original_wallpaper = "/Users/jonathan/Desktop/Photos/white.jpg"
    temp_wallpaper = "/Users/jonathan/Desktop/CPU visualizer/temp_wallpaper.jpg"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(temp_wallpaper), exist_ok=True)
    
    try:
        while True:
            try:
                # cpu_percent = psutil.cpu_percent()
                cpu_percent = simulate_cpu_usage()
                color_word, hue, saturation, value = get_color_info(cpu_percent)
                print(f'CPU Usage: {cpu_percent}%')
                print(f'Color Word: {color_word}')
                
                # Get RGB color from hue, saturation, and value
                rgb = colorsys.hsv_to_rgb(hue, saturation, value)
                tint_color = tuple(int(x * 255) for x in rgb)
                
                # Apply tint and set wallpaper
                tinted_image = apply_tint(original_wallpaper, tint_color)
                tinted_image.save(temp_wallpaper, 'JPEG')
                set_wallpaper(temp_wallpaper)
                print("Wallpaper updated")
                
                time.sleep(3)  # Wait for 10 seconds before checking again
            except Exception as e:
                print(f"An error occurred: {e}")
                print(traceback.format_exc())
                time.sleep(3)  # Wait before trying again
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_wallpaper):
            os.remove(temp_wallpaper)
        print("Temporary file removed. Goodbye!")