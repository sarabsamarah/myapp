from django.shortcuts import render
# from django.template import loader
# Create your views here.
# from django.http import HttpResponse
from .models import Pose

def home(request):

     return render(request, "home.html")


def showpose(request):
    # print(Pose)
    allPoses = Pose.objects.all()
    print(allPoses)
    context = {'allPoses': allPoses}
    return render(request, 'home.html',context)


# def name(request, pose_id):
#     return HttpResponse("You're looking at pose %s." % pose_id)

# def category(request, pose_id):
#     response = "You're looking at the results of pose %s."
#     return HttpResponse(response % pose_id)

# def email(request, pose_id):
#     return HttpResponse("You're inputting your email on pose %s." % pose_id) 

