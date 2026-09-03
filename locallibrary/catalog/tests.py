from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Book, Author, Genre

class BookListViewTest(TestCase):
    """Tests for BookListView with search and pagination."""
    
    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests."""
        # Create author
        author = Author.objects.create(
            first_name='Fyodor',
            last_name='Dostoevsky'
        )
        
        # Create genre
        genre = Genre.objects.create(name='Classic')
        
        # Create books
        cls.book1 = Book.objects.create(
            title='The Idiot',
            author=author,
            summary='A classic novel',
            isbn='9780374528379'
        )
        cls.book1.genre.add(genre)
        
        cls.book2 = Book.objects.create(
            title='Crime and Punishment',
            author=author,
            summary='Another classic',
            isbn='9780486415878'
        )
        cls.book2.genre.add(genre)
    
    def test_book_list_view_status_code(self):
        """Book list page returns 200."""
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
    
    def test_book_list_view_uses_correct_template(self):
        """Book list page uses correct template."""
        response = self.client.get(reverse('books'))
        self.assertTemplateUsed(response, 'catalog/book_list.html')
    
    def test_search_by_title(self):
        """Search returns matching books."""
        response = self.client.get(reverse('books'), {'q': 'Idiot'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Idiot')
        self.assertNotContains(response, 'Crime and Punishment')
    
    def test_search_empty_query_shows_all_books(self):
        """Empty query returns all books."""
        response = self.client.get(reverse('books'))
        self.assertContains(response, 'The Idiot')
        self.assertContains(response, 'Crime and Punishment')
    
    def test_search_no_results(self):
        """Search with no matches shows appropriate message."""
        response = self.client.get(reverse('books'), {'q': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no books in the library')