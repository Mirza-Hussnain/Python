import os
import time
import pandas as pd
import numpy as np
from base_util.DB_Connect import BaseManager
from base_util.log_setup import setup_logger
import inspect
import pandas as pd
import time 
# The import statements are for bringing in necessary libraries and modules.
# Pandas library are not mandatory in this code we can remove this.
# Function to run a specific query for reprocessing data.


def update_query_reprocess():
    # The purpose of this function is to execute a query related to reprocessing.
    # The query is executed, but the fetched data is not used or processed further.
    # There are no modifications needed here.
    # Function to run a complex query and fetch data for different systems.
    db_connection = None
    cursor = None
    try:
        db_connection, cursor = base.get_rw_db_connection()
        query = f"""select  p_cc, p_se , p_ki from patent_store.patent_file_info where src_file_loc='clvt-chub-dev/published/patents/cXML/regular/docdbamend/cxml_docdbamend202248_01.tar' and ( ( xml_type=1 and status =1 and xml_loc is not null) or (status in (3,4) and xml_type = 0 and xml_loc is null) );"""
        cursor.execute(query)
        data=cursor.fetchall()
        db_connection.close()
        # df=pd.DataFrame(data,columns=['p_cc','p_se','p_ki'])
        # df=df.drop_duplicates()
        # df=df.sort_values(by=['cc'])
    except Exception as error:
        logger.warning((f"script=prod_query - operation={inspect.stack()[0][3]} - err_msg={error} - status_msg=Failed to run the reprocess function."))
def update_query_summary(db_connection, cursor):
    # The purpose of this function is to execute a complex query for different systems.
    # However, the fetched data is collected in the 'result' list but not processed further.
    # Possible improvement: Instead of storing the data in 'result', process it immediately or use a generator to avoid storing all data in memory at once.
    # Function to run a query related to a specific system.
    result = []  # Use a generator to yield rows one by one

    try:
        system = ['FLD', 'FLD_MAT', 'LH_MAT', 'DOCDB', 'INPADOC', 'LH', 'CXMLPLUS', 'DWPI', 'INT_MAT']

        for i in system:
            begin = time.time()
            query = f'''SET statement_timeout = '90min'; 
                       select p_ki, lu, p_se from patent_store.patent_info 
                       where p_cc='CN' and p_date='2021-12-07' and status=1 and system = '{i}' '''
            cursor.execute(query)

            # Use a generator to yield rows one by one
            for row in cursor:
                yield row

    except Exception as error:
        logger.warning((f"script=prod_query - operation={inspect.stack()[0][3]} - err_msg={error} - status_msg=Failed to run the summary function."))

        
def update_query_feed():
    # The purpose of this function is to execute a query for a specific system.
    # The fetched data is not used or processed.
    # There are no modifications needed here.
    db_connection = None
    cursor = None
    try:
        query_lh = f'''SET statement_timeout = '900min'; select p_cc as cc from patent_store.patent_file_info pfi where system = 'LH' '''
        cursor.execute(query_lh)
        data=cursor.fetchall()
        db_connection.close()
    #     df=pd.DataFrame(data,columns=['cc'])
    #     df=df.drop_duplicates()
    #     df=df.sort_values(by=['cc'])
    #     # print(df)
    #     # print(len(df))
    except Exception as error:
        print(error)

if __name__ == "__main__":
    # Setting up database connection pools.
    # Possible improvement: It's good to close the database connections after using them to free up resources.
    # Calling the three functions to run their respective queries.
    logger = setup_logger()
    try:
        logger.warning("script=patent_query- status_msg=starting main function.")
        base = BaseManager(logger, "dds-util-feed-coverage")
        base.setup_db_connection_pool()
        base.setup_db_rw_connection_pool()
        logger.warning("script=patent_query - status_msg=done setting up db connection pools.")

        # Open a single database connection and pass it to functions
        db_connection, cursor = base.get_rw_db_connection()

        update_query_reprocess(db_connection, cursor)
        update_query_summary(db_connection, cursor)
        update_query_feed(db_connection, cursor)

        # Close the database connection
        db_connection.close()

    except Exception as error:
        # Logging an error if any exception occurs.
        # Possible improvement: Provide more detailed error messages to help with debugging.
        logger.error(f"script=prod_querys - operation={inspect.stack()[0][3]} - err_msg={error} - status_msg=Failed to run the main function.")

     








"""
Tasks assigned
First Task 
Analyze the provided code for any potential performance issues
Upon analyzing the provided code, I identified a few potential performance issues and areas that could be optimized:

1.Multiple Database Connections: Each function (`update_query_reprocess()`, `update_query_summary()`, `update_query_feed()`) opens its own database connection.
 This can lead to inefficiencies, especially if multiple queries are executed in succession. Consider opening a single database connection and passing it to each function.

2.Data Fetching and Storage: In the `update_query_summary()` function, fetched data for different systems is stored in the `result` list.
If the data is large, this can consume significant memory. Instead of storing all data in memory, you could process rows immediately or use a generator approach to reduce memory usage.

3.Logging Overhead: Extensive logging can impact performance. 
While logging is valuable for monitoring, excessive logging can slow down the execution of the script.


Second Task
 Identify areas where database queries can be optimized for efficiency.

The primary area for query optimization is within the `update_query_summary()` function where multiple queries are executed in a loop for different systems.
 To optimize these queries:

Combining Queries:' Instead of executing separate queries for each system, consider combining similar queries into a single query using the `IN` clause.
This reduces the number of database round trips and can improve efficiency.'


Third Task is to update code which are made in the above code
"""




