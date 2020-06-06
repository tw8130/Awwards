from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Review
from .forms import NewsLetterForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    all_projects = Project.fetch_all_images()
    form = NewsLetterForm()

    return render(request, 'index.html',{"all_images":all_projects,"letterForm":form})

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

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})

