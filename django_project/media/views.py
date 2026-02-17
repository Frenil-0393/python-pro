from django.shortcuts import render

from common.decorators import role_required


@role_required("media")
def dashboard(request):
	return render(request, "media/dashboard.html", {"user_name": request.user.first_name or "Media"})
