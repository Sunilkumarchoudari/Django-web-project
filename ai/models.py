from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


OPTIMIZERS_CHOICES = (
    ('notset','Unknown'),
    ('Adam','Adam'),
    ('Mini Batch Gradient Descent','Mini Batch Gradient Descent'),
    ('RMSprop','RMSprop'),
    ('Stochastic Gradient Descent','Stochastic Gradient Descent'),
)
LOSSES_CHOICES = (
    ('notset','Unknown'),
    ('Mean Squared Error','Mean Squared Error'),
    ('Mean Absolute Error','Mean Absolute Error'),
    ('Categorical Crossentropy','Categorical Crossentropy'),
    ('Sparse Categorical Crossentropy','Sparse Categorical Crossentropy'),
    ('Binary Crossentropy','Binary Crossentropy'),
)
TESTING_TYPE_CHOICES = (
    ('notset','Unknown'),
    ('drawing_test','Drawing Test'),
    ('image_test','Image Test'),
    ('audio_test','Audio Test'),
    ('video_test','Video Test'),
    ('webcam_test','Webcam Test'),
    ('microphone_test','Microphone Test'),
    ('text_area_test','Text Area Test'),
)

CATEGORIES = (
    ('ns','Unknown'),
    ('ml','Machine Learning'),
    ('dl','Deep Learning'),
)



import os
def get_upload_path(instance, filename):
    return os.path.join(str(instance.project_title), filename)


# Create your models here.
class project(models.Model):
    project_title = models.CharField(max_length=64,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    project_category = models.CharField(max_length=3,choices=CATEGORIES,default='notset')

    working_model_summary_image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)
    working_model_optimizer = models.CharField(max_length=32,choices=OPTIMIZERS_CHOICES,default='notset',blank=True,null=True)
    working_model_learning_rate = models.DecimalField(max_digits=8,decimal_places=7,validators=[MinValueValidator(0)])
    working_model_loss = models.CharField(max_length=32,choices=LOSSES_CHOICES,default='notset',blank=True,null=True)
    working_model_callbacks = models.CharField(max_length=128,blank=True,null=True)
    working_model_dropout_rates = models.CharField(max_length=128,blank=True,null=True)

    weights_only_link = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    model_only_link = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    model_with_weights_link = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    output_classes = models.FileField(upload_to=get_upload_path,blank=True,null=True)

    data_source_link = models.URLField()
    data_source = models.CharField(max_length=64)
    data_file_type = models.CharField(max_length=32)
    category = models.CharField(max_length=64)
    training_samples = models.CharField(max_length=64)
    valid_samples = models.CharField(max_length=64)
    testing_samples = models.CharField(max_length=64)
    dimentions = models.CharField(max_length=64)

    model_preprocessing_text = models.TextField()
    preprocessing_code = models.TextField(blank=True,null=True)
    model_choosing_text = models.TextField()
    initial_model_image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)
    training_model_text = models.TextField()
    training_model_image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)
    model_testing_text = models.TextField()
    model_testing_image = models.ImageField(upload_to=get_upload_path,blank=True,null=True)
    model_tuning_text = models.TextField()
    model_deploy_text = models.TextField()

    model_training_loss = models.DecimalField(max_digits=7,decimal_places=6,validators=[MinValueValidator(-1),MaxValueValidator(100)])
    model_training_acc = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(-1),MaxValueValidator(100)])
    model_valid_loss = models.DecimalField(max_digits=7,decimal_places=6,validators=[MinValueValidator(-1),MaxValueValidator(100)],blank=True,null=True)
    model_valid_acc = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(-1),MaxValueValidator(100)],blank=True,null=True)
    model_testing_loss = models.DecimalField(max_digits=7,decimal_places=6,validators=[MinValueValidator(-1),MaxValueValidator(100)],blank=True,null=True)
    model_testing_acc = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(-1),MaxValueValidator(100)],blank=True,null=True)

    how_it_works = models.TextField()
    testing_type = models.CharField(max_length=32,choices=TESTING_TYPE_CHOICES)
    classes = models.DecimalField(max_digits=10,decimal_places=0,default=0,validators=[MinValueValidator(0),MaxValueValidator(100)],blank=True,null=True)

    def __str__(self):
        return self.project_title



class restore_project(models.Model):
    File = models.FileField(upload_to='restore_files')
    def __str__(self):
        return self.File.name
