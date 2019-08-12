from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


@login_required
def join_neighbourhood(request, neigh_id):
    hood = get_object_or_404(Neighbourhood, pk=neigh_id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect(neighbourhoods)


@login_required
def leave_neighbourhood(request, neigh_id):
    hood = get_object_or_404(Neighbourhood, pk=neigh_id)
    if request.user.profile.neighbourhood == hood:
        request.user.profile.neighbourhood=None
        request.user.profile.save()
    return redirect(neighbourhoods)


@login_required
def delete_neighbourhood(request, neigh_id):
    hood = get_object_or_404(request.user.profile.hoods, pk=neigh_id)
    for member in hood.people.all():
        member.neighbourhood = None
        member.save()
    request.user.profile.hoods.filter(pk=neigh_id).delete()
    return redirect(myprofile)


@login_required
def create_neighbourhood(request):
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.admin = request.user.profile
            request.user.profile.save()
            hood.save()
            return redirect(neighbourhoods)
    else:
        hood_form = HoodForm()
    return render(request, 'newneighbourhood.html', locals())
