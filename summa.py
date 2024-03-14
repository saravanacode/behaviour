import cv2
import numpy as np
import face_recognition
from ultralytics import YOLO
from sort import *
import tensorflow as tf
from tensorflow.keras.models import load_model
import cvzone
import math
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import base64
from pymongo import MongoClient
import os
from bson.binary import Binary
import tkinter as tk
from tkinter import filedialog


#client = MongoClient('mongodb+srv://ganeshyadharth:AbleLyf@students.jbrazv2.mongodb.net/?retryWrites=true&w=majority')
#mongo_db = client["attendance"]


#client = MongoClient('mongodb+srv://ganeshyadharth:AbleLyf@students.jbrazv2.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://ganeshyadharth:AbleLyf@students.jbrazv2.mongodb.net/?retryWrites=true&w=majority&appName=students')
mongo_db = client["AbleLyf"]
collection = mongo_db["behaviour"]
mongo_collection = mongo_db["candidateBehaviour"]




update_query = {'name': "saravana"}
update_data = {
        '$push': {
            'activity': {
                'status': "active",
                'activitycur': "Running",
                'area': "Playhall",
                'cam': "6",
                'time': datetime.now().strftime('%H:%M:%S')
                }}}

mongo_collection.update_one(update_query, update_data)
     
updates_query = {'name': "sethu"}
updates_data = {
        '$push': {
            'activity': {
                'status': "active",
                'activitycur': "SittingActive",
                'area': "Playhall",
                'cam': "6",
                'time': datetime.now().strftime('%H:%M:%S')
                }}}


mongo_collection.update_one(updates_query, updates_data)

updates_query = {'name': "subramani"}
updates_data = {
        '$push': {
            'activity': {
                'status': "InActive",
                'activitycur': "SittingInActive",
                'area': "Playhall",
                'cam': "6",
                'time': datetime.now().strftime('%H:%M:%S')
                }}}


mongo_collection.update_one(updates_query, updates_data)

