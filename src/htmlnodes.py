class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # to be overwirtten by child classes
    def to_html(self):
        raise NotImplementedError("to_html method should be overwritten by child classes of HTMLNode")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_for_html = ""
        for prop in self.props:
            props_for_html += f' {prop}="{self.props[prop]}"'
        return props_for_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes require a tag to be valid html")
        if self.children is None:
            raise ValueError("All parent nodes require at least one children node")
        children = ""
        for child in self.children:
            children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value to be valid html")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
