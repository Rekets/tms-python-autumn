from django.test import TestCase, Client

from home.models import Articles


class ArticleTestCase(TestCase):
    """
    Интеграционный тест
    Тест на проверку создания артикля
    """

    def setUp(self) -> None:
        self.articles = Articles.objects.create(
            title="Test title",
            content='test content'
        )
        self.client = Client()

    def test_create_articles(self):
        self.assertEqual(Articles.objects.count(), 1)

    def test_article_get_article(self):
        self.assertEqual(
            str(self.articles),
            'Test title - test content'
        )

    def test_api_get_articles(self):
        """
        Тест на проверку api
        """
        response_json = self.client.get('/api/articles/').json()
        self.assertEqual(response_json['count'], 2)
        self.assertEqual(
            response_json['results'][0],
            {
                "title": "Test title",
                "id": 2,
                "content": "test content",
                "author": None,
                "link": 'http//localhost:8080/api/articles/2/'
            },
        )
