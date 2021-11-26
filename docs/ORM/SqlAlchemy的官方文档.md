### 1. 版本检查
```
import sqlalchemy
sqlalchemy.__version__
```

### 2. 链接
echo：True   会显示每条执行的SQL语句，可以关闭。
create_engine()返回一个Engine的实例，并且它表示通过数据库语法处理细节的核心接口
```
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory',echo=True)
```

### 3.声明映像
当使用orm时，构造进程首先描述数据库的表，然后定义我们用来映射哪些表的类。
在现版本中，这2个任务通常一起执行，通过使用Declarative方法，我们可以创建一些包含描述要被映射的实际数据库表的准则的映射类。
通过delarative_base()创建一个基类：
```
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
# 依据这个base定义任意数量的映射类
from sqlalchemy import Column,Integer,String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
```
### 4.构造模式（暂无）
### 5.创建映射类的实例
```
ed_user = User(name='ed',fullname='Ed Jones',password='edpassword')
```
### 6. 创建会话
orm通过Session与数据库建立链接的，当应用第一次载入时，我们定义一个Session类(声明create_engine（）的同时)，这个session类为新的session对象提供工厂服务。
```
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
```
这个定制的session类会创建绑定到数据库的session对象。如果需要和数据库建立链接，只需要实例化一个session：
```
session = Session()
```
此时对象的实例仍在等待中，只有在被使用的时候，才会建立链接。

### 7.添加新对象
```
ed_user = User(name='ed',fullname='Ed Jones',passoword='edspassword')
session.add(ed_user)
session.commit()  # 提交所有剩余的更改数据库
```
### 8.回滚
```
session.rollback()
```
### 9. 查询
通过session的query()方法创建一个查询对象。这个函数的参数数量是可变的，参数可以是任何类或者是类的描述的集合。
```
for instance in session.query(User).order_by(User.id)
    print instance.name,instance.fullname
```
或者
```
for name,fullname in session.query(User.name,User.fullname):
    print name,fullname
```
label()相当于row.name
```
for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)
```
aliased()，是类的别名，如果有多个实体都要查询一个类，可以用aliased()
```
for sqlalchemy.orm import aliased
    user_alias = aliased(User,name='user_alias')
for row in session.query(user_alias,user_alias.name).all():
    print row.user_alias
```
Query的Limit和Offset操作：
```
for u in session.query(User).order_by(User.id)[1:3]:
    print u
```
#### 9.1 关键字过滤查询

* query.filter(User.name == 'ed')  # 等于
* query.filter(User.name != 'ed')   # 不等于
* query.filter(User.name.like('%ed%'))  # 模糊查询
* user.filter(User.name.in_(['ed','wendy','jack']))  # in
* query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))  # in
* query.filter(~User.name.in_(['ed','wendy','jack']))  # not in
* query.filter(User.name ==None)  #is None
* query.filter(User.name !=None)  # not None
**与的操作**
```
from sqlalchemy import and_
```
* query.filter(and_(User.name == 'ed',User.fullname =='Ed Jones')) # and
* query.filter(User.name =='ed',User.fullname =='Ed Jones')  ＃and
* query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones' ) # and

**并的操作**
```
from sqlalchemy import or_
```
* query.filter(or_(User.name =='ed',User.name =='wendy'))  # or
* query.filter(User.name.match('Wendy'))  #match

#### 9.2 返回列表和数量

1. all()返回一个列表：可以进行Python列表的操作
```
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
query.all()
输出
[<User(name='ed',fullname='EdJones', password='f8s7ccs')>,<User(name='fred',fullname='FredFlinstone', password='blah')>]
```
2. first() 适用于限制一个情况，返回查询到的第一个结果作为标量？
```
query.first()

<User(name='ed',fullname='Ed Jones', password='f8s7ccs')>
```
3. one()完全获取所有行，并且如果查询到的不只有一个对象或是复合行，就会抛出异常。
```
from sqlalchemy.orm.exc import MultipleResultsFound
user=query.one()
try:
    user = query.one()
except:
    MultipleResultsFound, e:
    print e
```
如果一行也没有，会抛出no row was found的错误。
**scalar()作为one()方法的一句，并且在one()成功基础上返回行的第一列**
```
query = session.query(User.id).filter(User.name =='ed')
query.scarlar()
```
#### 9.3 使用字符串SQL

#### 9.4 计数
 count()用来统计查询结果的数量 
```
session.query(User).filter(User.name.like('%ed')).count()
```
更高级的用法：func.count()
```
from sqlalchemy import func
session.query(func.count(User.name),username).group_by(User.name).all()
[(1,'ed'),(1,'fred'),(1,'mary'),(1,'wendy')]
```
为了实现简单技术SELECT count(\*) FROM table:
```
session.query(func.count('*')).select_from(User).scalar()
或者
session.query(func.count(User.id)).scalar()
```
### 10. 建立联系（外键）
```
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    addresses = relationship("Address", backref="user")


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
```

#### **具体解释：**
1、假如没有relationship，我们只能像下面这样调用关系数据。
#给定参数user.name，获取该user的addresses（从一个表查询完了之后，再去另一个表中查找）
```
def get_addresses_from_user(user_name):
    user=session.query(User).filter_by(name=user_name).first()
    address=session.query(Address).filter_by(user_id=user.id).first()
    return address
```
如果在User中使用relationship定义addresses属性的话，
```
addresses=relationship('Address')
```
则我们直接在User对象中通过addresses属性获得指定用户的所有地址
```
def get_addresses_from_user(user_name):
    user=session.query(User).filter_by(name=user_name).first()
    return user.addresses
```
**注意，在上面的addresses属性中，我们并没有定义backref属性，所以我们可以通过User对象获取所拥有的地址，但是不能通过Address对象获取到所属的用户**
```
>>> u = User()
>>> u.addresses
[]
>>> a = Address()
>>> a.user
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Address' object has no attribute 'user'
```
但是当我们有从Address对象获取所属用户的需求时，backref参数就派上用场了。
```
addresses = relationship('Address', backref='user')
```
>简而言之
**backref用于在关系另一端的类中快捷地创建一个指向当前类对象的属性**


**概念性的东西**
>在大多数的外键约束关系数据库只能连接到一个主键列，或具有唯一约束的列。
>外键约束如果是指向多个列的主键，并且它本身也具有多列，这种被称为：“复合外键”
>外键可以自动更新自己来相应它所引用的行或者列。这被称为级联，是一种建立在关系数据库的功能。
>外键可以参考自己的表格。这种被称为“自引”外键

#### backref 和 back_populates的区别
[brackref和back_populates的区别](https://blog.csdn.net/sinat_41667855/article/details/118729091?spm=1001.2014.3001.5501)
放代码：
```
class Comment(db.Model):    
    id = db.Column(db.Integer, primary_key=True)    
    author = db.Column(db.String(30))    
    email = db.Column(db.String(254))    
    site = db.Column(db.String(255))    
    body = db.Column(db.Text)    
    from_admin = db.Column(db.Boolean, default=False)    
    reviewed = db.Column(db.Boolean, default=False)    
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)    
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))    
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))    
    post = db.relationship('Post', back_populates='comments')    
    replies = db.relationship('Comment', back_populates='replied', cascade='all')    
    replied = db.relationship('Comment', back_populates='replies', remote_side=[id])

```
> cascade的属性

* cascade=save-update; 默认选项，在添加一条数据的时候，会把其他和它相关联的数据都添加到数据中。若不想同步添加，令cascade=''
* delete；表示当删除某一个模型中的数据的时候，是否也删掉使用relationship和他相关的数据。
* delete-orphan：表示当对一个ORM对象接触了父表中的关联对象的时候，自己便会被删除掉。（即子表中的某条数据没有了关联数据，则该条数据会被自动删除掉）。当然如果父表中的数据被删除，自己也会被删除。这个选项只能用在一对多上，不能用在多对多以及多对一上。并且还需要在子模型中relationship中，增加一个single_parent=True的参数。
* merge：默认选项，当在使用session.merge，合并一个对象的时候，会将使用了relationship相关联的对象也进行merge操作。如user表中已有一条数据id=1,而脚本中另外生成了一条id=1的数据。那么就可用merge覆盖掉原数据及相关联数据。
* all：是对 save-update、merge、refresh-expire,expunge,delete几种的缩写。

> remote_side
* remote_side 字段用于建立多对一的关系，如果不加这个字段会报错。

### 11.操作主外键关联的对象
现在我们已经在User类中创建了一个空的addresser集合，可变集合类型，例如set和dict，都可以用，但是默认的集合类型是list。
```
>>>jack = User(name='jack',fullname='Jack Bean',passowrd ='gjffdd')
>>>jack.address
[]
```
现在可以直接在User对象中添加Address对象。只需要指定一个完整的列表：
```
jack.addresses = [Address(email_adress='jack@google.com'),Address('j25@yahoo.com')]
```
### 12.使用JOINS查询
现在有了2张表，可以进行更多的查询操作。
```
for u,a in session.query(User,Address).filter(User.id==Adress.user_id).filter(Address.email_address=='jack@google.com').all()
    print u
    print a
 
```
**用Query.join()方法会更加简单**
```
session.query(User).join(Address).filter(Adress.email_address=='jack@google.com').all()
```

之所以Query.join()知道怎么join两张表是因为他们之间只有一个外键。如果两张表中没有外键或一个以上的外键，当下列几种形式使用的时候，Query.join()可以表现的更好：
```
query.join(Address,User.id==Address.user_id)  # 明确的条件
query.join(User.addresses)  #指定从左到右的关系
query.join(Address,User.addresses)  # 同样，有明确的目标
query.join('addresses')  # 同样，使用字符串
query.outer_join(User.addresses)  # LEFT OUTER JOIN
```
#### 1.使用别名
当在多个表中查询时，如果同一张表需要被引用好几次，SQL通常要求对这个表起一个别名，因此，SQL可以区分这个表进行的其他操作。Query也支持别名的操作。下面我们joinAddress实体两次，找到同时拥有2个不同的email的用户。
```
>>> from sqlalchemy.orm import aliased
>>>adalias1 = aliased(Address)
>>>adalias2 = aliaed(Address)
>>> for username,email1,email2 in 
      session.query(User.name,adalias1.email_address,adalias2.email_address).
      join(adalias1,User.addresses).
      join(adalias2,User.addresses).
      filter(adalias1.email_address =='jack@google.com').
      filter(adalias2.email_address == 'j25@yahoo.com'):
      print username,email1
```

#### 2.使用子查询
```
from sqlalchemy.sql import func
stmt = session.query(Address.user_id.func.count('*').
          label('address_count')).group_by(Address.user_id).subquery()
>>>
for u,count in session.query(User,stmt.c.address_count).outerjoin(stmt,User.id ==stmt.c.user_id).order_by(User.id)
    print u,count
```
#### 3.从子查询中选择实体
上面的代码中，我们只返回了包含子查询的一个列的结果。如果想要子查询映射到一个实体的话，使用aliaesd()设置一个要映射类的子查询别名。
```
stmt = session.query(Address).filter(Address.email_address!='j25@yahoo.com').subquery()
adalias = aliased(Address,stmt)
>>> for user,address in session.query(User,adalias).join(adalias,User.addresses):
    print user
    print address
```

#### 4.使用exists（存在？)
#### 5.常见的关系运算符
== != None 都是用在多对一中，而contains()用在一对多的集合中：
```
query.filter(Address.user ==someuser)
query.filtere(User.addresses.contains(someaddress))
```
**Any()用于集合中**
```
query.filter(User.addresses.any(Address.email_address =='bar'))
query.filter(User.addresses.any(email_address='bar'))
```
**as()用在标量？不在集合中**
```
query.filter(Address.user.has(name='ed'))
```
**query.with_parent() 所有关系都适用**
```
session.query(Address).with_parent(someuser,'addresses')
```

[更多Sqlalchemy的使用经验](SQLAlchemy使用经验.md)