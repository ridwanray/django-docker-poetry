import pytest
from django.urls import reverse
from .factories import BlogFactory

pytestmark = pytest.mark.django_db


class TestBlogCRUD:
    blog_list_url = reverse('blog:blog-list')

    def test_create_blog(self, api_client):
        data = {
            "title": "Good news",
            "body": "Something good starts small",
            "published": True
            }

        response = api_client.post(self.blog_list_url, data)
        assert response.status_code == 201
        returned_json = response.json()
        assert 'id' in returned_json
        assert returned_json['title'] == data['title']
        assert returned_json['body'] == data['body']
        assert returned_json['published'] == data['published']

    def test_retrieve_blogs(self, api_client):
        BlogFactory.create_batch(5)
        response = api_client.get(self.blog_list_url)
        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_delete_blog(self, api_client):
        blog = BlogFactory()
        url = reverse("blog:blog-detail",
                      kwargs={"pk": blog.id})
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_update_blog(self, api_client):
        blog = BlogFactory(published= True)
        data = {
            "title": "New title",
            "body": "New body",
            "published": False,
        }
        url = reverse("blog:blog-detail",
                      kwargs={"pk": blog.id})

        response = api_client.patch(url, data)
        assert response.status_code == 200
        returned_json = response.json()
        assert returned_json['title'] == data['title']
        assert returned_json['body'] == data['body']
        assert returned_json['published'] == data['published']
        