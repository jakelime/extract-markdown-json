import re
import json


fpath = "20240626_114859.txt"
# data = json.loads(fpath)

with open(fpath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    markdown_content = "\n".join(lines)

# print(markdown_content)
# Regular expression pattern to match JSON data
json_pattern = r"`json\s*(\[\{.*?\}\])\s*`"

# Extract the JSON data
match = re.search(json_pattern, markdown_content, re.DOTALL)
if match:
    json_data = match.group(1)
    print("Extracted JSON data:")
    print(json_data)
    data = json.loads(json_data)
    print(f"SUCCESS!\n{data=}")
else:
    print("FAIL!\nNo valid JSON data found in the Markdown content.")
