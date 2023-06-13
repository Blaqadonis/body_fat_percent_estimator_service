
import os
import sys

import uuid
import pickle

from datetime import datetime
import numpy as np
import pandas as pd

import mlflow

from prefect import task, flow, get_run_logger
from prefect.context import get_run_context

from dateutil.relativedelta import relativedelta

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline


def generate_uuids(n):
    data_ids = []
    for i in range(n):
        data_ids.append(str(uuid.uuid4()))
    return data_ids


def read_dataframe(filename: str):
    df = pd.read_csv(filename)
    
    df['data_id'] = generate_uuids(len(df))

    return df

def prepare_dictionaries(df):
    df_dicts = df.to_dict(orient='records')
    return df_dicts


def load_model(run_id):
    with open('models/pipeline.bin', 'rb') as f_out:
        model = pickle.load(f_out)
    return model


def save_results(df, y_pred, run_id, output_file):
    df_result = pd.DataFrame()
    df_result["Density"] = df["Density"]
    df_result["Age"] =  df["Age"]
    df_result["Weight"] = df["Weight"]
    df_result["Height"] =  df["Height"]
    df_result["Neck"] =  df["Neck"]
    df_result["Chest"] = df["Chest"]
    df_result["Abdomen"] = df["Abdomen"]
    df_result["Hip"] = df["Hip"]
    df_result["Thigh"] = df["Thigh"]
    df_result["Knee"] =  df["Knee"]
    df_result["Biceps"] = df["Biceps"]
    df_result["Forearm"] =  df["Forearm"]
    df_result["Wrist"] =  df["Wrist"]
    df_result['model_version'] = run_id
    df_result['data_id'] = df['data_id']
    df_result.to_parquet(output_file, index=False)


@task
def apply_model(input_file, run_id, output_file):
    logger = get_run_logger()

    logger.info(f'reading the data from {input_file}...')
    df = read_dataframe(input_file)
    dicts = prepare_dictionaries(df)

    logger.info(f'loading the model with RUN_ID={run_id}...')
    model = load_model(run_id)

    logger.info(f'applying the model...')
    y_pred = model.predict(dicts)

    logger.info(f'saving the result to {output_file}...')

    save_results(df, y_pred, run_id, output_file)
    return output_file


def get_paths(run_date, run_id):
    prev_hour = run_date - relativedelta(hours=1)
    year = prev_hour.year
    month = prev_hour.month 

    input_file = f'data/bodyfat.csv'
    #input_file = f's3://nyc-tlc/trip data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/logged_files.csv'
    
    return input_file, output_file


@flow
def bodyfat_prediction(
        run_id: str,
        run_date: datetime = None):
    if run_date is None:
        ctx = get_run_context()
        run_date = ctx.flow_run.expected_start_time
    
    input_file, output_file = get_paths(run_date, run_id)

    apply_model(
        input_file=input_file,
        run_id=run_id,
        output_file=output_file
    )


def run():
   # taxi_type = sys.argv[1] # 'green'
   ## year = int(sys.argv[1]) # 2022
   # month = int(sys.argv[3]) # 2

    #run_id = sys.argv[1] # '06c44f9292764e73a72a93b9db20a24d'

    bodyfat_prediction(
       
        
        run_id='81ff00fd20ed4de68cf6f9b06221fbcf',
        #run_date=datetime(year=year, month=month, day=1)
    )


if __name__ == '__main__':
    run()




