from .db_functions import load_data_create_class, find_and_rag
import logging as log
import weaviate

from dotenv import load_dotenv
import os


class queryVectorDB():
    """
    Class for the vector database
    """ 
    def __init__(self):
        self.client = self.start()
        self.classname = 'CodeDocv28'

    def start(self):
        
        try:
            load_dotenv()
            WEAVIATE_AUTH_KEY = os.getenv("WEAVIATE_AUTH_KEY")
            WEAVIATE_URL = os.getenv("WEAVIATE_URL")
            COHERE_API_KEY = os.getenv("COHERE_API_KEY")
            
            client = weaviate.Client(
            url = WEAVIATE_URL,  
            auth_client_secret=weaviate.auth.AuthApiKey(api_key=WEAVIATE_AUTH_KEY),  
            additional_headers = {
            "X-Cohere-Api-Key": COHERE_API_KEY
            }
            )
            log.info('Client connected')
            return client
        
        except Exception as e:
            log.error('Client cannot be created', exc_info=True)
            return False
    
    def initiate_weaviate_class(self):
        try : 
            load_data_create_class(self.client, self.classname)
        except:
            log.error('Class creation or populate error')   
            return
        log.info('Class created and populated')
        return True


    
    def get_data(self, query:str):
        """
        Retrieve data from the weaviate schema based on the query
        Returned data is the entire content

        """
        concept = '["' + query +'"]'
        client = self.client
        

        log.info('Generating code(Vector Search) and explanation (RAG based)')
        #concept =  ["code for shopping list"]

        try:
            explanation_pseudo, code = find_and_rag(concept, client, classname = self.classname)
            result = {'exp_pseudo': explanation_pseudo,
                      'code': code}
            return result

        except:
            log.error('Error generating code and explanation',exc_info=True)

        
    