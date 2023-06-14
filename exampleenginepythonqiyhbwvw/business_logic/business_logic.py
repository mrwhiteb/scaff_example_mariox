from dataproc_sdk.dataproc_sdk_utils.logging import get_user_logger
import pyspark.sql.functions as f
from pyspark.sql import DataFrame,Window





class BusinessLogic:
    """
    Just a wrapper class to ease the user code execution.
    """

    def __init__(self):
        """
        Constructor
        """
        self.__logger = get_user_logger(BusinessLogic.__qualname__)
    def filter_by_age_and_vip(self, df: DataFrame) -> DataFrame:
        self.__logger.info('applying filter by edad and vip')
        return df.filter((f.col("edad") >= 30) & (f.col("edad") <= 50) & (f.col("vip") == 'true'))

    def join_tables(self, clients_df: DataFrame,contracts_df: DataFrame, products_df: DataFrame ) -> DataFrame:
        self.__logger.info('applying join process')
        return clients_df.join(contracts_df,f.col("cod_client") == f.col("cod_titular"),("inner"))\
                         .join(products_df,["cod_producto"],"inner")

    def filter_by_number_of_contrats(self,df: DataFrame) -> DataFrame:
        self.__logger.info('filtering by number of contracts')
        return df.select(*df.columns, f.count("nombre").over(Window.partitionBy("cod_client")).alias("count"))\
                  .filter(f.col("count") > 3).drop("count")

    def hash_columns(self, df: DataFrame) -> DataFrame:
        self.__logger.info('Generating hash column')
        return df.select(*df.columns, f.sha2(f.concat_ws("||", *df.columns),256).alias("hash"))


