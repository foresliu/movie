# -*- coding:utf-8 -*-

from . import admin


@admin.route('/')
def index():
    print "hello"


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    pass
