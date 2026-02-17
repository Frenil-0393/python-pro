from django.shortcuts import render

from common.decorators import role_required


@role_required("fan")
def dashboard(request):
	return render(request, "fan/dashboard.html", {"user_name": request.user.first_name or "Fan"})
