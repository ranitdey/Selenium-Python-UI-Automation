class UIException(Exception):
    def __init__(self, *args, **kwargs):
        default_message = 'UI Exception occurred'
        if not (args or kwargs):
            args = (default_message,)
        super().__init__(*args, **kwargs)

