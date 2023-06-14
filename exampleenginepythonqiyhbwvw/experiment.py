
from typing import Dict
from dataproc_sdk.dataproc_sdk_utils.logging import get_user_logger
from pyspark.sql import SparkSession, DataFrame


from exampleenginepythonqiyhbwvw.business_logic.business_logic import BusinessLogic


class DataprocExperiment:
    """
    Just a wrapper class to ease the user code execution.
    """

    def __init__(self):
        """
        Constructor
        """
        self.__logger = get_user_logger(DataprocExperiment.__qualname__)
        self.__spark = SparkSession.builder.getOrCreate()
    def run(self, **parameters: Dict) -> None:
        """
        Execute the code written by the user.

        Args:
            parameters: The config file parameters
        """
        self.__logger.info("Executing experiment")
        """clients_df = self.__spark.read.csv(str(parameters ["clients"]))"""
        clients_df = self.read_csv("clients", parameters)
        contracts_df = self.read_csv("contracts", parameters)
        products_df = self.read_csv("products", parameters)

        logic = BusinessLogic()
        filtered_clients_df: DataFrame = logic.filter_by_age_and_vip(clients_df)
        joined_dataframe: DataFrame = logic.join_tables(filtered_clients_df,contracts_df,products_df)
        filtered_contracts_df: DataFrame = logic.filter_by_number_of_contrats(joined_dataframe)
        logic.hash_columns(filtered_contracts_df).show(20,False)
        #clients_df.show()
        #contracts_df.show()
        #products_df.show()
        #filtered_contracts_df.show()

    def read_csv(self,table_id,parameters):
        return self.__spark.read \
        .option('header','true') \
        .option('delimiter',',') \
        .csv(str(parameters[table_id]))
