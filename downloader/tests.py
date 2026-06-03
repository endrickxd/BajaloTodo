from django.test import TestCase, Client
from django.urls import reverse
from .utils import format_duration, format_size

class DownloaderUtilsTests(TestCase):
    def test_format_duration(self):
        self.assertEqual(format_duration(None), "Desconocido")
        self.assertEqual(format_duration(45), "0:45")
        self.assertEqual(format_duration(125), "2:05")
        self.assertEqual(format_duration(3665), "1:01:05")

    def test_format_size(self):
        self.assertEqual(format_size(None), "Desconocido")
        self.assertEqual(format_size(500), "500.0 B")
        self.assertEqual(format_size(1024), "1.0 KB")
        self.assertEqual(format_size(1048576), "1.0 MB")

class DownloaderViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('downloader:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'downloader/index.html')

    def test_analyze_video_invalid_method(self):
        response = self.client.get(reverse('downloader:analyze_video'))
        self.assertEqual(response.status_code, 405) # Method Not Allowed

    def test_analyze_video_empty_url(self):
        response = self.client.post(reverse('downloader:analyze_video'), {'url': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn('status', response.json())
        self.assertEqual(response.json()['status'], 'error')

    def test_download_file_missing_url(self):
        response = self.client.get(reverse('downloader:download_file'))
        self.assertEqual(response.status_code, 400)

