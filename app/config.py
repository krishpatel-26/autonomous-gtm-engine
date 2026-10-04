from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    gtm_min_score:int=50; log_level:str='INFO'
    model_config={'env_file':'.env','extra':'ignore'}
settings=Settings()
