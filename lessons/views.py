from django.shortcuts import render, redirect
from .models import Lesson
from .forms import LessonForm

def lesson_list(request):
    q = request.GET.get("q", "")
    lessons = Lesson.objects.all()

    if q:
        lessons = lessons.filter(title__icontains=q)

    return render(request, "lessons/lesson_list.html", {
        "lessons": lessons,
        "q": q,
    })


def lesson_create(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lesson_list")
    else:
        form = LessonForm()

    return render(request, "lessons/lesson_form.html", {
        "form": form,
        "mode": "Create",
    })
