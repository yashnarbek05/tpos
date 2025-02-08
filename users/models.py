from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def normalize_login(self, login: str) -> str:
        return login.lower().strip()

    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError("login is required")
        login = self.normalize_login(login)
        user: User = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **extra_fields):
        return self.create_user(**extra_fields)


class UserGroups(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='usgrp_id',
    )
    name = models.CharField(
        max_length=150,
        default='-',
        db_column='usgrp_name',
        db_collation='utf8mb3_general_ci',
    )
    deleted = models.IntegerField(
        default=0,
        db_column='usgrp_deleted',
    )

    class Meta:
        managed = False
        db_table = 'dir_users_groups'


class User(models.Model):
    id = models.AutoField(
        primary_key=True,
        db_column='us_id',
        db_index=True,
    )
    group = models.ForeignKey(
        UserGroups,
        models.DO_NOTHING,
        db_column='us_group',
        default=4,
    )
    name1 = models.CharField(
        max_length=150,
        db_column='us_name1',
        db_collation='utf8mb3_general_ci',
    )
    name2 = models.CharField(
        max_length=150,
        db_column='us_name2',
        db_collation='utf8mb3_general_ci',
    )
    name3 = models.CharField(
        max_length=150,
        db_column='us_name3',
        db_collation='utf8mb3_general_ci',
    )
    date_of_birth = models.DateField(
        db_column='us_date_of_birth',
    )
    sex = models.CharField(
        max_length=1,
        default='M',
        db_column='us_sex',
        db_collation='utf8mb3_general_ci',
    )
    adress = models.CharField(
        max_length=150,
        db_column='us_adress',
        db_collation='utf8mb3_general_ci',
    )
    phone = models.CharField(
        max_length=150,
        db_column='us_phone',
        db_collation='utf8mb3_general_ci',
    )
    e_mail = models.CharField(
        max_length=150,
        db_column='us_e_mail',
        db_collation='utf8mb3_general_ci',
    )
    password = models.CharField(
        max_length=32,
        db_column='us_password',
        db_collation='utf8mb3_general_ci',
    )
    description = models.CharField(
        max_length=300,
        db_column='us_description',
        db_collation='utf8mb3_general_ci',
    )
    hash = models.CharField(
        max_length=32,
        db_column='us_hash',
        db_collation='utf8mb3_general_ci',
    )
    reward = models.FloatField(
        blank=True,
        null=True,
        default=0,
        db_column='us_reward',
    )
    autor0 = models.IntegerField(
        db_column='us_autor0',
    )
    date0 = models.DateTimeField(
        db_column='us_date0',
    )
    autor1 = models.IntegerField(
        db_column='us_autor1',
    )
    date1 = models.DateTimeField(
        db_column='us_date1',
    )
    deleted_mark = models.IntegerField(
        default=0,
        db_column='us_deleted_mark',
    )
    deleted = models.IntegerField(
        default=0,
        db_column='us_deleted',
    )
    login = models.CharField(
        max_length=30,
        db_column='us_login',
        db_collation='utf8mb3_general_ci',
    )
    allowed_objects = models.CharField(
        max_length=2048,
        default='0',
        db_column='us_allowed_objects',
        db_collation='utf8mb3_general_ci',
    )
    personal_desktop = models.IntegerField(
        default=0,
        db_column='us_personal_desktop',
    )
    max_discount = models.IntegerField(
        blank=True,
        null=True,
        db_column='max_discount',
    )
    allowed_debt = models.IntegerField(
        blank=True,
        null=True,
        db_column='allowed_debt',
    )
    allow_clear_receipt = models.IntegerField(
        blank=True,
        null=True,
        db_column='allow_clear_receipt',
    )
    allow_shift = models.IntegerField(
        blank=True,
        null=True,
        db_column='allow_shift',
    )
    passw = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_column='us_pass',
        db_collation='utf8mb3_general_ci',
    )

    objects = CustomUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'id'
    is_anonymous = None
    is_authenticated = None
    

    def set_password(self, password: str) -> None:
        self.pass_ = password

    def check_password(self, password: str) -> bool:
        return self.passw == password
    

    class Meta:
        managed = False
        db_table = 'dir_users'
