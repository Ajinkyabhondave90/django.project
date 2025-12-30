from django.shortcuts import render
from .models import comment
from .forms import commentform, userregistrationform
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request,'index.html')

def comments_list(request):
    comments = comment.objects.all().order_by('-created_at')
    return render(request, 'comment_list.html',{'comments':comments})

def comment_create(request):
    if request.method == "POST":
        form = commentform(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('comment_list')
    else:
        form = commentform()
    return render(request,'comment_form.html',{'form':form})


def comment_edit(request,comment_id):
    comment = get_object_or_404(comment, pk=comment_id, user = request.user)
    if request.method == "POST":
        form = commentform(request.POST, request.FILES,instance=comment)
        if form.IS_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')
    else:
        form = commentform(instance=comment)
    return render(request,'comment_form.html',{'form':form})

@login_required
def comment_delete(request, comment_id):
    get_object_or_404(comment, pk=comment_id, user = request.user)
    if request.method == "POST":
        comment.delete()
        return redirect('comment_list')
    return render(request,'comment_confirm_delete.html',{'comment': comment})


def resister(request):
    if request.method == 'POST':
        form = userregistrationform(request.form)
        if form.is_valid():
            User = form.save(commit=False)
            User.set_password(form.cleaned_data['password1'])
            User.save()
            login(request,User)
            return redirect('comments_list')
    else:
        form = userregistrationform()
        
    
    return render(request,'registration/regestration.html',{'form': form})



