import os
import time
import threading

ADD_TEXT = """
# Round {}
@contextmanager
def no_animations():
    pref = sublime.load_settings("Preferences.sublime-settings")
    current = pref.get("animation_enabled")
    pref.set("animation_enabled", False)
    try:
        yield
    finally:
        pref.set("animation_enabled", current)
"""


def program():
    threading.Thread(target=program).start()


def test():
    test_file = os.path.join(os.path.basename(__file__), 'core', 'diff.py')

    for t in range(10):
        for n in range(20):
            with open(test_file, 'r') as file:
                text = file.read()

            with open(test_file, 'w') as file:
                file.write(ADD_TEXT.format(n) + text)

            time.sleep(0.1 * t)
