from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectTracker
import plotly.figure_factory as ff
from plotly.figure_factory import create_gantt
import pandas as pd
import json, plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from django.http import JsonResponse
from django.http import HttpResponseRedirect


"""------------------------------------------------------------------------------------ 
Initialize specific gantt and ProjectTracker
---------------------------------------------------------------------------------------"""


def project_tracker(request):
    projects = ProjectTracker.objects.all()

    data = pd.DataFrame(
        {'Task': [project.projectId for project in projects],
         'Start': [project.sgate_date for project in projects],
         'Finish': [project.actual_rgate_date for project in projects]
         }
    )

    # Create Gantt chart using Plotly
    fig = ff.create_gantt(data, show_colorbar=True, index_col='Task', group_tasks=True)
    fig.update_layout(title_text='Project Gantt Chart', xaxis_title='Timeline', autosize=True)

    # Convert the figure to JSON
    gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'projects': projects,
        'gantt_chart_json': gantt_chart_json,
    }

    return render(request, 'tracker/project_tracker.html', context)

    
"""------------------------------------------------------------------------------------ 
Project info detail ->> All informations from admin + allows editing of actual dates
---------------------------------------------------------------------------------------"""


def project_info(request, pk):
    project = get_object_or_404(ProjectTracker, id=pk)

    # Assuming 'pk' is the project ID
    tasks = ProjectTracker.objects.filter(id=pk)

    data_rows = []

    for task in tasks:
        # Create unique 'Task' values for each event
        baseline_task=f'{task.projectId}-Latest Baseline'
        forecast_task=f'{task.projectId}-Latest Forecast'
        all_task=f'{task.projectId} - Overall'

        data_rows.append({'Task': task.projectId,
                          'Start': task.sgate_date,
                          'Finish': task.actual_sgate_date,
                          'Resource': 'S Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.agate_date,
                          'Finish': task.actual_agate_date,
                          'Resource': 'A Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.vgate_date,
                          'Finish': task.actual_vgate_date,
                          'Resource': 'V Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.rgate_date,
                          'Finish': task.actual_rgate_date,
                          'Resource': 'R Gate'})

        data_rows.append({'Task': all_task,
                          'Start': task.sgate_date,
                          'Finish': task.actual_rgate_date,
                          'Resource': 'Overall'})
        
        data_rows.append({'Task': baseline_task,
                          'Start': task.sgate_date,
                          'Finish': task.latesBase_date,
                          'Resource': 'Latest Baseline'})
        
        data_rows.append({'Task': forecast_task,
                          'Start': task.sgate_date,
                          'Finish': task.latesForecast_date,
                          'Resource': 'Latest Forecast'})

        
    colors = {
        'Latest Baseline': 'rgb(255, 0, 0)',  # Red for Latest Baseline
        'Latest Forecast': 'rgb(0, 0, 255)',  # Blue for Latest Forecast
        'Overall': 'rgb(255, 165, 0)',        # Strong Orange
        'S Gate': 'rgb(220, 0, 0)',            # Red
        'A Gate': 'rgb(0, 0, 255)',            # Blue
        'V Gate': 'rgb(148, 0, 211)',          # Violet
        'R Gate': 'rgb(0, 128, 0)'             # Dark Green
    }


    # Convert the list of dictionaries to a Pandas DataFrame
    data = pd.DataFrame(data_rows)


    # Create Gantt chart using Plotly
    fig = ff.create_gantt(data,colors=colors,  index_col='Resource', show_colorbar=True, group_tasks=True)
    fig.update_layout(title_text='Project Gantt Chart', xaxis_title='Timeline', autosize=True)

    # Convert the figure to JSON
    gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        
    context = {
        'project': project,
        'gantt_chart_json': gantt_chart_json,
    }



    return render(request, 'tracker/project_info.html', context)

"""------------------------------------------------------------------------------------ 
ABOUT SECTION VIEW
---------------------------------------------------------------------------------------"""

def about_view(request):
    return render(request, 'tracker/about.html')

"""------------------------------------------------------------------------------------ 
KPI section
---------------------------------------------------------------------------------------"""
def kpi_view(request):
    return render(request, 'tracker/kpi.html')

"""------------------------------------------------------------------------------------ 
General Gantt chart
---------------------------------------------------------------------------------------"""

def overall_gantt_chart(request):
    # Assuming 'projects' is a queryset of all projects
    projects = ProjectTracker.objects.all()

    # Filter projects based on request parameters (if any)
    project_name = request.GET.get('project_name')
    if project_name:
        projects = projects.filter(name=project_name)

    # Create a Pandas DataFrame for the overall Gantt chart
    data = pd.DataFrame({
        'Task': [project.name for project in projects],
        'Start': [project.sgate_date for project in projects],
        'Finish': [project.actual_rgate_date for project in projects]
    })

    # Create the overall Gantt chart using Plotly
    fig = create_gantt(
        data,
        show_colorbar=True,
        index_col='Task',
        group_tasks=True
    )
    
    fig.update_layout(
        title_text='Gantt Chart',
        xaxis_title='Timeline',
        autosize=True,
    )

    # Convert the figure to JSON
    overall_gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'overall_gantt_chart_json': overall_gantt_chart_json,
    }

    return render(request, 'tracker/gantt.html', context)
