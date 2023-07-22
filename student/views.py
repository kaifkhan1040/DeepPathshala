from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from student.models import *
from main.models import Teacher
from django.shortcuts import redirect

# Create your views here.
def home(request):
    course = Course.objects.all()
    return render(request,'student/courses.html',{'course':course})


@login_required(login_url='/user/login/')
def enroll_user(request,id):
    print('enroll')
    mucourse=Course.objects.get(id=id)
    print(request.method)
    enrol_user=CourseEnroll.objects.create(user=request.user,course=mucourse)
    enrol_user.save()
    print('saved')
    redirect_url='/student/course_single/'+str(id)
    return redirect(redirect_url)
    



@login_required(login_url='/user/login/')
def course_single(request,id):
    mucourse=Course.objects.get(id=id)
    course_id=id
    topic = Topic.objects.filter(course=mucourse)
    course_enroll=CourseEnroll.objects.filter(course=id , user=request.user)
    print(mucourse,topic)
    listact = []
    actid=''
    for i in topic:
        act = Activity.objects.filter(course=mucourse, topic=i)
        listact.append(act)
        print(listact)
        break
    for i in listact:
        for j in i:
            actid=j.id
    course = Course.objects.all()[:3]
    print(actid,'asdasd')

    return render(request,'student/course-single.html',{'mucourse':mucourse,'course':course,'actid':actid,'course_id':course_id,'course_enroll':course_enroll})

@login_required(login_url='/user/login/')
def play(request,id):
    activity=Activity.objects.get(id=id)
    course=activity.course
    print('act',activity,'course is',course)
    topic=Topic.objects.filter(course=course)
    listact=[]
    for i in topic:
        act=Activity.objects.filter(course=course,topic=i)
        listact.append(act)
    topiclist=[]
    topiclist.append(activity.topic)
    print(request.method)
    print(request.user)
    question_ans=Question.objects.filter(course=course)
    if request.method=='POST':
        question=request.POST.get('question')
        if question!='' and question !=None:
            QNA=Question(question=question,username=request.user,course=course)
            QNA.save()
    return render(request,'student/play.html',{'course':course,'topic':topic,'listact':listact,'activity':activity,'topiclist':topiclist,'question_ans':question_ans})

