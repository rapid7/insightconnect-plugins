import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from parameterized import parameterized
from icon_markdown.util.sanitizer import sanitize_html


class TestSanitizer(TestCase):
    """Test cases for HTML sanitization functionality."""

    @parameterized.expand(
        [
            # Test script tag encoding
            (
                '<p>Hello</p><script>alert("xss")</script><p>World</p>',
                '<p>Hello</p>&lt;script&gt;alert("xss")&lt;/script&gt;<p>World</p>',
            ),
            # Test iframe encoding
            (
                '<p>Content</p><iframe src="http://evil.com"></iframe>',
                '<p>Content</p>&lt;iframe src="http://evil.com"&gt;&lt;/iframe&gt;',
            ),
            # Test object tag encoding
            (
                '<p>Safe</p><object data="malicious.swf"></object>',
                '<p>Safe</p>&lt;object data="malicious.swf"&gt;&lt;/object&gt;',
            ),
            # Test embed tag encoding
            (
                '<p>Text</p><embed src="flash.swf">',
                '<p>Text</p>&lt;embed src="flash.swf"/&gt;',
            ),
            # Test link tag encoding
            (
                '<link rel="stylesheet" href="evil.css"><p>Content</p>',
                '&lt;link href="evil.css" rel="stylesheet"/&gt;<p>Content</p>',
            ),
            # Test style tag encoding
            (
                '<style>body{background:url("javascript:alert(1)")}</style><p>Text</p>',
                '&lt;style&gt;body{background:url("javascript:alert(1)")}&lt;/style&gt;<p>Text</p>',
            ),
            # Test event handler encoding - onclick (not in deny list, so preserved)
            (
                "<p onclick=\"alert('xss')\">Click me</p>",
                "<p onclick=\"alert('xss')\">Click me</p>",
            ),
            # Test event handler encoding - onerror
            (
                '<img src="x" onerror="alert(\'xss\')">',
                '&lt;img onerror="alert(\'xss\')" src="x"/&gt;',
            ),
            # Test event handler encoding - onload
            (
                '<img src="img.png" onload="malicious()">',
                '&lt;img onload="malicious()" src="img.png"/&gt;',
            ),
            # Test that safe tags are preserved
            (
                "<h1>Title</h1><p>Paragraph with <strong>bold</strong> and <em>italic</em></p>",
                "<h1>Title</h1><p>Paragraph with <strong>bold</strong> and <em>italic</em></p>",
            ),
            # Test that safe attributes are preserved
            (
                '<a href="https://example.com" title="Example">Link</a>',
                '<a href="https://example.com" title="Example">Link</a>',
            ),
            # Test that images are preserved with safe attributes
            (
                '<img src="image.png" alt="Description">',
                '<img alt="Description" src="image.png"/>',
            ),
            # Test table tags are preserved
            (
                "<table><tr><td>Cell</td></tr></table>",
                "<table><tr><td>Cell</td></tr></table>",
            ),
            # Test list tags are preserved
            (
                "<ul><li>Item 1</li><li>Item 2</li></ul>",
                "<ul><li>Item 1</li><li>Item 2</li></ul>",
            ),
            # Test empty input
            (
                "",
                "",
            ),
        ]
    )
    def test_sanitize_html(self, input_html, expected_output):
        """Test that dangerous HTML elements and attributes are properly sanitized."""
        result = sanitize_html(input_html)
        self.assertEqual(result, expected_output)

    def test_sanitize_html_encodes_script_tags(self):
        """Test that sanitize_html properly encodes script tags."""
        malicious_html = '<p>Safe</p><script>alert("xss")</script>'
        result = sanitize_html(malicious_html)
        self.assertNotIn("<script>", result)
        self.assertIn("&lt;script&gt;", result)
        self.assertIn("<p>Safe</p>", result)

    def test_sanitize_html_preserves_markdown_elements(self):
        """Test that common markdown-to-HTML elements are preserved."""
        markdown_html = """
        <h1>Heading 1</h1>
        <h2>Heading 2</h2>
        <p>Paragraph with <strong>bold</strong>, <em>italic</em>, and <code>code</code>.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
        <ol>
            <li>First</li>
            <li>Second</li>
        </ol>
        <blockquote>Quote</blockquote>
        <pre><code>code block</code></pre>
        <a href="https://example.com">Link</a>
        <img src="image.png" alt="Image">
        """
        result = sanitize_html(markdown_html)
        # Verify key elements are preserved
        self.assertIn("<h1>", result)
        self.assertIn("<h2>", result)
        self.assertIn("<p>", result)
        self.assertIn("<strong>", result)
        self.assertIn("<em>", result)
        self.assertIn("<code>", result)
        self.assertIn("<ul>", result)
        self.assertIn("<ol>", result)
        self.assertIn("<li>", result)
        self.assertIn("<blockquote>", result)
        self.assertIn("<pre>", result)
        self.assertIn("<a ", result)
        self.assertIn("<img ", result)

    def test_multiple_event_handlers_encoded(self):
        """Test that tags with multiple event handlers are encoded."""
        html = '<div onclick="a()" onmouseover="b()" onload="c()">Content</div>'
        result = sanitize_html(html)
        self.assertIn("&lt;div", result)
        self.assertIn("onclick", result)
        self.assertIn("onmouseover", result)
        self.assertIn("onload", result)
        self.assertIn("Content", result)

    def test_form_elements_preserved(self):
        """Test that form elements are preserved (not in denylist)."""
        html = '<form action="/submit"><input type="text" name="field"><button>Submit</button></form>'
        result = sanitize_html(html)
        self.assertIn("<form", result)
        self.assertIn("<input", result)
        self.assertIn("<button>", result)
