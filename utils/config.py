"""
Configuration file for test framework
"""

class Config:
    """Test configuration"""
    
    # API Configuration
    API_BASE_URL = "https://reqres.in/api"
    API_TIMEOUT = 10
    
    # Web Configuration  
    WEB_BASE_URL = "https://www.saucedemo.com"
    BROWSER_TIMEOUT = 30000  # 30 seconds in milliseconds
    HEADLESS = False  # Set to True for CI/CD
    
    # Test Users
    VALID_USER = {
        'username': 'standard_user',
        'password': 'secret_sauce'
    }
    
    LOCKED_USER = {
        'username': 'locked_out_user',
        'password': 'secret_sauce'
    }
    
    # Reporting
    REPORTS_DIR = "reports"
    SCREENSHOTS_DIR = f"{REPORTS_DIR}/screenshots"