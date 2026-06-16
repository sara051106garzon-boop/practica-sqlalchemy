class Config:
    SECRET_KEY = "12456789"
    
    # Ponemos tus credenciales fijas para que Flask no pueda fallar
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/Musigest"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False