import uuid
from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile, CustomUser
from cloudinary.models import CloudinaryField

# Create your models here.

TIME_CHOICES = (
    ("9am to 12pm", "9am to 12pm"),
    ("12pm to 3pm", "12pm to 3pm"),
    ("3pm to 6pm", "3pm to 6pm"),
)

# Create your models here.
class Studio(models.Model):
    """
    Django database model for studio spaces
    """
    studio_id = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.studio_id
  

class StudioBooking(models.Model):
    """
    Django database model for available studios
    """

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=12, choices=TIME_CHOICES, default="9am to 12pm")
    created_on = models.DateTimeField(auto_now=True)

    def _generate_booking_id(self):
        """
        Generate a random, unique booking id using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        # formatted_start_time = self.start_time.strftime('%Y-%m-%d %H:%M')
        return f"{self.booking_id} | {self.artist.username} | {self.studio} | {self.booking_date} at {self.booking_time}"

        # ^this is where I hit a problem trying to make a booking^
        # when I change {self.artist.username} to {self.artist.user} there seems to be some problem occurring in the view
        # I need to copy the booking template ver batim and reverse engineer where my view runs into a problem