#  Body Fat Percent Estimator by 🅱🅻🅰🆀
![bodyfat](https://github.com/Blaqadonis/body_fat_percent_estimator_service/assets/100685852/045a9a97-61b9-4c31-9ec7-e400711fb6d5)        ![image](https://github.com/Blaqadonis/body_fat_percent_estimator_service/assets/100685852/8e51fbe7-0069-436b-88ef-168473b01101) ![image](https://github.com/Blaqadonis/body_fat_percent_estimator_service/assets/100685852/aff88f75-8538-4fc7-a706-1279423f1b85)



CAVEAT:
This project is for fun and my personal education. It came out of just playing around with some MLOps tools for production, like ```MLflow Prefect wandb``` etcetera.
## What it is - Context
Lists estimates of the percentage of body fat determined by underwater
weighing and various body circumference measurements for 252 men.

## Why I worked on it.
Taking accurate measurement of body fat is inconvenient/costly and it is desirable to have easy methods of estimating body fat that are not inconvenient/costly.

## What it is - Content
The variables listed below, from left to right, are:

* Density determined from underwater weighing
* Percent body fat from Siri's (1956) equation
* Age (years)
* Weight (lbs)
* Height (inches)
* Neck circumference (cm)
* Chest circumference (cm)
* Abdomen 2 circumference (cm)
* Hip circumference (cm)
* Thigh circumference (cm)
* Knee circumference (cm)
* Ankle circumference (cm)
* Biceps (extended) circumference (cm)
* Forearm circumference (cm)
* Wrist circumference (cm)

(Measurement standards are apparently those listed in Benhke and Wilmore (1974), pp. 45-48 where, for instance, the abdomen 2 circumference is measured "laterally, at the level of the iliac crests, and anteriorly, at the umbilicus".)

These data are used to produce the predictive equations for lean body weight given in the abstract "Generalized body composition prediction equation for men using simple measurement techniques", K.W. Penrose, A.G. Nelson, A.G. Fisher, FACSM, Human Performance Research Center, Brigham Young University, Provo, Utah 84602 as listed in Medicine and Science in Sports and Exercise, vol. 17, no. 2, April 1985, p. 189. (The predictive equation were obtained from the first 143 of the 252 cases that are listed below).

## More details
A variety of popular health books suggest that the readers assess their health, at least in part, by estimating their percentage of body fat. In Bailey (1994), for instance, the reader can estimate body fat from tables using their age and various skin-fold measurements obtained by using a caliper. Other texts give predictive equations for body fat using body circumference measurements (e.g. abdominal circumference) and/or skin-fold measurements. See, for instance, Behnke and Wilmore (1974), pp. 66-67; Wilmore (1976), p. 247; or Katch and McArdle (1977), pp. 120-132).

The percentage of body fat for an individual can be estimated once body density has been determined. Folks (e.g. Siri (1956)) assume that the body consists
of two components - lean body tissue and fat tissue. Letting:

* D = Body Density (gm/cm^3)
* A = proportion of lean body tissue
* B = proportion of fat tissue (A+B=1)
* a = density of lean body tissue (gm/cm^3)
* b = density of fat tissue (gm/cm^3)

we have:

$D = \frac {1}{[(\frac {A}{a}) + (\frac {B}{b})]}$

solving for B we find:
$B = \frac {\frac {ab}{a - b} - \frac {b}{a - b}}{d}$

Using the estimates a=1.10 gm/cm^3 and b=0.90 gm/cm^3 (see Katch and McArdle (1977), p. 111 or Wilmore (1976), p. 123) we come up with "Siri's equation":

Percentage of Body Fat (i.e. 100*B) = 495/D - 450.

Volume, and hence body density, can be accurately measured a variety of ways. The technique of underwater weighing "computes body volume as the difference between body weight measured in air and weight measured during water submersion. In other words, body volume is equal to the loss of weight in
water with the appropriate temperature correction for the water's density" (Katch and McArdle (1977), p. 113). Using this technique,

$Body_-Density = \frac {WA}{[(\frac {WA-WW}{c.f.} - LV]}$

where:

WA = Weight in air (kg)
WW = Weight in water (kg)
c.f. = Water correction factor (=1 at 39.2 deg F as one-gram of water occupies exactly one cm^3 at this temperature, =.997 at 76-78 deg F)
LV = Residual Lung Volume (liters)
(Katch and McArdle (1977), p. 115). Other methods of determining body volume are given in Behnke and Wilmore (1974), p. 22 ff.

## Where from?

The data were generously supplied by Dr. A. Garth Fisher who gave permission to freely distribute the data and use for non-commercial purposes.

``` Roger W. Johnson
Department of Mathematics & Computer Science
South Dakota School of Mines & Technology
501 East St. Joseph Street
Rapid City, SD 57701

email address: rwjohnso@silver.sdsmt.edu
[web address](http://silver.sdsmt.edu/~rwjohnso)
```

## References
Bailey, Covert (1994). Smart Exercise: Burning Fat, Getting Fit, Houghton-Mifflin Co., Boston, pp. 179-186.

Behnke, A.R. and Wilmore, J.H. (1974). Evaluation and Regulation of Body Build and Composition, Prentice-Hall, Englewood Cliffs, N.J.

Siri, W.E. (1956), "Gross composition of the body", in Advances in Biological and Medical Physics, vol. IV, edited by J.H. Lawrence and C.A. Tobias, Academic Press, Inc., New York.

Katch, Frank and McArdle, William (1977). Nutrition, Weight Control, and Exercise, Houghton Mifflin Co., Boston.

Wilmore, Jack (1976). Athletic Training and Physical Fitness: Physiological Principles of the Conditioning Process, Allyn and Bacon, Inc., Boston.





# How it works!

Everything here runs locally. If you want to try out the service, follow the steps below:

Before you proceed, create a virtual environment. 

I used ```python version 3.8```. To create an environment with that version of python using ```Conda```:

```conda create -n <env-name> python=3.8```

Just replace ```<env-name>``` with any title you want. Next:
  
``` conda activate <env-name>```
  
to activate the environment.

## 1. Running the container (Dockerfile)

First, you need to have docker installed on your system. I am using a windows machine, and I have docker desktop installed on my system. If you do not have that,
then you should try doing that first. If you are all set and good, then proceed.

Now run:
  
  ``` pip install -r requirements.txt```
  
to install all necessary external dependencies.

Next, Run:
  
``` docker build -t <service-name>:v1 . ```
  
Replace ```<service-name>``` with whatever name you wish to give to the body fat percent estimator service, to build the image.
  
To run this service:
  
``` docker run -it --rm -p 9696:9696 <service-name>:latest ```
  
NOTE: I am running this on Windows hence Waitress. If your local machine requires Gunicorn, I think the Dockerfile should be edited with something like this:

``` FROM python:3.8-slim-buster

RUN pip install -U pip

WORKDIR /app

COPY [ "online_webservice_flask/predict.py", "models/pipeline.bin", "requirements.txt", "./" ]

RUN pip install -r requirements.txt

EXPOSE 9696 
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]
```

If the container is up and running, open up a new terminal. Reactivate the Conda environment. Run:
  
``` python test.py ```
  
NOTE: ```test.py``` is an example of data you can send to the ENTRYPOINT to interact with the service. Edit it as much as you desire and try out some predictions.
  
## 2. Simple web service (server managed locally with Flask)

You need to first run:

```pip install -r requirements.txt```

Followed by  ```python online_webservice_flask/predict.py```  to run this service.

Open up a new terminal. Run ```python test.py```  to interact with the service.

## 3. Web service hosted and managed on MLflow servers

You need to first run:

```pip install -r requirements.txt```

Next, spin up the MLflow server with:

```mlflow server --backend-store-uri sqlite:///local_server.db --default-artifact-root ./artifacts --host localhost --port 5000```

This will create a folder ```artifacts``` on your local machine, as well as the database ```local_server```.

Now, run:

```python test.py```


Try it out with family, friends, colleagues, neighbours, and let me know how to improve on it.
