from audioop import reverse
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
import random
 



class Resume(models.Model):
    BLACK = 'Black'
    WHITE = 'White'
    COLOURED = 'Coloured'
    INDIAN = 'Indian'
    CHINESE = 'Chinese'
    
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    MARRIED = 'Married'
    SINGLE = 'Single'
    WIDOWED = 'Widowed'
    DIVORCED = 'Divorced'
    
    GAUTENG = 'Gauteng'
    MPUMALANGA = 'Mpumalanga'
    FREE_STATE = 'Free-state'
    NORTH_WEST = 'North-west'
    LIMPOPO = 'Limpopo' 
    WESTER_CAPE = 'Western-cape'
    NOTHERN_CAPE = 'Nothern-cape'
    EASTERN_CAPE = 'Eastern-cape'
    KWAZULU_NATAL = 'Kwazulu-natal'
    
    ETHINIC_CHOICES = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (COLOURED, 'Coloured'),
        (INDIAN, 'Indian'),
        (CHINESE, 'Chinese'),
    ]
    
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    MARITAL_STATUS =[
        (MARRIED,'Married'),
        (SINGLE,'Single'),
        (WIDOWED, 'Widowed'),
        (DIVORCED, 'Divorced')
    ]
    
    PROVINCE_CHOICES = [
        (GAUTENG, 'Gauteng'),
        (MPUMALANGA, 'Mpumalanga'),
        (FREE_STATE, 'Free-state'),
        (NORTH_WEST, 'North-west'),
        (LIMPOPO, 'Limpopo' ),
        (WESTER_CAPE, 'Western-cape'),
        (NOTHERN_CAPE, 'Nothern-cape'),
        (EASTERN_CAPE, 'Eastern-cape'),
        (KWAZULU_NATAL, 'Kwazulu-natal')
        
    ]
    
    IMAGES = [
        'person1.jpg', 'person2.jpg', 'person3.jpg', 
        'person4.jpg', 'person5.jpg', 'person6.jpg', 
    ]
    
    user = models.OneToOneField(User, on_delete = models.CASCADE) #on_delete = models.CASCADE, if user is deleted their profile will be deleted
    uniqueId = models.CharField(null=True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_images') #upload_to = 'profile_images, profile image gets uploaded to a folder you define. You need to have the default.jpg in the uploads folder so that it can be used
    ethnicity = models.CharField(choices= ETHINIC_CHOICES, default=BLACK )
    email_confirmed =  models.BooleanField(default=False) #This will be used to conifrm people's email later
    date_birth = models.DateField()
    sex = models.CharField(choices=SEX_CHOICES, default= OTHER)
    marital_status = models.CharField(choices= MARITAL_STATUS, default= SINGLE)
    addressLine1 = models.CharField(null = True)
    addressLine2 = models.CharField(null= True)
    suburb = models.CharField(null= True)
    city = models.CharField(null=True)
    province = models.CharField(choices=PROVINCE_CHOICES, default=GAUTENG)
    phoneNumber = models.CharField(null=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True) #slug is used for detail page navigation. So suppose you make a profile on linkedin, in the url you get the person's name etc after the linkedin.com/...  . The ... here will be seprate slug for each url which we are creating 
    date_created = models.DateTimeField(default=timezone.now) #good to know information
    last_updated = models.DateTimeField() #good to know information
    cover_letter = models.FileField(upload_to='resumes') # attach a over letter and information
    cv = models.FileField(upload_to='resumes')
    
    
    def _str_(self):
        return '{} {} {}'.format(self.first_name,self.user.last_name, self.uniqueId)
    
    
    def get_absolute_url(self):
        return reverse('resume-detail', kwargs ={'slug' : self.slug}) #
    
    
    def save(self, *args, **kwargs):
        #Creating a unique Identifier for the resume(useful for other thigns in future)
        if self.uniqueId is None:
            self.uniqueId = 'user-'+str(uuid4()).split('-')[0] #this user Id will only be added to user instance once as first time clicked the save function it saves it as user-... but next tiime uniqueId wont be NULL so the if block won't work
        
        #Creating the SlugField for the URL - to detailed page
        #first_name = Skolo, last_name=Online, uniquesId=hdhfueu: 'Skolo-Online-hdhfueu:'
        if self.slug is None:
            self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))
        
        #assign a default profile image
        if self.image == 'default.jpg':
            self.image = random.choice(self.IMAGES) #randomely choose between IMAGES folder images and assign it here
            
        #keep track of every everytime someone uploads the resume, everytime the instance is saved - this should update
        self.last_updated = timezone.now #everytime you save this instance the time gets updated
        
        
        super(Resume, self).save(*args, **kwargs)
        
        
       
            
    
    
