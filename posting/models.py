from django.db import models


 
class PostProject(models.Model):
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='user')
    nom_projet = models.CharField(max_length=100, blank=False, null=False)
    epic_coder = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    prix_premiere = models.IntegerField(blank=False, null=False)
    prix_derniere = models.IntegerField(blank=False, null=False)
    description_projet = models.TextField(blank=False, null=False)
    cacher = models.BooleanField(default=False)

    updated_project = models.DateTimeField(auto_now=True)
    created_project = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("accounts.Account", blank=True, related_name='likes_post_projects')
    viewers_project = models.ManyToManyField("accounts.Account", blank=True, related_name='viewers_project')

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_project']

    def __str__(self):
        return self.nom_projet

class PostJobs(models.Model):
    STATUS_CHOICES = (
        (1, 'Select Type Work'),
        ('Hourly', 'Hourly'),
        ('Part time', 'Part time'),
        ('Full time', 'Full time'),
    )
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name='job')
    name_jobs = models.CharField(max_length=100, blank=False, null=False)
    type_work_job = models.CharField(choices=STATUS_CHOICES, max_length=100, blank=False, null=False, default=1)
    epic_coder = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    prix = models.IntegerField(blank=False, null=False)
    description_job = models.TextField(blank=False, null=False)
    cacher = models.BooleanField(default=False)

    updated_job = models.DateTimeField(auto_now=True)
    created_job = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField("accounts.Account", blank=True, related_name='likes_post_jobs')
    viewers_job = models.ManyToManyField("accounts.Account", blank=True, related_name='viewers_job')

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-created_job']

    def __str__(self):
        return str(self.user)
