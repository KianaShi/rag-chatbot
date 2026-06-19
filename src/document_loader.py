# Input: file_path
# Output: list[str]
# Behavior:
# Ignore empty lines.
# Different file formats should return the same output structure.

def load_document(filepath):
    f = open(filepath)
    lines = f.read().split("\n")
    result = [line.strip() for line in lines if line.strip() != ""]
    f.close()
    return result