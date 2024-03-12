from extract_markdown_images import extract_markdown_images
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
)

def split_nodes_image(old_nodes):
    return_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            return_nodes.append(old_node)
            continue
        old_node_text = old_node.text
        images = extract_markdown_images(old_node_text)
        if len(images) == 0:
            return_nodes.append(old_node)
            continue
        for image in images:
            sections = old_node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                return_nodes.append(TextNode(sections[0], text_type_text))
            return_nodes.append(TextNode(image[0], text_type_image, image[1]))
            old_node_text = sections[1]
        if old_node_text != "":
            return_nodes.append(TextNode(old_node_text, text_type_text))
    return return_nodes
