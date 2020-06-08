from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project,Profile,Review
from .forms import NewsLetterForm,RegistrationForm,ReviewForm,ProfileForm,ProjectForm
from django.contrib import messages
from .email import send_welcome_email
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you, {username}. Your account has been created')
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='/accounts/login/')
def welcome(request):
    all_projects = Project.fetch_all_images()
    form = NewsLetterForm()

    return render(request, 'index.html',{"all_images":all_projects,"letterForm":form})

#Ajax functionality
def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

def search_project(request):
    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "projects":searched_projects})

    else:
        message = "No search results yet!"
        return render (request, 'search.html', {"message": message})

def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{'profile':prof,'projects':projects})   

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'new_profile.html', {"form": form})   

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = current_user
            user_image.save()
        return redirect('index')
    else:
        form = ProjectForm()
    return render(request,"new_project.html",{"form":form})

# Project Serializer

class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
    
    def put(self, request, pk, format = None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors,
                            status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Profile Serializer

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)
    
    def put(self, request, pk, format = None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors,
                            status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)