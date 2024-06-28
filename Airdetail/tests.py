from django.test import TestCase

# Create your tests here.
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Airtrip.Airtrip.settings')
settings.configure()
from rest_framework.test import APIClient
from rest_framework import status
import json


class YourAPIsTestCase(TestCase):
    def setUp(self):
        # Initialize the APIClient for making requests
        self.client = APIClient()
    
    def test_post_endpoint(self):

        
        # Test POST request to your API endpoint
        #data = {'key': 'value'}  # Provide necessary data for POST request
        data =  {
        		"id":1,
    			"userName": "Ravddldi",
    			"firstName": "Raddmfvi",
    			"lastName": "S",
   		 	    "income": "15000.000",
    			"dateOfBirth": "1999-01-01",
    			"middleName": "S",
    			"gender": "M",
    			"age": 2,
    			"emails":"ksdjdmdl@ldk",
    			"addressInfo": {
        		"name": "Lakshmi",
        		"country": "India",
        		"region": "Karnataka",
        		"address": "#143 th cross skdfj",
        		"city": "Mandyau",
        		"buildinginfo": "187"
    					},
    			"homeAddress": {
        		"name": "Qas",
        		"country": "India",
        		"region": "Karnataka",
        		"address": "#111 5th cross skdfj",
        		"city": "Mandya",
        		"buildinginfo": "111"
    					}
        }    
        
        response = self.client.post('http://127.0.0.1:8000/person/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        person_id = response_data.get('id')
        print("Created person ID:", person_id)
        
        return person_id if person_id is not None else None
        
    def test_post_trip_endpoint(self):
        # Test POST request to your API endpoint
        person_id=self.test_post_endpoint()

        if person_id is None:
            print("Person ID is None. Cannot proceed with creating trip.")
            return

        data = {
		"tripId":1234,
		"shareId":"vA83",
		"name":"AP",
		"budget":3984,
		"description":"Hyderbad",
		"startsAt":"2024-06-12",
		"endsAt":"2024-06-15",
		"startTime":"10:12:00",
		"endTime":"12:20:00",
		"cost":29344,
		"personId":person_id
		}        

        print("Trip data:", data) 

        response = self.client.post('/person/trips/', json.dumps(data), content_type='application/json')

        print("Response content:", response.content)

        response = self.client.post('http://127.0.0.1:8000/person/trips/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = json.loads(response.content)
        trip_id=response_data.get('id')
        return trip_id if trip_id is not None else None


    def test_get_endpoint(self):
        # Test GET request to your API endpoint
        response = self.client.get('http://127.0.0.1:8000/persons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_get_person_endpoint(self):
        # Test GET request to your API endpoint
        person_id=self.test_post_endpoint()
        if person_id is None:
            print("Person ID is None. Cannot proceed.")
            return


        response = self.client.get('http://127.0.0.1:8000/persons/{person_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_get_trip_endpoint(self):
        # Test GET request to your API endpoint
        response = self.client.get('http://127.0.0.1:8000/persons/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)      
       

    def test_get_tripfull_endpoint(self):
        # Test GET request to your API endpoint
        person_id=self.test_post_endpoint()
        if person_id is None:
            print("Person ID is None. Cannot proceed.")
            return

        response = self.client.get('http://127.0.0.1:8000/persons/{person_id}/trips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
       
 
    def test_get_tripper_endpoint(self):
        # Test GET request to your API endpoint
        person_id=self.test_post_endpoint()
        if person_id is None:
            print("Person ID is None. Cannot proceed.")
            return
        
        trip_id=self.test_post_trip_endpoint()
        if trip_id is None:
            print("Trip ID is None. Cannot proceed.")
            return
        response = self.client.get('http://127.0.0.1:8000/persons/{person_id}/trips/{trip_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)               
                

    def test_get_attachment_endpoint(self):
        # Test GET request to your API endpoint
        person_id=self.test_post_endpoint()
        if person_id is None:
            print("Person ID is None. Cannot proceed.")
            return
        
        response = self.client.get('http://127.0.0.1:8000/persons/{person_id}/attachments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
"""
    def test_get_attachmentper_endpoint(self):
        # Test GET request to your API endpoint
        response = self.client.get('http://127.0.0.1:8000/persons/1/attachments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                

        
        
    def test_put_endpoint(self):
        # Test PUT request to your API endpoint
        data = {'middleName': 'middle'}  # Provide necessary data for PUT request
        response = self.client.put('http://127.0.0.1:8000/person/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
  	    
        
    def test_put_trip_endpoint(self):
        # Test PUT request to your API endpoint
        data = {'description': 'PUT Hyderbad'}  # Provide necessary data for PUT request 	    
        response = self.client.put('http://127.0.0.1:8000/person/1/trips/1/', data)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
	            
        
        
    def test_delete_endpoint(self):
        # Test DELETE request to your API endpoint
        response = self.client.delete('http://127.0.0.1:8000/persons1/7/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
   
    def test_delete_alltrip_endpoint(self):
        # Test DELETE request to your API endpoint
        response = self.client.delete('http://127.0.0.1:8000/persons1/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
  
    def test_delete_pertrip_endpoint(self):
        # Test DELETE request to your API endpoint
        response = self.client.delete('http://127.0.0.1:8000/persons1/1/trips/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)                
"""
