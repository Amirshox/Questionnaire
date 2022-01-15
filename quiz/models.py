from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Poll(BaseModel):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='polls')

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-modified_date',)


class Question(BaseModel):
    TEXT = 'TEXT'
    SINGLE = 'SINGLE'
    MULTIPLE = 'MULTIPLE'
    TYPE_OF_QUESTION = (
        (TEXT, TEXT),
        (SINGLE, SINGLE),
        (MULTIPLE, MULTIPLE)
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')

    text = models.TextField()
    type = models.CharField(max_length=8, choices=TYPE_OF_QUESTION)

    def __str__(self):
        return self.poll

    class Meta:
        ordering = ('created_date',)


class Option(BaseModel):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')

    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.questions_id

    class Meta:
        ordering = ('created_date',)


class Answer(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='answers')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    options = models.ManyToManyField(Option, related_name='answers', default=None)

    text_answer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.users.username

    class Meta:
        ordering = ('created_date',)
