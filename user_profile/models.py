from django.db import models
 
class Experience_user(models.Model):
    experience_user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    experince_title = models.CharField(max_length=100, null=True, blank=True)
    experince_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.experince_title if self.experince_title else ''

