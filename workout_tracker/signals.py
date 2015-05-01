from django.dispatch import Signal

notify = Signal(providing_args=[
    'recipient', 'actor', 'verb', 'action_object', 'target', 'description',
    'timestamp', 'level'
])
<<<<<<< HEAD
])
=======
])
>>>>>>> 19aadcc6cd0d639eea1575a96fc98e4202d7943e
