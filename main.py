import machine, neopixel, time
num_pixels = 12
pixels = neopixel.NeoPixel(machine.Pin(22), num_pixels)
def switch_off():
    for i in range(12):
        pixels[i] = (0, 0, 0)
    pixels.write()
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.write()

# To Switch off light comment while loop & run only method call switch_off()
switch_off()
while True:
    rainbow_cycle(0)  # Increase the number to slow down the rainbow


