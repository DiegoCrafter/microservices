# services/users/project/config.py

class BaseConfig:
    """Base Configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    pass

class TestingConfig(BaseConfig):
    """Test Config"""
    pass

class ProductionConfig(BaseConfig):
    """Production Development"""
    pass 

