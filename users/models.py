from django.db import models
from django.contrib.auth.models import AbstractUser
#from nodes import models as node_models
from django.apps import apps


# Custom User implementation containing all the user fields
class CustomUser(AbstractUser):
    MEMBER = '0'
    NODEADMIN = '1'
    GLOBALADMIN = '2'

    ROLES =(
        (MEMBER, 'Member'),
        (NODEADMIN, 'Node Admin'),
        (GLOBALADMIN, 'Global Admin')
    )

    # add additional fields in here
    IDNumber = models.IntegerField(default=0)

    # Node is a foreign key so field has to be filled by a node object.
    Node = models.ForeignKey('nodes.Node', null=True, on_delete=models.CASCADE)

    Role = models.CharField(default=0, choices=ROLES, max_length=20)

    # string function that returns the username when this class is printed.
    def __str__(self):
        return self.first_name+ " "+self.last_name
