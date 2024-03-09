class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, textnode):
        return (
                self.text == textnode.text 
                and 
                self.text_type == textnode.text_type 
                and 
                self.url == textnode.url
        )

    def repr(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

