from casepro.test import BaseCasesTest
from django.core.urlresolvers import reverse
from django.test import Client
from django_comments.models import Comment
from django_comments.forms import CommentForm


class CommentTest(BaseCasesTest):
    def setUp(self):
        super(CommentTest, self).setUp()
        self.client = Client()
        self.ann = self.create_contact(self.unicef, 'C-001', "Ann",
                                       fields={'age': "34"},
                                       groups=[self.females, self.reporters, self.registered])
        self.login(self.user1)

    def test_post_comment(self):
        data = CommentForm(self.user1, {}).generate_security_data()
        data.update({
            'name': 'the supplied name',
            'comment': 'Foo',
        })
        response = self.url_post(
            'unicef',
            reverse('comments-post-comment'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.all().count(), 1)
        self.assertEqual(Comment.objects.all().first().comment, 'Foo')

    def test_view_comments(self):
        data = CommentForm(self.user1, {}).generate_security_data()
        data.update({
            'name': 'the supplied name',
            'comment': 'Foo',
        })
        self.url_post(
            'unicef',
            reverse('comments-post-comment'), data)
        data = CommentForm(self.user1, {}).generate_security_data()
        data.update({
            'name': 'the supplied name',
            'comment': 'Foo2',
        })
        self.url_post(
            'unicef',
            reverse('comments-post-comment'), data)
        url = reverse('msg_board.comment_list')
        self.login(self.admin)
        response = self.url_get('unicef', url)

        print response
        self.assertContains(response, 'Foo2')