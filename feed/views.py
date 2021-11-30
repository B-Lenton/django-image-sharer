from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView

from .forms import  PostForm
from .models import Post

# check out www.ccbv.co.uk for guidance/documentation on everything Class-Based Views

class HomePageView(TemplateView):
    # look for a file named home.html
    template_name = "home.html"

    #creating variable for dynamic content in html pages
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all of our posts (from models.py) & order them by id descending (recency)
        context["posts"] = Post.objects.all().order_by("-id")
        return context

# if user goes to a particular detail view, fetch that particular image/post for us - Django manages the database for us
class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

# allows users to post to the page / upload things
class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    # if image is uploaded successfuly, send user to home page
    success_url = "/"

    # tells django to use the dispatch method (found in the online docs about the messages framework)
    def dispatch(self, request, *args, **kwargs):
        # this runs before the below method, so now form_valid can access the 'request' object
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    # return a Http response to the success url (i.e. add image to home page)
    def form_valid(self, form):
        new_object = Post.objects.create(
            # returns the text and image of the PostForm from forms.py
            text = form.cleaned_data["text"],
            image = form.cleaned_data["image"]
        )
        # see .../contrib/messages/ in djangoproject docs
        messages.add_message(self.request, messages.SUCCESS, "Your post was uploaded successfully")
        return super().form_valid(form)
