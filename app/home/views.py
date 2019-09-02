# -*- coding:utf-8 -*-

from . import home


@home.route("/register/", methods=["GET", "POST"])
def register():
    pass


@home.route("/login/", methods=['GET', 'POST'])
def login():
    pass
