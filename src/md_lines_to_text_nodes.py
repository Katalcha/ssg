import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def text_to_textnodes(text):
    md_bolded = "**"
    md_italic = "*"
    md_code = "`"
    
    # ( ͡° ͜ʖ ͡°)
    return (
        split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            [TextNode(text, text_type_text)], 
                            md_bolded, 
                            text_type_bold
                        ), 
                        md_italic, 
                        text_type_italic
                    ), 
                    md_code, 
                    text_type_code
                )
            )
        )
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

def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    matched_regex = re.findall(regex, text)
    return matched_regex

def extract_markdown_links(text):
    regex = r"\[(.*?)\]\((.*?)\)"
    matched_regex = re.findall(regex, text)
    return matched_regex
