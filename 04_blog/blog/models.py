from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE,IntegerField


class Blog(Model):
    title = CharField(max_length=100)
    body = TextField()
    author = ForeignKey('auth.User', on_delete=CASCADE) 

    def __str__(self):
        return self.title
