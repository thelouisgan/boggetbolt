# boggetbolt

# BOGGETBOLT Championships 2023: Automating Key Moments with Arduino and Python

Welcome to the electrifying **BOGGETBOLT CHAMPIONSHIPS 2023 LIVE from Iskandar Puteri!** This exhilarating event showcases a high-speed showdown where runners sprint from Level 3 down the staircase in a thrilling test of speed and endurance.

In an effort to capture and highlight key moments of this adrenaline-pumping race, an Arduino-based setup paired with Python automation has been ingeniously employed. An Arduino Ultrasonic Sensor is strategically placed to detect a specific signal — "BOGGETBOLT".

The Python script, connected to the Arduino via a serial connection, listens for this signal. Upon detecting "BOGGETBOLT", the script triggers an action using the PyAutoGUI library. It simulates a keyboard press, specifically the 'B' key, which correlates to an event of importance within the race.

**How It Works:**
- The Arduino Ultrasonic Sensor acts as a signaling device, detecting the crucial "BOGGETBOLT" cue.
- Python's serial library listens to the connected Arduino for incoming messages.
- Upon receiving the designated signal, PyAutoGUI executes a keystroke emulation, simulating a press of the 'B' key.

This automation enables the system to mark significant race moments in real-time, providing a synchronized mechanism for capturing and documenting highlights of the event. The Python script is designed to contribute to the seamless flow of live updates, ensuring that the audience is engaged and informed about pivotal occurrences throughout the race.

🌟 **Join us on BBTV Livestreams 1 and 2** as we broadcast every heart-pounding moment of this thrilling race! Experience the thrill alongside us as we share lightning-fast speeds and unveil the top 3 leaderboard contenders vying for victory! 🥇🥈🥉

The atmosphere is charged with excitement as the system actively contributes to an immersive viewing experience. Stay tuned for the jaw-dropping displays of athleticism and determination at the **BOGGETBOLT CHAMPIONSHIPS 2023!** 🌟🎉
