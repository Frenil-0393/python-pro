from django.shortcuts import render

from common.decorators import role_required


@role_required("organizer")
def dashboard(request):
	return render(request, "organizer/dashboard.html", {"user_name": request.user.first_name or "Organizer"})
