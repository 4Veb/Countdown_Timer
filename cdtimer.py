import time
import os

def countdown_timer(x: int, *, separator: str = ":", clear: bool = True) -> None:
    if not separator:
        separator: str = ":"

    for c in range(x, 0, -1):
        seconds: int = c % 60
        minutes: int = int(c / 60) % 60
        hours: int = int(c / 3600)

        if clear:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{hours:02}" + separator + f"{minutes:02}" 
                + separator + f"{seconds:02}")
        else:
            print(f"{hours:02}" + separator + f"{minutes:02}" 
                + separator + f"{seconds:02}")
        time.sleep(1)

# Example
if __name__ == "__main__":
    try:
        countdown_timer(60, clear=True)
    except KeyboardInterrupt:
        print("\r× Stopped by user.")
