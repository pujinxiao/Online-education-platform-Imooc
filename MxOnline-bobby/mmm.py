# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class CoursesCourse(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    detail = models.TextField()
    degree = models.CharField(max_length=2)
    learn_times = models.IntegerField()
    students = models.IntegerField()
    fav_nums = models.IntegerField()
    image = models.CharField(max_length=100)
    click_nums = models.IntegerField()
    add_time = models.DateTimeField()
    course_org_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=20)
    tag = models.CharField(max_length=10)
    teacher_id = models.IntegerField(blank=True, null=True)
    teacher_tell = models.CharField(max_length=300)
    youneed_know = models.CharField(max_length=300)
    is_banner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_course'


class CoursesCourseresource(models.Model):
    name = models.CharField(max_length=100)
    download = models.CharField(max_length=100)
    add_time = models.DateTimeField()
    course_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_courseresource'


class CoursesLesson(models.Model):
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField()
    course_id = models.IntegerField()
    learn_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_lesson'


class CoursesVideo(models.Model):
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField()
    lesson_id = models.IntegerField()
    url = models.CharField(max_length=200)
    learn_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_video'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OperationCoursecomments(models.Model):
    comments = models.CharField(max_length=200)
    add_time = models.DateTimeField()
    course_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operation_coursecomments'


class OperationUserask(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    course_name = models.CharField(max_length=50)
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'operation_userask'


class OperationUsercourse(models.Model):
    add_time = models.DateTimeField()
    course_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operation_usercourse'


class OperationUserfavorite(models.Model):
    fav_id = models.IntegerField()
    fav_type = models.IntegerField()
    add_time = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operation_userfavorite'


class OperationUsermessage(models.Model):
    user = models.IntegerField()
    message = models.CharField(max_length=500)
    has_read = models.IntegerField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'operation_usermessage'


class OrganizationCitydict(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'organization_citydict'


class OrganizationCourseorg(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    click_nums = models.IntegerField()
    fav_nums = models.IntegerField()
    image = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    add_time = models.DateTimeField()
    city_id = models.IntegerField()
    category = models.CharField(max_length=20)
    course_nums = models.IntegerField()
    students = models.IntegerField()
    tag = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'organization_courseorg'


class OrganizationTeacher(models.Model):
    name = models.CharField(max_length=50)
    work_years = models.IntegerField()
    work_company = models.CharField(max_length=50)
    work_position = models.CharField(max_length=50)
    points = models.CharField(max_length=50)
    click_nums = models.IntegerField()
    fav_nums = models.IntegerField()
    add_time = models.DateTimeField()
    org_id = models.IntegerField()
    image = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organization_teacher'


class Taobao(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taobao'


class UsersBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    index = models.IntegerField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_banner'


class UsersEmailverifyrecord(models.Model):
    code = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    send_type = models.CharField(max_length=30)
    send_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_emailverifyrecord'


class UsersUserprofile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    nick_name = models.CharField(max_length=50)
    birday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class UsersUserprofileGroups(models.Model):
    userprofile_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_userprofile_groups'
        unique_together = (('userprofile_id', 'group_id'),)


class UsersUserprofileUserPermissions(models.Model):
    userprofile_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_userprofile_user_permissions'
        unique_together = (('userprofile_id', 'permission_id'),)


class XadminBookmark(models.Model):
    title = models.CharField(max_length=128)
    url_name = models.CharField(max_length=64)
    query = models.CharField(max_length=1000)
    is_share = models.IntegerField()
    content_type_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xadmin_bookmark'


class XadminLog(models.Model):
    action_time = models.DateTimeField()
    ip_addr = models.CharField(max_length=39, blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.CharField(max_length=32)
    message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xadmin_log'


class XadminUsersettings(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xadmin_usersettings'


class XadminUserwidget(models.Model):
    page_id = models.CharField(max_length=256)
    widget_type = models.CharField(max_length=50)
    value = models.TextField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xadmin_userwidget'
