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
    threading.Thread(target=test).start()


def test():
    test_file = os.path.join(os.path.dirname(__file__), 'core', 'diff.py')
    print('test_file', test_file)
    with open(test_file, 'r') as file:
        text = file.read()

    def inner():
        for t in range(1, 10):
            for n in range(20):
                try:
                    with open(test_file, 'w') as file:
                        file.write(ADD_TEXT.format(n) + text)
                except Exception as e:
                    print(
                        "Attempt {} with {} timeout failed."
                        .format(n, 0.05 * t)
                    )
                    raise e from None
                time.sleep(0.05 * t)
                os.remove(test_file)

    try:
        inner()
    finally:
        time.sleep(0.5)
        with open(test_file, 'w') as file:
            file.write(text)

        print('FIN')
