"""
API Helper for making HTTP requests
"""
import requests
import logging
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)


class APIHelper:
    """Helper class for API testing"""
    
    def __init__(self, base_url=None):
        """Initialize API helper"""
        self.base_url = base_url or Config.API_BASE_URL
        self.timeout = Config.API_TIMEOUT
        self.session = requests.Session()
        logger.info(f"APIHelper initialized with base URL: {self.base_url}")
    
    def get(self, endpoint, params=None):
        """Send GET request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET request to: {url}")
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            logger.info(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"GET request failed: {str(e)}")
            raise
    
    def post(self, endpoint, data=None, json=None):
        """Send POST request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST request to: {url}")
        
        try:
            response = self.session.post(
                url, 
                data=data, 
                json=json, 
                timeout=self.timeout
            )
            logger.info(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"POST request failed: {str(e)}")
            raise
    
    def put(self, endpoint, data=None, json=None):
        """Send PUT request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT request to: {url}")
        
        try:
            response = self.session.put(
                url, 
                data=data, 
                json=json, 
                timeout=self.timeout
            )
            logger.info(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"PUT request failed: {str(e)}")
            raise
    
    def delete(self, endpoint):
        """Send DELETE request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE request to: {url}")
        
        try:
            response = self.session.delete(url, timeout=self.timeout)
            logger.info(f"Response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"DELETE request failed: {str(e)}")
            raise
    
    def verify_status_code(self, response, expected_code):
        """Verify response status code"""
        actual_code = response.status_code
        if actual_code == expected_code:
            logger.info(f"✓ Status code verified: {actual_code}")
            return True
        else:
            logger.error(f"✗ Status code mismatch. Expected: {expected_code}, Got: {actual_code}")
            return False
    
    def verify_json_field(self, response, field_name):
        """Verify JSON response contains field"""
        try:
            json_data = response.json()
            if field_name in json_data:
                logger.info(f"✓ Field '{field_name}' found in response")
                return True
            else:
                logger.error(f"✗ Field '{field_name}' not found in response")
                return False
        except Exception as e:
            logger.error(f"Error parsing JSON: {str(e)}")
            return False


# Test the helper
if __name__ == "__main__":
    api = APIHelper()
    
    # Test GET request
    response = api.get("/users/1")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test verification
    api.verify_status_code(response, 200)
    api.verify_json_field(response, "data")