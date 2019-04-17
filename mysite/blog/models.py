from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    """自定义model的manager"""

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布'),
    )
    title = models.CharField(max_length=250, verbose_name="标题")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Many-to-one,a user can write any number of posts.Each post is written by a user.
    # Using CASCADE, we specify that when the referenced user is deleted,
    # the database will also delete its related blog posts.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="作者")
    body = models.TextField(verbose_name='正文')
    publish = models.DateTimeField(default=timezone.now, verbose_name="发布日期")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新日期")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="状态")

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        # Post 按发布日期降序排序
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        You can use the post_detail URL that you have defined in the
        preceding section to build the canonical URL for Post objects. The
        convention in Django is to add a get_absolute_url() method to the
        model that returns the canonical URL of the object. For this
        method, we will use the reverse() method that allows you to build
        URLs by their name and passing optional parameters. Edit your
        models.py file and add the following(您可以使用在上一节中定义的post_detail URL来构建Post对象的规范URL。Django中的约定是
        将get_absolute_url（）方法添加到返回对象的规范URL的模型。 对于此方法，我们将使用reverse（）方法，该方法允许您按名称构建URL并传递
        可选参数。编辑models.py文件并添加以下内容)
        :return:
        """
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
