# manage命令
manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
# 开发应用步骤
## 创建项目
manage startapp blog
1. 设计model
2. 激活APP
    在settings文件中，INSTALLED_APPS中添加app
3. 创建和应用数据库迁移
   manage.py makemigrations
   manage.py migrate
   
4. 添加model到管理站点（Adding your models to the administration site）
    编辑app 的admin.py，添加如下内容：
    admin.site.register(Post)
    
5. 检索记录
    model manager 方法
    objects对象是每个model检索在数据库中所有记录的默认manager
   get:检索单条记录: post = Post.objects.get(id=123)
   all:检索多条记录： posts = Post.objects.all(),这里objects是 model manager
   filter:
    检索发布日期为2018年的文章: Post.objects.filter(publish__year=2017)
    检索某人、2017年发布的文章：Post.objects.filter(publish__year=2017,author__username='admin')
   exclude:从结果集中排除一些结果
    Post.objects.filter(publish__year=2017).exclude(title__startswith='why')
   order_by:指定结果集的排序方法，如果是降序的话，在排序字段前加上符号-：
   Posts.objects.order_by('-title')
   自定义manager
 6. 创建list和detail 视图
    在app的views文件中，创建视图
 7. 为视图添加url(映射url到view function)
       
    7.1 在app目录下创建urls.py文件
    Creating a urls.py file for each app is the best way to make your applications
reusable by other projects.

    7.2 在项目中的urls.py中包含app的url：
    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls', namespace='blog'))
    ]
    ```
    规范模型的URL：为model添加get_absolute_url()方法，会在Template中使用
8. 创建Template for view
   
   Tempalte 目录结构如下：
   ```
   app目录/
        templates/
            blog/
                base.html
                post/
                    list.html
                    detail.html
   ```
9. 创建css静态文件

   目录:
   ```app/static/css/blog.css```    
   
10. 添加分页功能    