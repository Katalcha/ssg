from textnode import (
    TextNode,
    text_type_text
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            return_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        return_nodes.extend(split_nodes)
    return return_nodes
