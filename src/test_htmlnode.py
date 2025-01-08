import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode()
        node2 = HTMLNode(props={"href": "https://google.com"})
        node3 = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank"
        })
        print(node1.props_to_html())
        print(node2.props_to_html())
        print(node3.props_to_html())
    
    def test_eq(self):
        node1 = HTMLNode(tag= "p", 
                         value= "Hello this is a test", 
                         children= [1,2,3,4,5],
                         props={
                             "href": "https://google.com",
                             "target": "_blank"
                         })
        node2 = HTMLNode(tag= "p", 
                         value= "Hello this is a test", 
                         children= [1,2,3,4,5],
                         props={
                             "href": "https://google.com",
                             "target": "_blank"
                         })
        print(node1)
        print(node2)
        self.assertEqual(node1,node2)
        