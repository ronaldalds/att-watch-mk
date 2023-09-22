from src.service.watch_service import att_watch

running = False

def handle_start_watch(mk):
    global running
    if not running:
        running = True
        response = att_watch(mk)
        running = False
        return response
    else:
        return f"Att Watch MK{mk:02} em execução."
