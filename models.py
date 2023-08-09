from django.db import models

class graphEnquiry(models.Model):
    prefrence = models.CharField(max_length=50,null=False)
    # x_axis = models.CharField(max_length=50)
    # y_axis = models.CharField(max_length=50)
    html_data = models.TextField()

    def __str__(self):
        return self.prefrence
