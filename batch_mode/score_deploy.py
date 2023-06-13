from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule
from score import bodyfat_prediction

deployment = Deployment.build_from_flow(
    flow=bodyfat_prediction,
    name="Blaq's Body Fat Prediction Service",
    parameters={
        
        "run_id": "81ff00fd20ed4de68cf6f9b06221fbcf",
    },
    schedule=CronSchedule(cron="1 * * * *"),
    work_queue_name="Bodyfat_queue",
)

deployment.apply()

#import schedule
#import time

#from score import bodyfat_prediction

#def run_bodyfat_prediction():
    # Replace '030e5b40fd3f495ea03580f13afdb844' with the desired run_id
    #bodyfat_prediction(run_id='030e5b40fd3f495ea03580f13afdb844')

#schedule.every().hour.do(run_bodyfat_prediction)

#while True:
   # schedule.run_pending()
    #time.sleep(1)