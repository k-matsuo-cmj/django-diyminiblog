from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import BlogComment

class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['description']
        labels = {
            'description': _('コメント'),
        }
        help_texts = {
            'description': _('ブログへのコメントを入力してください'),
        }
