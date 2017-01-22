from django.shortcuts import render
from ui.models import Feedback
# Create your views here.
def show_feedbacks(request):
    return render(request, 'base.html', {
        "page_title": "All Feedbacks"
    })


def submit_feedback(request):
    return render(request, 'base.html', {
        "page_title": "Submit your Feedback","feedbacks":Feedback.objects.all()
    })
