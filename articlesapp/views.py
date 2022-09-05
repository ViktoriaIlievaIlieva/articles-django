from django.shortcuts import render, redirect
from articlesapp.models import Articles


def home(request):

    articles = Articles.objects.all().order_by("-id")
    last_three_in_ascending_order = articles[:3]

    return render(request, "home.html", {"last_three_in_ascending_order": last_three_in_ascending_order})


def all_articles(request):

    articles = Articles.objects.all()

    return render(request, "all_articles.html", {"articles": articles})


def single_article(request):

    id = request.GET.get("id")
    article = Articles.objects.get(id=id)
    return render(request, "single_article.html", {"article": article})


def delete_article(request):
    id = request.GET.get("id")
    article = Articles.objects.get(id=id)
    article.delete()

    return redirect("/")


def new_article(request):
    if request.method == "GET":
        return render(request, "new_article.html")

    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        publish_date = request.POST.get("publish_date")

        new_article = Articles(title=title, content=content, publish_date=publish_date)
        new_article.save()
        id = new_article.id

        return redirect(f"/single-article/?id={id}")

