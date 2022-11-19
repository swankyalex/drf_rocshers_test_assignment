from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Station(models.Model):
    """Model for space-stations"""

    RUNNING = "Running"
    BROKEN = "Broken"

    STATE_CHOICES = (
        (RUNNING, "running"),
        (BROKEN, "broken"),
    )

    name = models.CharField(max_length=128)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RUNNING)
    time_create = models.DateTimeField(auto_now_add=True)
    time_broke = models.DateTimeField(null=True, blank=True)
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    z = models.IntegerField(default=100)

    # redefine save method for checking if station is broken
    def save(self, *args, **kwargs):
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            self.state = self.BROKEN
            if not self.time_broke:
                self.time_broke = datetime.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Pointer(models.Model):
    """Model for pointers to control stations"""

    AXIS_X = "x"
    AXIS_Y = "y"
    AXIS_Z = "z"

    AXIS_CHOICES = (
        (AXIS_X, "x"),
        (AXIS_Y, "y"),
        (AXIS_Z, "z"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    axis = models.CharField(max_length=1, choices=AXIS_CHOICES)
    distance = models.IntegerField()

    def __str__(self):
        return f"By {self.user} on {self.axis} axis for {self.distance} points"
