from extract_markdown_links import extract_markdown_links
from textnode import (
    TextNode,
    text_type_text,
    text_type_link
)

def split_nodes_link(old_nodes):
    return_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            return_nodes.append(old_node)
            continue
        old_node_text = old_node.text
        links = extract_markdown_links(old_node_text)
        if len(links) == 0:
            return_nodes.append(old_node)
            continue
        for link in links:
            sections = old_node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                return_nodes.append(TextNode(sections[0], text_type_text))
            return_nodes.append(TextNode(link[0], text_type_link, link[1]))
            old_node_text = sections[1]
        if old_node_text != "":
            return_nodes.append(TextNode(old_node_text, text_type_text))
    return return_nodes
