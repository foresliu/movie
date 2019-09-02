# -*- coding:utf-8 -*-

from . import home


@home.route("/register/", methods=["GET", "POST"])
def register():
    return "<h1>register</h1>"


@home.route("/login/", methods=['GET', 'POST'])
def login():
    return "login"
