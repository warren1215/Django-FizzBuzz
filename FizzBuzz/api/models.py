from django.db import models

class FizzModel(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length = 200)
    creation_date = models.DateTimeField(auto_now_add = True)
    message = models.CharField(max_length = 200)

    def __str__(self):
        return self.message
