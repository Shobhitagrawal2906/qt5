import requests
import json
import uuid
import qdrant_client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

class Qdrant:
    _instance = None

    @staticmethod
    def get_instance():
        return Qdrant._instance
        
    def __init__(self, qdrant_url):
        if Qdrant._instance is None:
            Qdrant._instance = self
        else:
            raise("Qdrant is a singleton class!")
        
        self.client = QdrantClient(qdrant_url) 
        self.create_collection()
    
    def create_collection(self):
       
        try:
            self.client.get_collection("Embeddings")
        
        except qdrant_client.http.exceptions.UnexpectedResponse:
            
            self.client.create_collection(
                collection_name="Embeddings",
                vectors_config=VectorParams(size=2048, distance=Distance.COSINE)
            )
    
    def insert_data(self, data):
        
        operation_info = self.client.upsert(
            collection_name="Embeddings",
            wait=True,
            points=[
                PointStruct(id=str(uuid.uuid4()),vector=data)
            ],
        )
        print(operation_info)
