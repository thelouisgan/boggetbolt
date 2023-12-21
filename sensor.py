import serial
import keyboard

# Replace '/dev/cu.usbserial-10' with your actual serial port
ser = serial.Serial('/dev/cu.usbserial-10', 9600)

while True:
    if ser.in_waiting:
        message = ser.readline().decode().strip()
        if message == "BOGGETBOLT":
            keyboard.press('b')
            keyboard.release('b')
            print("Pressed 'B' key")
