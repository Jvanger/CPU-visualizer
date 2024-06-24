# CPU Usage Visualizer

This Python script visualizes CPU usage by dynamically changing the desktop wallpaper color. The color transitions from green (low CPU usage) through yellow to red (high CPU usage), providing a visual indicator of system load.

## Features

- Real-time CPU usage monitoring
- Dynamic wallpaper color changes based on CPU load
- Smooth color transitions
- Configurable update intervals
- Error handling and logging

## Requirements

- macOS (tested on macOS Catalina and later)
- Python 3.7+

## Dependencies

This script relies on the following Python libraries:

- `psutil`: For CPU usage monitoring
- `Pillow` (PIL): For image processing
- `colorsys`: For color space conversions

You can install these dependencies using pip: pip install psutil Pillow 

## Setup

1. Clone this repository or download the script.
2. Ensure you have a white background image to use as the base wallpaper.
3. Update the `original_wallpaper` path in the script to point to your white background image.
4. Make sure the script has permission to change your desktop wallpaper:
   - Go to System Preferences > Security & Privacy > Privacy
   - Select "Full Disk Access" from the left sidebar
   - Click the lock icon to make changes (enter your password)
   - Click the "+" button and add Terminal (or the application you're using to run the script)

## Usage

Run the script from the terminal:python3 cpuVisual.py

The script will start monitoring CPU usage and updating the wallpaper color accordingly. To stop the script, press Ctrl+C in the terminal.

## How It Works

1. **CPU Monitoring**: The script uses `psutil` to measure CPU usage every 10 seconds.

2. **Color Mapping**: CPU usage percentage is mapped to a color hue:
   - 0% (Low usage) → Green (Hue 0.33)
   - 50% (Medium usage) → Yellow (Hue 0.17)
   - 100% (High usage) → Red (Hue 0.0)

3. **Image Processing**: The script applies a color tint to a white background image using PIL.

4. **Wallpaper Update**: The tinted image is saved as a temporary file and set as the desktop wallpaper using AppleScript.

## Customization

- Adjust the `time.sleep()` value in the main loop to change how often the wallpaper updates.
- Modify the `get_color_info()` function to change the color mapping or add more color stages.
- Update the `apply_tint()` function to alter the intensity of the tint.

## Troubleshooting

If the wallpaper isn't changing:
1. Ensure the script has necessary permissions (see Setup step 4).
2. Check the console output for any error messages.
3. Verify that the paths for `original_wallpaper` and `temp_wallpaper` are correct.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [psutil documentation](https://psutil.readthedocs.io/en/latest/)
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
