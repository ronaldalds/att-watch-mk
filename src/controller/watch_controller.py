from src.service.watch_service import att_watch

def handle_start_watch(mk):
    response = att_watch(mk)
    return response