import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from parameterized import parameterized
from icon_markdown.util.sanitizer import sanitize_html


class TestSanitizer(TestCase):
    """Test cases for allowlist-based HTML sanitization."""

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
            # Test event handler encoding - onclick
            (
                "<p onclick=\"alert('xss')\">Click me</p>",
                "&lt;p onclick=\"alert('xss')\"&gt;Click me&lt;/p&gt;",
            ),
            # Test event handler encoding - onerror (img with disallowed attribute)
            (
                '<img src="x" onerror="alert(\'xss\')">',
                '&lt;img onerror="alert(\'xss\')" src="x"/&gt;',
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
            # Test that images with relative URLs are preserved
            (
                '<img src="image.png" alt="Description">',
                '<img alt="Description" src="image.png"/>',
            ),
            # Test that images with data: URI are preserved (inline base64)
            (
                '<img src="data:image/png;base64,iVBOR"/>',
                '<img src="data:image/png;base64,iVBOR"/>',
            ),
            # SSRF regression: img with external http URL is encoded
            (
                '<p><img src="http://attacker.com/beacon.png"/></p>',
                '<p>&lt;img src="http://attacker.com/beacon.png"/&gt;</p>',
            ),
            # SSRF regression: img targeting cloud metadata endpoint is encoded
            (
                '<img src="http://169.254.169.254/latest/meta-data/">',
                '&lt;img src="http://169.254.169.254/latest/meta-data/"/&gt;',
            ),
            # LFI regression: file:// scheme is encoded
            (
                '<img src="file:///etc/passwd"/>',
                '&lt;img src="file:///etc/passwd"/&gt;',
            ),
            # XSS regression: javascript: scheme is encoded
            (
                '<img src="javascript:alert(1)"/>',
                '&lt;img src="javascript:alert(1)"/&gt;',
            ),
            # SSRF regression: srcset with an embedded external URL is encoded
            # (srcset is not an allowed attribute, so the tag is encoded regardless of parsing)
            (
                '<img srcset="a.png, http://evil/x">',
                '&lt;img srcset="a.png, http://evil/x"/&gt;',
            ),
            # SSRF regression: protocol-relative resource URL is encoded
            (
                '<img src="//evil.com/beacon.png">',
                '&lt;img src="//evil.com/beacon.png"/&gt;',
            ),
            # mailto: link is preserved
            (
                '<a href="mailto:user@example.com">contact</a>',
                '<a href="mailto:user@example.com">contact</a>',
            ),
            # Fragment link (footnote reference) is preserved
            (
                '<a href="#fn1">note</a>',
                '<a href="#fn1">note</a>',
            ),
            # javascript: hyperlink is encoded
            (
                '<a href="javascript:alert(1)">x</a>',
                '&lt;a href="javascript:alert(1)"&gt;x&lt;/a&gt;',
            ),
            # SSRF regression: inline style with url() is encoded
            (
                '<div style="background:url(http://attacker/)">x</div>',
                '&lt;div style="background:url(http://attacker/)"&gt;x&lt;/div&gt;',
            ),
            # SSRF regression: video with external src is encoded (video is not allowed)
            (
                '<video src="http://internal/"></video>',
                '&lt;video src="http://internal/"&gt;&lt;/video&gt;',
            ),
            # SSRF regression: meta refresh redirect is encoded
            (
                '<meta http-equiv="refresh" content="0;url=http://internal/">',
                '&lt;meta content="0;url=http://internal/" http-equiv="refresh"/&gt;',
            ),
            # Unknown/custom tags are encoded (allowlist default-deny)
            (
                "<custom-tag>z</custom-tag>",
                "&lt;custom-tag&gt;z&lt;/custom-tag&gt;",
            ),
            # Task-list checkbox is preserved (regression: must render, not be encoded)
            (
                '<input type="checkbox" checked="">',
                '<input checked="" type="checkbox"/>',
            ),
            # Table column alignment via style is preserved
            (
                '<th style="text-align: center;">C</th>',
                '<th style="text-align: center;">C</th>',
            ),
            # A style value that smuggles url() alongside a safe declaration is encoded
            (
                '<th style="text-align:left;background:url(http://e)">C</th>',
                '&lt;th style="text-align:left;background:url(http://e)"&gt;C&lt;/th&gt;',
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
        """Test that disallowed HTML elements and attributes are properly encoded."""
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

    def test_form_elements_denied(self):
        """Test that form elements are encoded (SSRF vector via action=)."""
        html = '<form action="http://attacker/steal"><button>Submit</button></form>'
        result = sanitize_html(html)
        self.assertNotIn("<form", result)
        self.assertIn("&lt;form", result)
        self.assertIn("&lt;/form&gt;", result)

    def test_image_with_disallowed_scheme_is_encoded(self):
        """Regression test for SSRF via img src with attacker-controlled URL."""
        html = '<p>Report</p><img src="http://169.254.169.254/latest/meta-data/">'
        result = sanitize_html(html)
        self.assertNotIn('<img src="http://169.254', result)
        self.assertIn("&lt;img", result)
        self.assertIn("<p>Report</p>", result)

    def test_image_with_data_uri_is_preserved(self):
        """Inline base64 images (data: URI) remain functional after the SSRF fix."""
        html = '<img src="data:image/png;base64,iVBORw0KGgoAAAA" alt="inline">'
        result = sanitize_html(html)
        self.assertIn("data:image/png;base64", result)
        self.assertNotIn("&lt;img", result)

    def test_style_attribute_url_is_encoded(self):
        """Inline style attribute carrying url() is encoded to prevent CSS-based SSRF."""
        html = '<div style="background:url(http://attacker/beacon)">x</div>'
        result = sanitize_html(html)
        self.assertIn("&lt;div", result)
        self.assertIn("style", result)

    def test_entity_escaped_tag_is_not_resurrected(self):
        """Regression for the formatter=None resurrection SSRF.

        Text that merely *looks* like a tag (entity-escaped, e.g. from a Markdown code span) must
        stay escaped on output and never be turned back into a live element.
        """
        html = '<p>&lt;img src="http://evil/x"&gt;</p>'
        result = sanitize_html(html)
        # The <img> must remain inert text, not a live tag, and must not be double-escaped.
        self.assertNotIn('<img src="http://evil/x"', result)
        self.assertIn('&lt;img src="http://evil/x"', result)
        self.assertNotIn("&amp;lt;", result)

    def test_entity_escaped_style_import_is_not_resurrected(self):
        """A CSS @import smuggled as entity-escaped text must not become a live <style>."""
        html = "<p>&lt;style&gt;@import url(http://evil/x.css);&lt;/style&gt;</p>"
        result = sanitize_html(html)
        self.assertNotIn("<style>", result)
        self.assertIn("&lt;style&gt;", result)
        self.assertNotIn("&amp;lt;", result)

    def test_task_list_checkbox_is_preserved(self):
        """Regression: task-list checkboxes must render (were encoded by the 4.0.2 denylist)."""
        html = '<ul class="task-list"><li><label><input type="checkbox" checked="" />done</label></li></ul>'
        result = sanitize_html(html)
        self.assertIn("<input", result)
        self.assertNotIn("&lt;input", result)

    def test_table_alignment_style_is_preserved(self):
        """Regression: table column alignment via style must render (was encoded by 4.0.2)."""
        html = '<th style="text-align: right;">R</th>'
        result = sanitize_html(html)
        self.assertIn('<th style="text-align: right;">', result)
        self.assertNotIn("&lt;th", result)

    def test_nested_disallowed_tags_not_double_escaped(self):
        """A disallowed tag containing another disallowed tag is escaped exactly once."""
        html = '<svg><use xlink:href="http://evil"/></svg>'
        result = sanitize_html(html)
        self.assertNotIn("&amp;lt;", result)
        self.assertIn("&lt;svg&gt;", result)
        self.assertIn("&lt;use", result)
