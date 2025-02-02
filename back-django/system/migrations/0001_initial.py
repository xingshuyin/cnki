# Generated by Django 5.1.2 on 2024-11-04 06:45

import datetime
import django.db.models.deletion
import system.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(db_comment='名称', max_length=200, verbose_name='名称')),
                ('source', models.CharField(db_comment='来源', max_length=200, null=True, verbose_name='来源')),
                ('source_root', models.CharField(db_comment='基础来源', max_length=200, null=True, verbose_name='基础来源')),
                ('source_sub', models.CharField(db_comment='子版块', max_length=200, null=True, verbose_name='子版块')),
                ('tag', models.JSONField(db_comment='标签', default=list, null=True, verbose_name='标签')),
                ('content_md', models.TextField(db_comment='MARKDOWN内容', null=True, verbose_name='MARKDOWN内容')),
                ('content_html', models.TextField(db_comment='HTML内容', null=True, verbose_name='HTML内容')),
                ('file', models.JSONField(db_comment='文件', default=list, null=True, verbose_name='文件')),
                ('image', models.JSONField(db_comment='图片', default=list, null=True, verbose_name='图片')),
                ('video', models.JSONField(db_comment='视频', default=list, null=True, verbose_name='视频')),
                ('url', models.CharField(blank=True, db_comment='文章链接', max_length=100, null=True, verbose_name='文章链接')),
                ('url_hash', models.CharField(blank=True, db_index=True, max_length=255, null=True, unique=True)),
                ('type', models.IntegerField(choices=[(1, '图片'), (2, '视频'), (3, '文字')], db_comment='文章类型(1 图片, 2 视频, 3文字)', default=1)),
                ('view', models.IntegerField(db_comment='浏览数', default=0)),
                ('like', models.IntegerField(db_comment='点赞数', default=0)),
                ('comment', models.IntegerField(db_comment='评论数', default=0)),
                ('collect', models.IntegerField(db_comment='收藏数', default=0)),
                ('is_delete', models.BooleanField(db_comment='是否删除', default=False)),
                ('is_top', models.BooleanField(db_comment='是否置顶', default=False)),
                ('is_hot', models.BooleanField(db_comment='是否热门', default=False)),
                ('is_original', models.BooleanField(db_comment='是否原创', default=False)),
                ('is_recommend', models.BooleanField(db_comment='是否推荐', default=False)),
            ],
            options={
                'verbose_name': '文章',
                'db_table': 'article',
                'db_table_comment': '文章',
            },
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('file', models.FileField(max_length=200, storage=system.models.storage(), upload_to=system.models.make_single_file_name)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '文件',
                'db_table': 'file',
                'db_table_comment': '文件',
            },
        ),
        migrations.CreateModel(
            name='interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(db_comment='接口名称', max_length=50)),
                ('key', models.CharField(db_comment='标识符', max_length=50, null=True)),
                ('method', models.IntegerField(choices=[(0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'DELETE')], db_comment='请求方式')),
                ('path', models.CharField(db_comment='接口地址', max_length=100)),
                ('model', models.CharField(db_comment='接口模型', max_length=100)),
                ('model_name', models.CharField(db_comment='接口模型名称', max_length=100)),
            ],
            options={
                'verbose_name': '接口',
                'db_table': 'interface',
                'db_table_comment': '接口',
            },
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('username', models.CharField(blank=True, db_comment='登录用户名', max_length=32, null=True, verbose_name='登录用户名')),
                ('ip', models.CharField(blank=True, db_comment='登录ip', max_length=32, null=True, verbose_name='登录ip')),
                ('agent', models.TextField(blank=True, db_comment='agent信息', null=True, verbose_name='agent信息')),
                ('browser', models.CharField(blank=True, db_comment='浏览器名', max_length=200, null=True, verbose_name='浏览器名')),
                ('os', models.CharField(blank=True, db_comment='操作系统', max_length=200, null=True, verbose_name='操作系统')),
                ('continent', models.CharField(blank=True, db_comment='州', max_length=50, null=True, verbose_name='州')),
                ('country', models.CharField(blank=True, db_comment='国家', max_length=50, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, db_comment='省份', max_length=50, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, db_comment='城市', max_length=50, null=True, verbose_name='城市')),
                ('district', models.CharField(blank=True, db_comment='县区', max_length=50, null=True, verbose_name='县区')),
                ('isp', models.CharField(blank=True, db_comment='运营商', max_length=50, null=True, verbose_name='运营商')),
                ('area_code', models.CharField(blank=True, db_comment='区域代码', max_length=50, null=True, verbose_name='区域代码')),
                ('country_english', models.CharField(blank=True, db_comment='英文全称', max_length=50, null=True, verbose_name='英文全称')),
                ('country_code', models.CharField(blank=True, db_comment='简称', max_length=50, null=True, verbose_name='简称')),
                ('longitude', models.CharField(blank=True, db_comment='经度', max_length=50, null=True, verbose_name='经度')),
                ('latitude', models.CharField(blank=True, db_comment='纬度', max_length=50, null=True, verbose_name='纬度')),
                ('login_type', models.IntegerField(choices=[(1, '普通登录')], db_comment='登录类型', default=1, verbose_name='登录类型')),
            ],
            options={
                'verbose_name': '登录日志',
                'db_table': 'log',
                'db_table_comment': '登录日志',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='spider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(db_comment='规则名称-', max_length=50)),
                ('rule', models.JSONField(db_comment='规则', default=dict)),
                ('enable', models.BooleanField(db_comment='是否启用', default=True)),
            ],
            options={
                'verbose_name': '爬虫规则表',
                'db_table': 'spider',
                'db_table_comment': '爬虫规则表',
            },
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_comment='名称', max_length=100, verbose_name='名称')),
                ('code', models.CharField(db_comment='地区编码', db_index=True, max_length=20, unique=True, verbose_name='地区编码')),
                ('level', models.BigIntegerField(db_comment='地区等级(0省份 1城市 2区县 3乡级)', verbose_name='地区等级')),
                ('lat', models.CharField(blank=True, db_comment='纬度', max_length=10, null=True, verbose_name='纬度')),
                ('lng', models.CharField(blank=True, db_comment='经度', max_length=10, null=True, verbose_name='经度')),
                ('parent', models.ForeignKey(blank=True, db_comment='父地区编码', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.area', to_field='code', verbose_name='父地区编码')),
            ],
            options={
                'verbose_name': '地区',
                'db_table': 'area',
                'db_table_comment': '地区',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(db_comment='部门名称', max_length=20)),
                ('key', models.CharField(db_comment='标识符', max_length=50, null=True)),
                ('sort', models.IntegerField(db_comment='排序', default=1)),
                ('owner', models.CharField(blank=True, db_comment='负责人', max_length=32, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='system.dept')),
            ],
            options={
                'verbose_name': '部门',
                'db_table': 'dept',
                'db_table_comment': '部门',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('openid', models.CharField(db_comment='微信openid', max_length=100, null=True, unique=True, verbose_name='微信openid')),
                ('username', models.CharField(db_comment='账号', max_length=100, unique=True, verbose_name='账号')),
                ('role', models.JSONField(db_comment='角色', default=list, verbose_name='角色')),
                ('type', models.IntegerField(choices=[(1, '前端'), (2, '后端')], db_comment='类型', default=1, verbose_name='类型')),
                ('is_super', models.BooleanField(db_comment='是否为超级管理员', default=False, verbose_name='是否为超级管理员')),
                ('dept', models.ForeignKey(db_comment='部门', null=True, on_delete=django.db.models.deletion.PROTECT, to='system.dept', verbose_name='部门')),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
                'db_table_comment': '用户',
            },
            managers=[
                ('objects', system.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(db_comment='名称', max_length=100, null=True, verbose_name='名称')),
                ('code', models.CharField(db_comment='唯一编码', max_length=100, unique=True, verbose_name='编码')),
                ('file', models.JSONField(db_comment='文件', default=list, verbose_name='文件')),
                ('image', models.JSONField(db_comment='图片', default=list, verbose_name='图片')),
                ('area', models.ForeignKey(db_comment='区域', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system.area', to_field='code', verbose_name='区域')),
            ],
            options={
                'verbose_name': '企业',
                'db_table': 'enterprise',
                'db_table_comment': '企业',
            },
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('icon', models.CharField(blank=True, db_comment='菜单图标', max_length=64, null=True)),
                ('label', models.CharField(db_comment='菜单名称', max_length=64)),
                ('sort', models.IntegerField(blank=True, db_comment='显示排序', default=1, null=True)),
                ('is_link', models.BooleanField(db_comment='是否外链', default=False)),
                ('is_catalog', models.BooleanField(db_comment='是否目录', default=False)),
                ('path', models.CharField(blank=True, db_comment='路由地址', max_length=128, null=True)),
                ('component', models.CharField(blank=True, db_comment='组件地址', max_length=128, null=True)),
                ('name', models.CharField(blank=True, db_comment='路由名称', max_length=50, null=True)),
                ('disable', models.BooleanField(blank=True, db_comment='禁用状态', default=False, null=True)),
                ('cache', models.BooleanField(blank=True, db_comment='是否页面缓存', default=False, null=True)),
                ('parent', models.ForeignKey(blank=True, db_comment='上级菜单', db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='system.menu')),
            ],
            options={
                'verbose_name': '菜单',
                'db_table': 'menu',
                'db_table_comment': '菜单',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('name', models.CharField(max_length=50)),
                ('key', models.CharField(db_comment='标识符', max_length=50, null=True)),
                ('permission', models.IntegerField(choices=[(0, '仅本人数据权限'), (1, '本部门及以下数据权限'), (2, '本部门数据权限'), (3, '全部数据权限'), (4, '自定数据权限')], db_comment='数据权限范围', default=0)),
                ('is_admin', models.BooleanField(db_comment='是否为管理员', default=False)),
                ('interface', models.ManyToManyField(blank=True, to='system.interface')),
                ('menu', models.ManyToManyField(blank=True, to='system.menu')),
            ],
            options={
                'verbose_name': '角色',
                'db_table': 'role',
                'db_table_comment': '角色',
            },
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('icon', models.CharField(db_comment='头像', default='https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png', max_length=100, null=True, verbose_name='头像')),
                ('birthday', models.DateField(db_comment='生日', null=True, verbose_name='生日')),
                ('signature', models.CharField(db_comment='个性签名', max_length=100, null=True, verbose_name='个性签名')),
                ('name', models.CharField(db_comment='姓名', max_length=100, null=True, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], db_comment='性别', default=0, null=True, verbose_name='性别')),
                ('email', models.EmailField(db_comment='邮箱', max_length=254, null=True, verbose_name='邮箱')),
                ('phone', models.CharField(db_comment='电话', max_length=12, null=True, verbose_name='电话')),
                ('article_collect', models.ManyToManyField(related_name='collect_user', to='system.article', verbose_name='收藏文章')),
                ('article_like', models.ManyToManyField(related_name='like_user', to='system.article', verbose_name='点赞文章')),
                ('follow_user', models.ManyToManyField(to='system.user_info', verbose_name='关注用户')),
                ('user', models.OneToOneField(db_comment='用户', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'user_info',
                'db_table_comment': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='article_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, db_comment='创建时间', default=datetime.datetime.now, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_comment='更新时间', null=True)),
                ('dept_belong', models.IntegerField(blank=True, db_comment='所属部门id', null=True)),
                ('creator', models.IntegerField(blank=True, db_comment='创建人id', null=True)),
                ('content', models.CharField(help_text='评论内容', max_length=1000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='system.article')),
                ('reply', models.ForeignKey(blank=True, help_text='回复对象', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reply_set', to='system.article_comment', verbose_name='回复对象')),
                ('root', models.ForeignKey(blank=True, help_text='根评论对象', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='root_set', to='system.article_comment', verbose_name='根评论对象')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='system.user_info')),
            ],
            options={
                'verbose_name': '文章评论',
                'db_table': 'article_comment',
                'db_table_comment': '文章评论',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, db_comment='作者', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system.user_info', verbose_name='作者'),
        ),
    ]
