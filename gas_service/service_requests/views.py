from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('dashboard')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'service_requests/dashboard.html', {'requests': requests})



def view_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk) 
    return render(request, 'service_requests/view_request.html', {'request_obj': service_request})



def register(request):
    return render(request, 'register.html')