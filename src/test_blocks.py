import unittest

from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):

    def test_mark_down_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,["This is **bolded** paragraph", 
                                 "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                                 "* This is a list\n* with items"])
        
    def test_mark_down_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,["This is **bolded** paragraph", 
                                 "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                                 "* This is a list\n* with items"])
    def test_headings(self):
        # Valid headings
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("### Subheading"), "heading")
        self.assertEqual(block_to_block_type("###### Smallest heading"), "heading")

        # Invalid heading (too many # symbols)
        self.assertEqual(block_to_block_type("####### Not a heading"), "paragraph")

    def test_code_blocks(self):
        # Valid code block
        self.assertEqual(block_to_block_type("```\nCode block\n```"), "code")

        # Invalid code block (missing closing backticks)
        self.assertEqual(block_to_block_type("```\nNot a code block"), "paragraph")

        # Invalid code block (no starting backticks)
        self.assertEqual(block_to_block_type("Not a code block\n```"), "paragraph")

    def test_quotes(self):
        # Valid quotes
        self.assertEqual(block_to_block_type("> This is a quote."), "quote")
        self.assertEqual(
            block_to_block_type("> Proper quote\n> Still quoted."), "quote"
        )

        # Invalid quotes (mixed with non-quote lines)
        self.assertEqual(block_to_block_type("> Quote\nNot quoted anymore."), "paragraph")
        self.assertEqual(
            block_to_block_type("> Quote\n\nNo quote here.\n> Back to quote."),
            "paragraph",
        )

    def test_unordered_lists(self):
        # Valid unordered lists
        self.assertEqual(
            block_to_block_type("* Item 1\n* Item 2\n- Item 3"), "unordered_list"
        )
        self.assertEqual(block_to_block_type("- Item 1"), "unordered_list")

        # Invalid unordered list (non-list line included)
        self.assertEqual(
            block_to_block_type("* Item 1\nInvalid Line\n* Item 2"), "paragraph"
        )
    def test_ordered_lists(self):
        # Valid ordered lists
        self.assertEqual(
            block_to_block_type("1. First\n2. Second\n3. Third"), "ordered_list"
        )
        #Invalid ordered lists
        # Numbers are skipped
        self.assertEqual(block_to_block_type("1. First\n3. Second"), "paragraph")
        # Numbers don’t start at 1
        self.assertEqual(block_to_block_type("2. First\n3. Second"), "paragraph")
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
    
    def test_blockquote(self):
        md = """
> This is a
> quote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a\nquote block</blockquote><p>this is paragraph text</p></div>",
        )
  

if __name__ == "__main__":
    unittest.main()