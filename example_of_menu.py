# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import cv2
import time
import requests
from bs4 import BeautifulSoup
import csv

df = pd.read_csv("offers.csv")
name = st.multiselect('Тип квартиры', df['Тип'].unique())
room = st.multiselect('Количество комнат', df['Количество комнат'].unique())
new_df = df[(df['Тип'].isin(name)) & (df['Количество комнат'].isin(room))]
st.table(new_df)

uploaded_file1 = st.file_uploader("Choose a image file 1", type="jpg")
if uploaded_file1 is not None:
    image1 = Image.open(uploaded_file1)
    st.image(image1, caption='Photo 1', use_column_width=True)
    img_array1 = np.array(image1)
    resized1 = cv2.resize(img_array1, (8,8), interpolation=cv2.INTER_AREA)
    gray_image1 = cv2.cvtColor(resized1, cv2.COLOR_BGR2GRAY)
    avg = gray_image1.mean()
    ret, threshold_image1 = cv2.threshold(gray_image1, avg, 255, 0)
    st.image(threshold_image1)
    hash1 = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image1[x, y]
            if val == 255:
                hash1 = hash1 + "1"
            else:
                hash1 = hash1 + "0"
    st.write(hash1)


uploaded_file2 = st.file_uploader("Choose a image file 2", type="jpg")
if uploaded_file2 is not None:
    image2 = Image.open(uploaded_file2)
    st.image(image2, caption='Photo 2', use_column_width=True)
    img_array2 = np.array(image2)
    resized2 = cv2.resize(img_array2, (8, 8), interpolation=cv2.INTER_AREA)
    gray_image2 = cv2.cvtColor(resized2, cv2.COLOR_BGR2GRAY)
    avg = gray_image2.mean()
    ret, threshold_image2 = cv2.threshold(gray_image2, avg, 255, 0)
    st.image(threshold_image2)
    hash2 = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image2[x, y]
            if val == 255:
                hash2 = hash2 + "1"
            else:
                hash2 = hash2 + "0"
    st.write(hash2)


    def CompareHash(hash1, hash2):
        l = len(hash1)
        i = 0
        count = 0
        while i < l:
            if hash1[i] != hash2[i]:
                count = count + 1
            i = i + 1
        return count
    st.write("Result is ", CompareHash(hash1, hash2))
    st.header("FINAL RESULT")
    if CompareHash(hash1, hash2) >= 0 and CompareHash(hash1, hash2) <= 13:
        st.write("Similar")
    elif CompareHash(hash1, hash2) > 13 and CompareHash(hash1, hash2) <= 30:
        st.write("Quiet Similar")
    else:
        st.write("Not Similar")