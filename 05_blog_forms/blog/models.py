from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE
from django.core.validators import RegexValidator


class Blog(Model):
    # Validator to allow only alphabetic characters and spaces
    title = CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z ]*$',
                message='Title must contain only alphabetic characters and spaces.',
                code='invalid_title'
            )
        ]
    )
    body = TextField()
    author = ForeignKey('auth.User', on_delete=CASCADE)

    def __str__(self):
        return self.title
