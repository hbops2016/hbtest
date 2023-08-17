
from sqlalchemy import create_engine
from config.settings import settings
from sqlalchemy.orm import sessionmaker,declarative_base ,Session
import pymysql
pymysql.install_as_MySQLdb()

# 创建数据库连接对象
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,pool_pre_ping=True)
# 创建session对象
SessionLocal = sessionmaker(autocommit=False ,expire_on_commit=False ,bind=engine)

# 动态创建数据的model的基类，数据库model只需要继承该类，即可完成model到数据库表之间的映射
# Base = declarative_base()




