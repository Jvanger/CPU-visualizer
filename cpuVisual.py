import psutil
import colorsys
import time

def get_color_word(cpu_percentage):
    """
    Maps the CPU percentage to a color word using a smooth color transition.
    0% - 25%: Green to Yellow
    26% - 50%: Yellow to Orange
    51% - 75%: Orange to Red
    76% - 100%: Red to Dark Red
    """
    if cpu_percentage <= 25:
        hue = (cpu_percentage / 100) * 0.17  # Transition from Green (0.33) to Yellow (0.17)
    elif cpu_percentage <= 50:
        hue = 0.17 - (cpu_percentage - 25) / 100 * 0.09  # Transition from Yellow (0.17) to Orange (0.08)
    elif cpu_percentage <= 75:
        hue = 0.08 - (cpu_percentage - 50) / 100 * 0.08  # Transition from Orange (0.08) to Red (0.0)
    else:
        hue = 0.0 + (cpu_percentage - 75) / 100 * 0.08  # Transition from Red (0.0) to Dark Red (0.08)

    # Convert HSV to RGB and then to a hexadecimal color code
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    hex_color = '#{:02x}{:02x}{:02x}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

    # Map the hexadecimal color code to a color word
    if hex_color >= '#00ff00' and hex_color < '#80ff00':
        return 'Bright Green'
    elif hex_color >= '#80ff00' and hex_color < '#ffff00':
        return 'Green'
    elif hex_color >= '#ffff00' and hex_color < '#ff8000':
        return 'Yellow'
    elif hex_color >= '#ff8000' and hex_color < '#ff0000':
        return 'Orange'
    elif hex_color >= '#ff0000' and hex_color < '#800000':
        return 'Red'
    else:
        return 'Dark Red'



if __name__ == '__main__':
    while True:
        cpu_percent = psutil.cpu_percent()
        color_word = get_color_word(cpu_percent)
        print(f'CPU Usage: {cpu_percent}%')
        print(f'Color Word: {color_word}')
        time.sleep(1)  # Wait for 1 second before checking again