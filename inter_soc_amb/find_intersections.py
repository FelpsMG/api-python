from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class Api_functions:

    def __init__(self, id_proposta):
        load_dotenv()
        print('----------Inicializado')
        self.id_proposta = id_proposta
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.engine = create_engine(f'postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}')


    def _find_intersections(self):

        with self.engine.connect() as conn:
            # sql_query = 'SELECT * FROM apolice_espectros WHERE '
            # result = conn.execute(text(sql_query))
            query = f'SELECT * FROM inter_soc_amb_view WHERE id_proposta = {self.id_proposta};'
            intersection = conn.execute(query).fetchone()
            # intersections = conn.fetchall()
            if intersection == None:
                answer = 'Interseções socioambientais não encontradas'
                return answer
            else:
                answer = 'Interseções socioambientais encontradas'
                return answer

        