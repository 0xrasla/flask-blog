from flask import render_template, flash, redirect, url_for, jsonify
from blogger import app
from blogger.forms import CreateFrom
from blogger.models import Blog


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/blog/all_blogs")
def allblogs():
    allblogs = Blog.objects
    return render_template("allblogs.html", title="All Blogs", all=allblogs)


@app.route("/blog/create", methods=["GET", "POST"])
def create():
    form = CreateFrom()

    if form.validate_on_submit():
        flash("Your Post Posted Successfully....")

        blog = Blog(
            title=form.title.data, author=form.author.data, content=form.content.data
        )
        blog.save()

        return redirect(url_for("allblogs"))
    return render_template("/blog/create.html", title="Create New Blog", form=form)


@app.route("/delete/<id>")
def deleterecord(id):
    blog = Blog.objects(id=id).first()
    blog.delete()

    return redirect(url_for("allblogs"))


@app.route("/blog/<id>")
def viewrecord(id):
    blog = Blog.objects(id=id).first()
    return render_template("blog/singleblog.html", blog=blog, title="Single Blog")


@app.route("/blog/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = CreateFrom()
    blog = Blog.objects(id=id).first()
    form.content.default = blog.content

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.author = form.author.data
        blog.content = form.content.data

        blog.save()

        return redirect(url_for("viewrecord", id=id))

    return render_template("blog/edit.html", blog=blog, title="Edit Blog", form=form)
