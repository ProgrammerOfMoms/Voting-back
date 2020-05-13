from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    votes = models.IntegerField(default=0)
    
    def upvote(self):
        self.votes = self.votes + 1

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['id']

class Voter(models.Model):
    idVK = models.CharField(max_length=20, default=-1)
    firstName = models.CharField(max_length=20, default="unknown")
    lastName = models.CharField(max_length=20, default="unknown")
    is_voted = models.BooleanField(default=False, null=True)
    vote = models.ForeignKey(Candidate, on_delete = models.CASCADE, null=True)