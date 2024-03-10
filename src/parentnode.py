from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes require a tag")
        if self.children is None:
            raise ValueError("All parent nodes require at least one children node")
        childrens = ""
        for child in self.children:
            childrens += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childrens}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
