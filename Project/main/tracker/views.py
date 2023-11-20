from django.shortcuts import render, get_object_or_404
from .models import ProjectTracker
import plotly.figure_factory as ff
from plotly.figure_factory import create_gantt
import pandas as pd
import json, plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

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
    fig.update_layout(title_text='Project Gantt Chart', xaxis_title='Timeline')

    # Convert the figure to JSON
    gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'projects': projects,
        'gantt_chart_json': gantt_chart_json,
    }

    return render(request, 'tracker/project_tracker.html', context)

    
def project_info(request, pk):
    project = get_object_or_404(ProjectTracker, id=pk)

    # Assuming 'pk' is the project ID
    tasks = ProjectTracker.objects.filter(id=pk)

    data_rows = []

    for task in tasks:
       
        data_rows.append({'Task': task.projectId,
                          'Start': task.actual_sgate_date,
                          'Finish': task.actual_agate_date,
                          'Event': 'S Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.actual_agate_date,
                          'Finish': task.actual_agate_date,
                          'Event': 'A Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.actual_vgate_date,
                          'Finish': task.actual_vgate_date,
                          'Event': 'V Gate'})
        
        data_rows.append({'Task': task.projectId,
                          'Start': task.rgate_date,
                          'Finish': task.actual_rgate_date,
                          'Event': 'R Gate'})


def project_info(request, pk):
    project = get_object_or_404(ProjectTracker, id=pk)

    # Assuming 'pk' is the project ID
    tasks = ProjectTracker.objects.filter(id=pk)

    data_rows = []

    for task in tasks:
        # Create unique 'Task' values for each event
        all_task=f'{task.projectId} - Overall'
        s_gate_task = f'{task.projectId} - S Gate'
        a_gate_task = f'{task.projectId} - A Gate'
        v_gate_task = f'{task.projectId} - V Gate'
        r_gate_task = f'{task.projectId} - R Gate'

        data_rows.append({'Task': all_task,
                          'Start': task.sgate_date,
                          'Finish': task.actual_rgate_date,
                          'Event': 'Overall duration'})
        
        data_rows.append({'Task': s_gate_task,
                          'Start': task.sgate_date,
                          'Finish': task.actual_sgate_date,
                          'Event': 'S Gate'})
        
        data_rows.append({'Task': a_gate_task,
                          'Start': task.agate_date,
                          'Finish': task.actual_agate_date,
                          'Event': 'A Gate'})
        
        data_rows.append({'Task': v_gate_task,
                          'Start': task.vgate_date,
                          'Finish': task.actual_vgate_date,
                          'Event': 'V Gate'})
        
        data_rows.append({'Task': r_gate_task,
                          'Start': task.rgate_date,
                          'Finish': task.actual_rgate_date,
                          'Event': 'R Gate'})

    # Convert the list of dictionaries to a Pandas DataFrame
    data = pd.DataFrame(data_rows)

    # Create Gantt chart using Plotly
    fig = ff.create_gantt(data, index_col='Task', show_colorbar=True, group_tasks=True)
    fig.update_layout(title_text='Project Gantt Chart', xaxis_title='Timeline')

    # Convert the figure to JSON
    gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'project': project,
        'gantt_chart_json': gantt_chart_json,
    }

    return render(request, 'tracker/project_info.html', context)

def about_view(request):
    return render(request, 'tracker/about.html')



def overall_gantt_chart(request):
    # Assuming 'projects' is a queryset of all projects
    projects = ProjectTracker.objects.all()

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
        title_text='Overall Gantt Chart',
        xaxis_title='Timeline',
    )

    # Convert the figure to JSON
    overall_gantt_chart_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        'overall_gantt_chart_json': overall_gantt_chart_json,
    }

    return render(request, 'tracker/gantt.html', context)