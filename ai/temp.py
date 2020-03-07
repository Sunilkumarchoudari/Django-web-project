from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
from .models import project,restore_project
from django.forms.models import model_to_dict
import shutil,os,json
from django.conf import settings
from django.core import serializers
from PIL import Image
import numpy as np
import re
import base64
import random
import string
from keras.models import load_model
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
import cv2


# Create your views here.
def get_project(request,id):
    c = get_object_or_404(project,id=id)
    context = {
        'title':f"AI PROJECTS - {c.project_title}",
        'id':c.id,
        'project_title' : c.project_title,
        'working_model_summary_image' : c.working_model_summary_image,
        'working_model_optimizer' : c.working_model_optimizer,
        'working_model_learning_rate' : c.working_model_learning_rate,
        'working_model_loss' : c.working_model_loss,
        'working_model_callbacks' : c.working_model_callbacks,
        'working_model_dropout_rates' : c.working_model_dropout_rates,

        'weights_only_link' : c.weights_only_link,
        'model_only_link' : c.model_only_link,
        'model_with_weights_link': c.model_with_weights_link,

        'data_source_link':c.data_source_link,
        'data_source':c.data_source,
        'data_file_type':c.data_file_type,
        'category':c.category,
        'training_samples':c.training_samples,
        'valid_samples':c.valid_samples,
        'testing_samples':c.testing_samples,
        'dimentions':c.dimentions,
        'model_preprocessing_text' : c.model_preprocessing_text.split('\n'),
        'preprocessing_code' : c.preprocessing_code.split('\n'),
        'model_choosing_text' : c.model_choosing_text.split('\n'),
        'initial_model_image' : c.initial_model_image,
        'training_model_text' :c.training_model_text.split('\n'),
        'training_model_image' : c.training_model_image,
        'model_testing_text' : c.model_testing_text.split('\n'),
        'model_testing_image' : c.model_testing_image,
        'model_tuning_text' : c.model_tuning_text.split('\n'),
        'model_deploy_text' : c.model_deploy_text.split('\n'),
    }
    return render(request,f'ai/{c.id}.html',context = context)
