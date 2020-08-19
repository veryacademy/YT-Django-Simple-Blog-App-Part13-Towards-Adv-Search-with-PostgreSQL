""" def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []
    query = Q()

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            if q is not None:
                query &= Q(title__contains=q)

            results = Post.objects.filter(query)

    return render(request, 'blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results})
 """

# Task1

""" 
def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Post.objects.filter(title__search=q)

    return render(request, 'blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results})
 """
# Need django.contrib.postgres

# Task2


""" def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Post.objects.annotate(search=SearchVector(
                'title', 'content'),).filter(search=q)

    return render(request, 'blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results}) """

# from django.contrib.postgres.search import SearchVector

# Task3


""" def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            results = Post.objects.annotate(search=SearchVector(
                'title', 'content'),).filter(search=SearchQuery(q))

    return render(request, 'blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results})
 """
# from django.contrib.postgres.search import SearchQuery

# Task4


""" def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

           # step 1 vector = SearchVector('title', 'content')
           # rank = SearchRank(vector, query, weights=[0.2, 0.4, 0.6, 0.8])
            vector = SearchVector('title', weight='A') + \
                SearchVector('content', weight='B')
            query = SearchQuery(q)

            results = Post.objects.annotate(
                rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')

    return render(request, 'blog/search.html',
                  {'form': form,
                   'q': q,
                   'results': results}) """

# from django.contrib.postgres.search import SearchRank
