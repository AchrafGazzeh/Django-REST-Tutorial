from django.test import TestCase
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from .models import Snippet

class SnippetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.snippet = Snippet.objects.create(
            title='Test Snippet',
            code='print("Hello, world!")',
            linenos=True,
            language='python',
            style='friendly',
            owner=self.user
        )
    
    def test_snippet_model_save_method(self):
        expected_highlighted = highlight(
            self.snippet.code,
            get_lexer_by_name(self.snippet.language),
            HtmlFormatter(style=self.snippet.style, linenos='table', full=True, title=self.snippet.title)
        )
        self.assertEqual(self.snippet.highlighted, expected_highlighted)
    
    def test_snippet_model_fields(self):
        self.assertEqual(self.snippet.title, 'Test Snippet')
        self.assertEqual(self.snippet.code, 'print("Hello, world!")')
        self.assertEqual(self.snippet.linenos, True)
        self.assertEqual(self.snippet.language, 'python')
        self.assertEqual(self.snippet.style, 'friendly')
        self.assertEqual(self.snippet.owner, self.user)