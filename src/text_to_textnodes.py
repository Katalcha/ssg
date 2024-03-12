from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image
from split_nodes_delimiter import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
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
