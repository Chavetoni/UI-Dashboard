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
            # Add mock timeline events and documents for project details page
            if project_id == 1:
                project['teamMembers'] = [
                    {"id": 1, "name": "Nestor A.", "role": "Geotechnical Project Manager"},
                    {"id": 2, "name": "Ron L.", "role": "Geotechnical Project Manager"},
                    {"id": 3, "name": "Daniel G.", "role": "Geotechnical Project Manager"},
                    {"id": 4, "name": "Amos E.", "role": "Geotechnical Department Manager"}
                ]
                project['timelineEvents'] = [
                    {"id": 1, "date": "Jan 15, 2025", "title": "Project Kickoff", "description": "Initial client meeting and site overview.", "status": "Completed"},
                    {"id": 2, "date": "Feb 5, 2025", "title": "Site Survey", "description": "Comprehensive site survey and sample collection.", "status": "Completed"},
                    {"id": 3, "date": "Mar 1, 2025", "title": "Lab Analysis", "description": "Soil testing and analysis of site samples.", "status": "Completed"},
                    {"id": 4, "date": "Mar 28, 2025", "title": "Preliminary Report", "description": "Initial findings and recommendations drafted.", "status": "In Progress"},
                    {"id": 5, "date": "Apr 10, 2025", "title": "Foundation Analysis", "description": "Detailed foundation requirements and specifications.", "status": "Upcoming"},
                    {"id": 6, "date": "Apr 30, 2025", "title": "Final Report", "description": "Final report submission and client presentation.", "status": "Upcoming"}
                ]
                project['documents'] = [
                    {"id": 1, "name": "Final Report Project.pdf", "uploadDate": "Mar 28, 2025", "size": "4.8 MB"},
                    {"id": 2, "name": "Final Report Project.docx", "uploadDate": "Mar 28, 2025", "size": "2.3 MB"}
                ]
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
    user_projects = MOCK_PROJECTS  # Get the list of projects
    active_project_count = sum(1 for p in user_projects if p['status'] not in ['Completed', 'Cancelled'])

    context = {
        'projects': user_projects,
        'active_count': active_project_count,
        'view_name': 'dashboard',
    }

    # Update to use the tailwind template
    return render(request, 'client_portal/dashboard.html', context)



@login_required
def project_detail(request, project_id):
    """Displays details for a specific project."""
    project = _get_project_by_id(project_id)  # Using mock data helper

    if project is None:
        messages.warning(request, f"Project with ID {project_id} not found.")
        return redirect('client_portal:dashboard')  # Use correct namespace if defined

    context = {
        'project': project,
        'view_name': 'project_detail'
    }
    # Update to use the tailwind template
    return render(request, 'client_portal/project_detail.html', context)