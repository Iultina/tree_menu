def menu_processor(request):
    path = request.path
    return {'current_path': path}