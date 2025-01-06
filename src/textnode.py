from enum import Enum

class TextType(Enum):
    Normal = "Normal"
    Bold = "Bold"
    Italic = "Italic"
    Code = "Code"
    Links = "Links"
    Images = 'Images'
    
#Define TextNode Class

class TextNode():

    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if isinstance(other,TextNode):
            return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

        return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
