[数据库官方文档链接](
http://docs.mongoengine.org/tutorial.html)

## 一、链接数据库
```
pip  install mongoengine
from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/my_db")
connect(host="mongodb://my_user:my_password@127.0.0.1:27017/my_db")


connect(
    db='test',
    username='user',
    password='12345',
    host='mongodb://admin:qwerty@localhost/production')
    
```
## 二、断开链接
该功能可用于断开特定链接。
```
from mongoengine import connect, disconnectconnect('a_db', alias='db1')

class User(Document):
    name = StringField()
    meta = {'db_alias': 'db1'}

disconnect(alias='db1')

connect('another_db', alias='db1')
```

## 三、定义文档
```
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    meta = {'db_alias': 'user-db-alias'}
 
from mongoengine import *
import datetime

class Page(Document):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
```

若根据以后的需求增加不同的字段内容，可使用以下继承的方式：
* allow_inheritance:默认值为true，如果有多态模型可以集成并把allow_inheritance打开
* 单个文档可以通过在元数据中提供db_alias来链接到不同的数据库
* collection，可以更改数据集合的名称。

```
connect(alias='user-db-alias', db='user-db')
connect(alias='book-db-alias', db='book-db')
connect(alias='users-books-db-alias', db='users-books-db')

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)

    meta = {'allow_inheritance': True，'collection':'cmsPost'}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
```
## 四、动态文档保存
动态文档的工作方式与文档相同，但设置给他们的任何数据/属性也将保存
```
from mongoengine import *

class Page(DynamicDocument):
    title = StringField(max_length=200, required=True)

# Create a new page and add tags

>>> page = Page(title='Using MongoEngine')

>>> page.tags = ['mongodb', 'mongoengine']

>>> page.save()

>>> Page.objects(tags='mongoengine').count()>>> 1

```

### 4.1标签
如果要使用标签，将标签作为单独的字段，存储到数据库中
```
class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
```
### 4.2评论
MongoDB能够在其他文档中嵌入文档。可以为这些嵌入式文档定义概要，就像他们可能用于常规文档一样。要创建嵌入文档，只需像往常一样定义一个文档，继承
EmbeddedDocument而不是Document。
要将文档嵌入到另一个文档中，请使用EmbeddedDocumentField字段类型，将嵌入的文档作为第一个参数提供。

```
class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)
  # 我们可以在帖子文档中存储评论文档列表
class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
```
### 4.3处理引用删除
```
class ProfilePage(Document):
    ...
    employee = ReferenceField('Employee', reverse_delete_rule=mongoengine.CASCADE)
    #这个例子中的声明意味着当一个Employee对象被移除时，ProfilePage引用该雇员的那个也被移除。如果删除了整批员工，则所有链接的配置文件页面也会被删除
```

## 五、存储数据
```
ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
```
或者
```
ross = User(email='ross@example.com')ross.first_name = 'Ross'ross.last_name = 'Lawley'ross.save()
```

## 六、访问数据
```
for post in Post.objects:
    print(post.title)
```
### 6.1检索特定类型信息
```
for post in Post.objects:
    print(post.title)
    print('=' * len(post.title))

    if isinstance(post, TextPost):
        print(post.content)

    if isinstance(post, LinkPost):
        print('Link: {}'.format(post.link_url))
```

## 七、filed参数
* required（默认：false）
  如果设置为True，并且该字段未设置在文档实例上，则在文档验证时将提出验证。
* default（默认：None）
默认参数的规则需要特别小心谨慎（如ListField或DictField）
```
class ExampleFirst(Document):
    # Default an empty list
    values = ListField(IntField(), default=list)

class ExampleSecond(Document):
    # Default a set of values
    values = ListField(IntField(), default=lambda: [1,2,3])

class ExampleDangerous(Document):
    # This can make an .append call to  add values to the default (and all the following objects),
    # instead to just an object
    values = ListField(IntField(), default=[1,2,3])
```
* unique（默认：False）
当True时，给Field构造函数来指定一个字段在集合中是唯一的，如果尝试将与唯一字段具有相同值的文档保存为数据库的文档，NotUniqueError则会引发。
* unique_with（默认：无）
与此字段一起使用的字段名称，将不会具有相同值的集合中的两个文档。unique_with可以是单个字段名称，也可以是字段名称的列表或元组。
* primary_key （默认：False）
如果为True，则使用此字段作为集合的主键。 DictField 和EmbeddedDocuments都支持作为文档的主键。
如果设置，该字段也可通过PK字段访问
* choices （默认：无）
一个可迭代的（例如列表，元组或集合）选项，这个字段的值应该被限制到这个选项。
  
```
SIZE = (('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'))


class Shirt(Document):
    size = StringField(max_length=3, choices=SIZE)
    
SIZE = ('S', 'M', 'L', 'XL', 'XXL')

class Shirt(Document):
    size = StringField(max_length=3, choices=SIZE)
    
class User(Document):
    username = StringField(unique=True)
    first_name = StringField()
    last_name = StringField(unique_with='first_name')

```

* validation（可选）
验证字段，以值为参数调用，如果验证失败，应提高验证。例如：
  
```
def _not_empty(val):
    if not val:
        raise ValidationError('value can not be empty')

class Person(Document):
    name = StringField(validation=_not_empty)

```
  也可以通过设置validate=False，调用save()方法时跳过整个文档验证过程。
  
```
class Recipient(Document):
    name = StringField()
    email = EmailField()

recipient = Recipient(name='admin', email='root@localhost')
recipient.save()               # 会产生一个 ValidationError 错误
recipient.save(validate=False) # 不会

```


## 八、列表字段
ListField将另一个字段对象作为其第一个参数，其中指定了列表中可能存储哪些类型的元素。
```
class Page(Document):
    tags = ListField(StringField(max_length=50))

```

## 九、参考字段
参考字段可以使用ReferenceField存储到数据库中的其他文档。将另一个文档作为第一个参数传递给构造器，然后简单地将文档对象分配给字段：
```
class User(Document):
    name = StringField()

class Page(Document):
    content = StringField()
    author = ReferenceField(User)

john = User(name="John Smith")john.save()

post = Page(content="Test Page")post.author = johnpost.save()

```
## 十、一对多与ListField
如果通过引用列表实现一对多关系，则引用将存储为DBRefs，并且需要将对象的实例传递给查询
```
class User(Document):
    name = StringField()

class Page(Document):
    content = StringField()
    authors = ListField(ReferenceField(User))

bob = User(name="Bob Jones").save()
john = User(name="John Smith").save()

Page(content="Test Page", authors=[bob, john]).save()
Page(content="Another Page", authors=[john]).save()

# 查找所有由bob编写的网页，此处用到了高级查询，后面会介绍
Page.objects(authors__in=[bob])

# 查找所有由bob和john编写的网页
Page.objects(authors__all=[bob, john])

# 删除由bob编写的某篇文章（根据某个id查找到的）.
Page.objects(id='...').update_one(pull__authors=bob)

# 把john添加到某篇文章（根据某个id查找到的）.
Page.objects(id='...').update_one(push__authors=john)

```
## 十一、处理引用文档的删除
默认情况下，MongoDB不检查数据的完整性，因此删除其他文档仍然存在引用的文档将导致一致性问题。MongoEngine的ReferenceField增加了一些功能来防范这些类型的数据库完整性问题，为每个引用提供删除规则规范。通过reverse_delete_rule在ReferenceField定义上提供属性来指定删除规则，如下所示：
```
class ProfilePage(Document):
    ...
    employee = ReferenceField('Employee', reverse_delete_rule=mongoengine.CASCADE)
    #这个例子中的声明意味着当一个Employee对象被移除时，ProfilePage引用该雇员的那个也被移除。如果删除了整批员工，则所有链接的配置文件页面也会被删除

```
* mongoengine.DO_NOTHING
这是默认设置，不会执行任何操作。删除速度很快，但可能会导致数据库不一致或悬空引用。

* mongoengine.DENY
如果仍存在对被删除对象的引用，则拒绝删除。

* mongoengine.NULLIFY
删除任何仍然指向被删除对象的对象字段（使用MongoDB的“未设置”操作），从而有效地消除关系。
即删除了被引用的字段，对引用它的字段无影响，举个例子，假如，文章的作者字段采用的是引用字段，那么作者一旦被删除，那么，由他写的文章仅仅是没有了作者，他的文章都还在。

* mongoengine.CASCADE
引用字段被删除，则引用此字段的文档也会被删除，
举个例子，假如，文章的作者字段采用的是引用字段，那么作者一旦被删除，那么，由他写的文章也都被删除。

* mongoengine.PULL
从ListField（ReferenceField）的任何对象的字段中删除对该对象的引用（使用MongoDB的“拉”操作 ）。

## 十二、通用参考字段
第二种场景也存在，GenericReferenceField。这允许引用任何类型的Document，因此不会将Document子类作为构造函数参数:
```
class Link(Document):
    url = StringField()

class Post(Document):
    title = StringField()

class Bookmark(Document):
    bookmark_object = GenericReferenceField()

link = Link(url='http://hmarr.com/mongoengine/')
link.save()

post = Post(title='Using MongoEngine')
post.save()

Bookmark(bookmark_object=link).save()
Bookmark(bookmark_object=post).save()
Note

```
## 十三、索引
可以在集合上指定索引以加快查询速度。这是通过创建indexes在meta字典中调用的索引规范列表完成的，其中索引规范可以是单个字段名称，包含多个字段名称的元组和包含完整索引定义的字典。
顺序可以通过在字段名前加上+（用于升序）或-号（用于降序）来指定。请注意，方向只对多字段索引很重要。文本索引可以通过在字段名前添加一个$来指定。散列索引可以通过在字段名前添加#来指定：
```
class Page(Document):
    category = IntField()
    title = StringField()
    rating = StringField()
    created = DateTimeField()
    meta = {
        'indexes': [
            'title',
            '$title',  # 文本索引
            '#title',  # 散列索引
            ('title', '-rating'),
            ('category', '_cls'),
            {
                'fields': ['created'],
                'expireAfterSeconds': 3600
            }
        ]
    }

```
如果采用字段，那么以下选项可用：
* fileds
要索引的字段。与上述相同的格式指定
* cls
如果您有多态模型可以继承并allow_inheritance打开，则可以配置索引是否应该将该_cls字段自动添加到索引的开头
* unique
索引是否应该是唯一的
* expireAfterSeconds（可选的）
允许您通过设置以秒为单位时间，过期来自动将某个字段中的数据过期。

## 十四、排序
可以使用QuerySet使用的ordering属性指定默认排序，排序在QuerySet创建时应用，并且可以通过随后的order_by()覆盖：
```
from datetime import datetime

class BlogPost(Document):
    title = StringField()
    published_date = DateTimeField()

    meta = {
        'ordering': ['-published_date']
    }

blog_post_1 = BlogPost(title="Blog Post #1")
blog_post_1.published_date = datetime(2010, 1, 5, 0, 0 ,0)

blog_post_2 = BlogPost(title="Blog Post #2")
blog_post_2.published_date = datetime(2010, 1, 6, 0, 0 ,0)

blog_post_3 = BlogPost(title="Blog Post #3")
blog_post_3.published_date = datetime(2010, 1, 7, 0, 0 ,0)

blog_post_1.save()
blog_post_2.save()
blog_post_3.save()

# 通过默认的排序（降序），获取第一篇文章
# from BlogPost.meta.ordering
latest_post = BlogPost.objects.first()
assert latest_post.title == "Blog Post #3"

# 覆盖原来的默认排序规则，采用升序
first_post = BlogPost.objects.order_by("+published_date").first()
assert first_post.title == "Blog Post #1"

```
### 14.1 order_by
可以使用order_by()按1个或多个键确定结果。
```
# Order by ascending dateblogs = BlogPost.objects().order_by('date')    # equivalent to .order_by('+date')

# Order by ascending date first, then descending titleblogs = BlogPost.objects().order_by('+date', '-title')

```
### 14.2 skip和limit
```
# Only the first 5 peopleusers = User.objects[:5]

# All except for the first 5 peopleusers = User.objects[5:]

# 5 users, starting from the 11th user foundusers = User.objects[10:15]

```

## 十五、过滤查询
查询可以通过调用带有字段查找关键字参数对象进行筛选。关键字参数中的密钥与您正在查询document上的字段对应：
```
# This will return a QuerySet that will only iterate over users whose# 'country' field is set to 'uk'uk_users = User.objects(country='uk')

```
**嵌入式文档上的字段也可以使用字段查找语法，使用双下划线代替对象属性访问语法的点**
```
# This will return a QuerySet that will only iterate over pages that have# been written by a user whose 'country' field is set to 'uk'uk_pages = Page.objects(author__country='uk')

```
### 15.1 查询参数：
* ne–不等于
* lt–小于
* lte–小于或等于
* gt–大于
* gte–大于或等于
* not–否定标准检查，可在其他操作员之前使用（例如Q(age__not__mod=(5, 0)))
* in–值列在列表中（应提供值列表）
* nin–值不在列表中（应提供值列表）
* mod–，其中和是两个提供的值value % x == yxy
* all–提供的值列表中的每一个项目都在数组中
* size–阵列的大小
* exists–存在字段值

### 15.2 字符串查询：
* exact–字符串字段与价值完全匹配
* iexact–字符串字段与值完全匹配（案例不敏感）
* contains–字符串字段包含值
* icontains–字符串字段包含值（案例不敏感）
* startswith–字符串字段从价值开始
* istartswith–字符串字段从值开始（案例不敏感）
* endswith–字符串字段以值结尾
* iendswith–字符串字段以值结尾（案例不敏感）
* match–执行$elemMatch，以便您可以在数组中匹配整个文档

## 十六、列表查询
* 包含该项的列表将匹配：
```
class Page(Document):
    tags = ListField(StringField())

# This will match all pages that have the word 'coding' as an item in the# 'tags' listPage.objects(tags='coding')

```
* 可以使用数字值，按列表中的位置进行查询
```
Page.objects(tags__0='db')

```
* 如果只想要获取列表的一部分，例如：可以使用切片操作：
```
# comments - skip 5, limit 10Page.objects.fields(slice__comments=[5, 10])

```
* 对于更新文档，如果不知道列表中的位置，则可以使用$定位操作
```
ost.objects(comments__by="joe").update(**{'inc__comments__$__votes': 1})
ost.objects(comments__by="joe").update(**{'inc__comments__$__votes': 1})

```
## 十七、默认文档查询
第一个参数是定义该方法的document类
第二个是初始查询集。该方法需要用queryset_manager()装饰才能被识别。
```
class BlogPost(Document):
    title = StringField()
    date = DateTimeField()

    @queryset_manager
    def objects(doc_cls, queryset):
        # This may actually also be done by defining a default ordering for
        # the document, but this illustrates the use of manager methods
        return queryset.order_by('-date')

```
### 17.1自定义查询
若要使用自定义的class来进行查询，需要在meta中进行配置
```
class AwesomerQuerySet(QuerySet):

    def get_awesome(self):
        return self.filter(awesome=True)

class Page(Document):
    meta = {'queryset_class': AwesomerQuerySet}

# To call:Page.objects.get_awesome()

```
## 十八、计数
```
num_users = User.objects.count()

```
* 如果只想获得queryset数据的长度而不做其他操作，count()更好
* 如果既要计算数据集的长度，又要对querset数据做其他操作（如过去每个对象的属性等），使用len()更有优势

## 十九、聚合计算
### 19.1 总和
```
yearly_expense = Employee.objects.sum('salary')
```
### 19.2 平均值
```
mean_age = User.objects.average('age')
```
### 19.3 获取item的频率
MongoEngine提供了一个方法来获取一个在集合里item的频率-item_frequencies()。下面一个例子可以生成tag-clouds
```
class Article(Document):
    tag = ListField(StringField())

# After adding some tagged articles...
tag_freqs = Article.objects.item_frequencies('tag', normalize=True)

from operator import itemgetter
top_tags = sorted(tag_freqs.items(), key=itemgetter(1), reverse=True)[:10]

```
## 二十、aggregate
[CSDN网站的借鉴](https://blog.csdn.net/tmpbook/article/details/51259293)
```
class Person(Document):
    name = StringField()

Person(name='John').save()
Person(name='Bob').save()

pipeline = [
    {"$sort" : {"name" : -1}},
    {"$project": {"_id": 0, "name": {"$toUpper": "$name"}}}
    ]data = Person.objects().aggregate(pipeline)
    assert data == [{'name': 'BOB'}, {'name': 'JOHN'}]

```
## 二十一、高级查询
 和 或的组合操作
 
```
from mongoengine.queryset.visitor import Q

# Get published postsPost.objects(Q(published=True) | Q(publish_date__lte=datetime.now()))

# Get top posts
Post.objects((Q(featured=True) & Q(hits__gte=1000)) | Q(hits__gte=5000))

```
## 二十二、更新操作

>* set–设置特定值
>* unset–删除特定值（自蒙哥德布v1.3）
>* inc–将价值增加一个给定金额
>* dec–将价值减损给定金额
>* push–将值附加到列表中
>* push_all–将多个值附加到列表中
>* pop–根据值删除列表的第一个或最后一个元素
>* pull–从列表中删除值
>* pull_all–从列表中删除多个值
>* add_to_set–仅在其不在列表中的情况下向列表添加值
```
>>> post = BlogPost(title='Test', page_views=0, tags=['database'])
>>> post.save()
>>> BlogPost.objects(id=post.id).update_one(inc__page_views=1)
>>> post.reload()  # the document has been changed, so we need to reload it
>>> post.page_views
1
>>> BlogPost.objects(id=post.id).update_one(set__title='Example Post')
>>> post.reload()
>>> post.title'
Example Post'
>>> BlogPost.objects(id=post.id).update_one(push__tags='nosql')
>>> post.reload()
>>>  post.tags
['database', 'nosql']
```
如果不知道索引的位置，可以使用以下操作来更新列表项目
```
post = BlogPost(title='Test', page_views=0, tags=['database', 'mongo'])
>>> post.save()
>>> BlogPost.objects(id=post.id,tags='mongo').update(set__tags__S='mongodb')
>>>post.reload()
>>>post.tags
['database', 'mongodb']
```

## 二十三、动态查询数据

```shell
query = {"status":"default"}
User.objects(__raw__==query).order_by("-status")
```
