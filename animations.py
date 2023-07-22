import time
import os

def animate_interface():
    animation_frames = [
        """
        [+] Sending
        """,
        """
        [+] Sending.
        """,
        """
        [+] Sending..
        """,
        """
        [+] Sending...
        """
    ]

    while True:
        for frame in animation_frames:
            os.system('clear')
            print(frame)
            time.sleep(0.2)