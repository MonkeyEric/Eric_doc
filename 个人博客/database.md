# ������վ�����ݽṹ

## admin �û�

|�ֶ�|����	|��	|Ĭ��	|ע��|
|:---|:--------- |:--- |---|------|
|id	|integer	|��	|	|����|
|role	|varchar(10)	|��	|	|��ͨ�û���VIP�û�������Ա��SVIP��1�ˣ�|
|email	|varchar(20)	|��	|	|�ʼ�|
|password_hash|	varchar(130)|	��|	|	|����|
|blog_title	|varchar(20)|	��	|	|���ͱ���|
|blog_sub_title|	varchar(20)|	��	|	|���͸�����|
|name	|varchar(20)|	��|	|	|�ǳ�|
|about	|text|	��|	|	|���ڣ���飩|
|timestamp	|datetime|	��|	|	|�������ݿ�ʱ��|
|last_login_time|	datetime	|��	|	|�ϴε�¼ʱ��|
|avatar_path|	varchar(30)|	��|	|	ͷ����·��|


## post ����	
|�ֶ�|����|��|Ĭ��|ע��|
|:---|:--------- |:--- |---|------|
|id|integer|��| |	����|
|title|	varchar��80��|��| |����|
|body|text|��| |��������|
|timestamp|datetime|	��|		|���·���ʱ��|
|can_comment|boolean|	��	|TRUE	|�Ƿ��������|
|author_id|integer|	��	|	|����id|
|category_id|integer|	��|	|	��ǩid|
|post_cover|varchar��30��|	��	|���ѡ��	|�Լ�����һ�������ļ��У�Ȼ�������÷���|
|category|���| |	|post��category|
|comments|���|	|	|post��comments|

