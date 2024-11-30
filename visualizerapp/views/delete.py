from django.shortcuts import redirect, get_object_or_404, render

def delete_line(request, line_id):
    if request.method == 'POST':
        lines = request.session.get('lines', [])
        lines = [line for idx, line in enumerate(lines) if idx != int(line_id)]
        request.session['lines'] = lines
        request.session.modified = True
        return redirect('plotter')


def delete_point(request, point_id):
    if request.method == 'POST':
        points = request.session.get('points', [])
        points = [point for idx, point in enumerate(points) if idx != int(point_id)]
        request.session['points'] = points
        request.session.modified = True
        return redirect('plotter')


def delete_function(request, function_id):
    if request.method == 'POST':
        functions = request.session.get('functions', [])
        functions = [function for idx, function in enumerate(functions) if idx != int(function_id)]
        request.session['functions'] = functions
        request.session.modified = True
        return redirect('plotter')

