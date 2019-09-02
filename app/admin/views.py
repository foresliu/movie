# -*- coding:utf-8 -*-

from . import admin


@admin.route('/')
def index():
    return "index"


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    return "login"
