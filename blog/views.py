from django.shortcuts import render

# Creat some junk and stuff.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
