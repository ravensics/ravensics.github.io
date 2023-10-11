import re

# Define the input and output file paths
input_file = r"C:/Users/kertz/Documents/GitHub/ravensics.github.io/_posts/2023-10-07-TISC2023-writeup.md"
output_file = r"C:/Users/kertz/Documents/GitHub/ravensics.github.io/_posts/2023-10-07-TISC2023-writeup-new.md"

# Define the pattern to match the old image reference format
pattern = r'!\[(.*?)\]\({{ site.url }}{{ site.baseurl }}/assets/images/TISC2023/../../_resources/([^)]+)\)'

# Define the replacement format
replacement = r'![\1]({{ site.url }}{{ site.baseurl }}/assets/images/TISC2023/\2)'

# Read the content of the input file
with open(input_file, 'r') as file:
    content = file.read()

# Use regular expressions to find and replace the old format with the new format
new_content = re.sub(pattern, replacement, content)

# Write the updated content to the output file
with open(output_file, 'w') as file:
    file.write(new_content)

print(f"Conversion complete. Output saved to {output_file}")