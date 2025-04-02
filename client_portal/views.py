from django.shortcuts import render

# Create your views here.
# portal/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

# --- Mock Data (Same as before, place it here or import from another file) ---
# In reality, you'd fetch this from your other Django API/DB source
MOCK_PROJECTS = [
    # ... (Copy the MOCK_PROJECTS list from the Flask example here) ...
     {
        "id": 1, "name": "7 Brew in San Antonio", "status": "In Progress", "progress": 65, "deadline": "May 15, 2025", "lastUpdated": "Mar 28, 2025",
        "description": "Geotechnical analysis...", "client": "Howard C.", "startDate": "Jan 15, 2025", "location": "San Antonio, TX", "teamMembers": [], "timelineEvents": [], "documents": []
     },
     {
        "id": 2, "name": "7 Brew in Austin", "status": "Planning Phase", "progress": 25, "deadline": "July 30, 2025", "lastUpdated": "Mar 25, 2025",
        "description": "Site assessment...", "client": "Jane D.", "startDate": "Feb 01, 2025", "location": "Austin, TX", "teamMembers": [], "timelineEvents": [], "documents": []
     },
     {
        "id": 3, "name": "7 Brew in Houston", "status": "On Hold", "progress": 40, "deadline": "June 10, 2025", "lastUpdated": "Mar 20, 2025",
        "description": "Project on hold...", "client": "Howard C.", "startDate": "Feb 15, 2025", "location": "Houston, TX", "teamMembers": [], "timelineEvents": [], "documents": []
     }
]


def _get_project_by_id(project_id):
    """Helper function to get a project by its ID."""
    for project in MOCK_PROJECTS:
        if project['id'] == project_id:
            return project
    return None

def index(request):
    if request.user.is_authenticated:
        return redirect('client_portal:dashboard')
    else:
        return redirect('client_portal:login')
    
@login_required
def dashboard(request):
     # Fetch projects relevant to request.user if possible, otherwise use mock
    user_projects = MOCK_PROJECTS # Get the list of projects
    active_project_count = sum(1 for p in user_projects if p['status'] not in ['Completed', 'Cancelled'])

    context = {
        # 'project': project, # Remove single project
        'projects': user_projects, # Add list of projects
        'active_count': active_project_count, # Add count
        'view_name': 'dashboard', # Correct view name
    }

    # return render(request, 'portal/project_detail.html', context) # Incorrect template
    return render(request, 'portal/dashboard.html', context) # CORRECTED: Render dashboard template

@login_required
def project_detail(request, project_id):
    """Displays details for a specific project."""
    # project = get_object_or_404(ProjectModel, pk=project_id) # How you'd do it with models
    project = _get_project_by_id(project_id) # Using mock data helper

    if project is None:
        messages.warning(request, f"Project with ID {project_id} not found.")
        return redirect('client_portal:dashboard') # Use correct namespace if defined

    context = {
        'project': project,
        'view_name': 'project_detail'
    }
    return render(request, 'client_portal/project_detail.html', context) 
