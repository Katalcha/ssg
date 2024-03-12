def markdown_to_blocks(full_markdown_document):
    return_list = []
    for line in full_markdown_document.split("\n\n"):
        if line == "":
            continue
        trimmed_line = line.strip()
        return_list.append(trimmed_line)
    return return_list
