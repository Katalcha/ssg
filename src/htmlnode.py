class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # to be overwritten by child classes
    def to_html(self):
        raise NotImplementedError("to_html method should be overwritten by child classes")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_for_html = ""
        for prop in self.props:
            props_for_html += f' {prop}="{self.props[prop]}"'
        return props_for_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
