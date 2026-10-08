from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    """Display tasks and create a new task from a POST request.

    :param request: Django HTTP request object.
    :return: Rendered task page or redirect to home.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("home")

    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/index.html", {"tasks": tasks})


def toggle_task(request, task_id):
    """Toggle the completed status of a task.

    :param request: Django HTTP request object.
    :param task_id: ID of the task to update.
    :return: Redirect to the home page.
    """
    if request.method != "POST":
        return redirect("home")

    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("home")


def delete_task(request, task_id):
    """Delete a task using its ID.

    :param request: Django HTTP request object.
    :param task_id: ID of the task to delete.
    :return: Redirect to the home page.
    """
    if request.method != "POST":
        return redirect("home")

    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("home")