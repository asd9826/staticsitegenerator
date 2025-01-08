
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
        
        for key in self.props:
            prop_string = prop_string + " " + f'{key}="{self.props[key]}"'
        
        return prop_string
    
    def __eq__(self, other):
        if isinstance(other,HTMLNode):
            return (self.tag ==other.tag and self.value == other.value and self.children == other.children and self.props == other.props)
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"