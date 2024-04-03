from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse
import os
import io
import uuid
import random
import string 
from datetime import datetime
from generator.models  import IncompleteGeneration


def edit(request):
    # Construct the absolute path to the image
    # img_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'image', 'certificate template.jpg')

    # # Open the image
    # img = Image.open(img_path)
     
    # # Initialize ImageDraw and ImageFont
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("arial.ttf",50) # You might want to use a custom font

    # #retrive the record using the id argument sent from the template
    # record=IncompleteGeneration.objects.get(id=id)
    
    # name = record.name
    # course = record.course
    # Duration = record.duration
    # email=record.email
    # uid= ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
  
    # current_date = datetime.now()
    # date = current_date.strftime('%B - %Y')
    # # Add text to the image
    # name_position = (882,339) 
    # course_position = (766,619) 
    # Duration_position = (922,816) 
    # uid_position=(17,1337) # Adjust the position as needed
    # color =(110,108,214)
    # date_position =(1132,1036)
    # uid_color=(0,0,0)
  
    # draw.text(name_position,text=name,font=font,fill=color)
    # draw.text(course_position,text=course,font=font,fill=color)
    # draw.text(Duration_position,text=Duration,font=font,fill=color)
    # draw.text(uid_position,text=str(uid),font=font,fill=color)
    # draw.text(date_position,text= str(date),font=font,fill=color)
  
    # img.save(f"static/certificates/{name}_img.png")


    # # Create an in-memory binary stream to store the image data
    # # img_byte_array = io.BytesIO()
    # # img.save(img_byte_array, format='PNG')

    # #saving the record in db
    # completed=CompletedGeneration(uid=str(uid),name=name,course=course,duration=Duration,email=email)
    # # Set the certificate field with the image data
    # # completed.certificate = img_byte_array.getvalue()  # Store the binary data directly
    # completed.save()
    # # img_byte_array.close()
    # #removing the record from IncompleteGeneration table
    # record.delete()
    # Return the modified image as a response
    return render(request,'certificate-template.html')