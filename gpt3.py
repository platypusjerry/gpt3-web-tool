"""Creates the Example and GPT classes for a user to interface with the OpenAI
API."""

import openai
import uuid
from operator import itemgetter



def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class Example:
    """Stores an input, output pair and formats it to prime the model."""
    def __init__(self, inp, out):
        self.input = inp
        self.output = out
        self.id = uuid.uuid4().hex

    def get_input(self):
        """Returns the input of the example."""
        return self.input

    def get_output(self):
        """Returns the intended output of the example."""
        return self.output

    def get_id(self):
        """Returns the unique ID of the example."""
        return self.id

    def as_dict(self):
        return {
            "input": self.get_input(),
            "output": self.get_output(),
            "id": self.get_id(),
        }


class GPT:
    """The main class for a user to interface with the OpenAI API.

    A user can add examples and set parameters of the API request.
    """
    def __init__(self,
                 engine,
                 temperature,
                 max_tokens,
                 top_p,
                 frequency_penalty,
                 presence_penalty,
                 input_prefix=" ",
                 input_suffix="\n",
                 output_prefix=" ",
                 output_suffix="\n\n",
                 append_output_prefix_to_query=False):
        self.examples = {}
        self.engine = engine
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.input_prefix = input_prefix
        self.input_suffix = input_suffix
        self.output_prefix = output_prefix
        self.output_suffix = output_suffix
        self.append_output_prefix_to_query = append_output_prefix_to_query
        self.stop = (output_suffix + input_prefix).strip()

    def add_example(self, ex):
        """Adds an example to the object.

        Example must be an instance of the Example class.
        """
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples[ex.get_id()] = ex

    def delete_example(self, id):
        """Delete example with the specific id."""
        if id in self.examples:
            del self.examples[id]

    def get_example(self, id):
        """Get a single example."""
        return self.examples.get(id, None)

    def get_all_examples(self):
        """Returns all examples as a list of dicts."""
        return {k: v.as_dict() for k, v in self.examples.items()}

    def get_prime_text(self):
        """Formats all examples to prime the model."""
        return "".join(
            [self.format_example(ex) for ex in self.examples.values()])

    def get_engine(self):
        """Returns the engine specified for the API."""
        return self.engine

    def get_temperature(self):
        """Returns the temperature specified for the API."""
        return self.temperature
    
    def get_top_p(self):
        """returns the top_p specified for the api"""
        return self.top_p
    
    def get_max_tokens(self):
        """Returns the max tokens specified for the API."""
        return self.max_tokens
    
    def get_frequency_penalty(self):
        """returns the frequency penalty specified for the api"""
        return self.frequency_penalty

    def get_presence_penalty(self):
        """returns the presence penalty specified for the api"""
        return self.presence_penalty

    def craft_query(self, prompt):
        """Creates the query for the API request."""
        q = self.get_prime_text(
        ) + self.input_prefix + prompt + self.input_suffix
        if self.append_output_prefix_to_query:
            q = q + self.output_prefix

        return q
    
    def update_temp(self, new_temp):
        self.temperature = new_temp
        return self.temperature
    

    def submit_request(self, prompt, new_temp):
        """Calls the OpenAI API with the specified parameters."""
        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=self.craft_query(prompt),
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.update_temp(new_temp),
                                            top_p=self.get_top_p(),
                                            frequency_penalty=self.get_frequency_penalty(),
                                            presence_penalty=self.get_presence_penalty(),
                                            n=1,
                                            stream=False,
                                            stop=self.stop)
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response['choices'][0]['text']

    def format_example(self, ex):
        """Formats the input, output pair."""
        return self.input_prefix + ex.get_input(
        ) + self.input_suffix + self.output_prefix + ex.get_output(
        ) + self.output_suffix
            

            
            
            
            
            
            
            
class semantic():
    def __init__(self, 
                 documents):
        self.documents = documents
        
        
    def get_query(self, query):
        return query
    
    def get_documents(self):
        return self.documents
    

    
    
    
    
    def get_score(self, query):
        search_response = openai.Engine("babbage").search(
            query = self.get_query(query),
            documents = self.get_documents()
            )
        data_search_response = dict(search_response)
        intents_list = ['Interested', 'Need Information', 'Unsubscribe',
                       'Wrong Person', 'Complaint', 'Inquiry', 'Request',
                       'Feedback', 'Advertisement']
        scores = []
        for a,b in data_search_response.items():
            if a == 'data':
                data_list = list(data_search_response.values())
                document_list = data_list[1]
                
                for i,j in zip(document_list, intents_list):
                    document = dict(i)
                    intent_score = dict((k, document[k]) for k in ['document', 'score']
                                                if k in document)
                    intent_score.update(text = j)
                    scores.append(intent_score)
                    
            
        return scores
    
    
    
    
    def intent_filtering(self, raw_score):
        data = sorted(raw_score, key=itemgetter('score'), reverse=True)
        for a in range(len(data)):
            if data[a]["score"] < 0:
                data[a]["score"] = 0
        
        max = 0
        top_int = []
        for i in range(len(data)-1):
            if data[i]["score"] - data[i+1]["score"] > max:
                max = data[i]["score"] - data[i+1]["score"]
                top_int.append(data[i])
                
        return_list = []
        for a in range(len(top_int)):
            return_list.append(top_int[a]["text"])
            
        str_ = "\n , ".join(return_list)
        
        return(str_)
    
    
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
