from htmlnodes import ParentNode
from md_lines_to_text_nodes import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

div_tag = "div"

def markdown_to_blocks(full_md_doc):
    return_list = []
    for line in full_md_doc.split("\n\n"):
        if line == "":
            continue
        trimmed_line = line.strip()
        return_list.append(trimmed_line)
    return return_list

def markdown_to_html_node(full_md_doc):
    blocks = markdown_to_blocks(full_md_doc)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode(div_tag, children, None)

def block_to_html_node(md_block):
    block_type = block_to_block_type(md_block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(md_block)
    if block_type == block_type_heading:
        return heading_to_html_node(md_block)
    if block_type == block_type_code:
        return code_to_html_node(md_block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(md_block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(md_block)
    if block_type == block_type_quote:
        return quote_to_html_node(md_block)
    raise ValueError("invalid block type")

def block_to_block_type(markdown_block):
    splitted = markdown_block.split("\n")
    if (
        markdown_block.startswith("# ")
        or markdown_block.startswith("## ")
        or markdown_block.startswith("### ")
        or markdown_block.startswith("#### ")
        or markdown_block.startswith("##### ")
        or markdown_block.startswith("###### ")
    ):
        return block_type_heading
    if (
        len(splitted) > 1 
        and splitted[0].startswith("```")
        and splitted[-1].startswith("```")
    ): 
        return block_type_code
    if (markdown_block.startswith(">")):
        for line in splitted:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if (markdown_block.startswith("* ")):
        for line in splitted:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if (markdown_block.startswith("- ")):
        for line in splitted:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if (markdown_block.startswith("1. ")):
        i = 1
        for line in splitted:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(md_block):
    p = "p"
    splitted = md_block.split("\n")
    paragraph = " ".join(splitted)
    children = text_to_children(paragraph)
    return ParentNode(p, children)

def heading_to_html_node(md_block):
    level = 0
    for char in md_block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(md_block):
        raise ValueError(f"Invalid heading level: {level}")
    text = md_block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(md_block):
    tag = "code"
    if not md_block.startswith("```") or not md_block.endswith("```"):
        raise ValueError("Invalid code block")
    text = md_block[4:-3]
    children = text_to_children(text)
    code = ParentNode(tag, children)
    return ParentNode("pre", [code])

def ordered_list_to_html_node(md_block):
    ol = "ol"
    li = "li"
    items = md_block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode(li, children))
    return ParentNode(ol, html_items)

def unordered_list_to_html_node(md_block):
    ul = "ul"
    li = "li"
    items = md_block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(li, children))
    return ParentNode(ul, html_items)

def quote_to_html_node(md_block):
    bq = "blockquote"
    splitted_block = md_block.split("\n")
    lines = []
    for element in splitted_block:
        if not element.startswith(">"):
            raise ValueError("Invalid quote block")
        lines.append(element.lstrip(">").strip())
    content = " ".join(lines)
    children = text_to_children(content)
    return ParentNode(bq, children)
