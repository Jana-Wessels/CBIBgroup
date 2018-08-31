from django.db import models

# Node implementation containing all the node fields
class Node(models.Model):
    NodeID = models.CharField(default=None,max_length=10, null=True, blank=True,)
    Name = models.CharField(default=' ', max_length=200)
    Location = models.CharField(default=' ', max_length=200)
    Description = models.TextField(default=' ', max_length=10000)

    # string function that returns the node name when this class is printed.
    def __str__(self):
        return self.Name



