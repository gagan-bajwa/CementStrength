from CementStrength.entity import DbOperationsConfig
import pandas as pd
import csv
import sqlite3
import os
from CementStrength import logger
from CementStrength.utils import read_yaml,create_directories


class DbOperations:
    def __init__(self,config: DbOperationsConfig):
        self.config = config
        create_directories(self.config.training_dir)
        create_directories(self.config.db_dir)

    def connect_to_db(self):
        logger.info("Connecting to database")
        self.sqliteConnection = sqlite3.connect(self.config.db_name)
        self.cursor = self.sqliteConnection.cursor()
        logger.info("Connection Established")
    
    def close_connection(self):
        self.cursor.close()
        logger.info("Connection Closed")

    def get_data_into_db(self):
        logger.info("Getting data into database")
        dfs = [pd.read_csv(os.path.join(self.config.source_dir,f)) for f in  os.listdir(self.config.source_dir)]
        result = pd.concat(dfs)
        result.to_sql('Cement_Strength',con=self.sqliteConnection,if_exists='replace',index= False)
        self.cursor.close()
        logger.info("Data inserted")
    
    def fetch_data_from_db(self):
        logger.info("fetching data from DB")
        df_sql = pd.read_sql(sql ='select * from Cement_Strength;',con = self.sqliteConnection)
        self.cursor.close()
        df_sql.to_csv(self.config.training_file)
        logger.info("data fetched")

        


    



