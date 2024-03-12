from markdown_to_blocks import markdown_to_blocks

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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
