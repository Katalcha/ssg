import re

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    matched_regex = re.findall(regex, text)
    return matched_regex
