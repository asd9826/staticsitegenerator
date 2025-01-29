import unittest

from blocks import markdown_to_blocks, block_to_block_type

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
  

if __name__ == "__main__":
    unittest.main()