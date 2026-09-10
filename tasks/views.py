from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("home")

    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/index.html", {"tasks": tasks})


def toggle_task(request, task_id):
    if request.method != "POST":
        return redirect("home")

    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("home")


def delete_task(request, task_id):
    if request.method != "POST":
        return redirect("home")

    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")