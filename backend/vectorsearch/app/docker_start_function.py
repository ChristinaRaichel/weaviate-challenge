from .query_vector_DB import queryVectorDB
import logging as logger

try:
    qvb = queryVectorDB()
    if qvb == False : return      
    qvb.initiate_weaviate_class()
except:
    logger.info('Error in connecting/loading weaviate instance', exc_info=True)
