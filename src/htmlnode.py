
class HTMLNode():
    
    def __init__(self, tag = None, value = None, children= None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    
    def props_to_html(self):
        prop_string = ""
        if self.props is None:
            return ""
        
        for prop in self.props:
            prop_string += f' {prop}="{self.props[prop]}"'
        
        return prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"