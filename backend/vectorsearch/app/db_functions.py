from datasets import load_dataset
import logging as log

def create_class(client, classname):
    class_obj = {
        "class": classname,
        "properties": [
            {
                "name": "output",
                "dataType": ["text"],
            },
            {
                "name": "instruction",
                "dataType": ["text"],
            },
        ],
        "vectorizer": "text2vec-cohere", 
        "moduleConfig": {
            "generative-cohere": {
            "model": "command-xlarge-nightly", 
            }
    }
    }

    client.schema.create_class(class_obj)
    

def import_data(client,classname,dataset, batch_size = 200,timeout_retries=3):

    client.batch.configure(
    batch_size=batch_size,
    dynamic=True,
    timeout_retries=timeout_retries,)

    counter=0

    def check_batch_result(results: dict):
        if results is not None:
            for result in results:
                if "result" in result and "errors" in result["result"]:
                    if "error" in result["result"]["errors"]:
                        print(result["result"])

    with client.batch as batch:
        for dictionary in dataset:        
            if (counter %5 == 0):
                print(f"Import {counter} ")

            properties = {
            "output": dictionary["output"] if dictionary["output"] else '',
            "instruction": dictionary["instruction"] if dictionary["instruction"] else '',
            }
            
            batch.add_data_object(properties, classname)
            counter = counter+1
            if counter == 1: break
            
        print(f"Import {counter} / {len(dataset)}")
    print("Import complete")


def load_data_create_class(client, classname):
    
    log.getLogger().setLevel(log.INFO)

    try:
        dataset = load_dataset('flytech/python-codes-25k', split='train')

    except:
        print('an exception occured',exc_info=True)
        log.error('Dataset not loaded from web')
        return False
    log.info('Loaded dataset from web')

  
    try:
        create_class(client, classname = classname)
    except:
        log.error('Class not created',exc_info=True)
        return False
    log.info('Class created')
    
    
        
    try:
        import_data(client,classname, dataset)
        log.info('Data imported in collection')
    except:
        log.error('Error importing data',exc_info=True)
        return False
    return True


def find_and_rag(concept, client, classname):
    generatePrompt = "explain {output} as if to a learner and generate psedocode/algorithm for {output}"
    
    result = (
    client.query    
    .get(classname, ["instruction", "output"])
    .with_generate(single_prompt=generatePrompt)
    .with_near_text({
        "concepts": concept 
    })
    .with_limit(1)
    ).do()
    

    try:
        explanation_pseudo = result['data']['Get'][classname][0]['_additional']['generate']['singleResult']
        code = result['data']['Get'][classname][0]['output']
        return explanation_pseudo, code

    except:
        log.error('Search data is null', exc_info=True)