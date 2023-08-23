<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Image Enhancement App 
</h1>
<p align="center"> A Demonstration of Design patterns and Concepts</p>

<p align="center">
    <strong>This demo application is created to demonstrate and prove the Design patterns and concepts published on my <a href="https://medium.com/@benjaminchamwb/enhancing-code-quality-with-design-patterns-5f95ade37ee">Medium article</a>.</strong>
</p>

---

## What does the Image Enhancement App do ?
The app allows user to perform image enhancement (e.g. brightness/contrast/noise) on an image file. The enhanced image will be saved as "enhanced_image.png". <br>
The app is implemented as a Proof-of-concept and would not meet the real-world challenges for image enhancement.

## Running the project
You can setup the project by creating a conda environment and using pip to install the depedencies:
```{.sourceCode .bash}
#Create Conda environment and activate
conda create -n demo_app python=3.8
#Activate Conda environment
conda activate demo_app
#install dependencies
pip install -r requirements.txt
```
When above setup is complete, run app.py
```{.sourceCode .python}
python app.py
```
## Overview of Software Logic
1.) The App request for user to indicate the image file for enhancement. At this point, the user shall input the image file path.<br>
![image](https://github.com/benjamincham/Design-patterns-Demo-Image-Enhancement-App/assets/34295582/e6901025-8a69-45c9-b983-5228381c7751)<br>

2.) After the App validate that the image file exist, the app would display a list of Image enhancement Options. The user shall indicate the number (i.e. 1, 2, or 3) on the type of enhancement to perform.<br>
![image](https://github.com/benjamincham/Design-patterns-Demo-Image-Enhancement-App/assets/34295582/9e8e6cd0-2108-4888-b66e-d9556475fa14)<br>

3.) With the selected enhancement type, the app performs the enhancement and displays both the original and enhanced image for visual comparison<br>
![image](https://github.com/benjamincham/Design-patterns-Demo-Image-Enhancement-App/assets/34295582/d9116d95-a4c6-4d4e-8169-5cd6bc0a24ed)<br>
