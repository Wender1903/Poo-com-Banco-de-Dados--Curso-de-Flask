from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Serie(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# Inserindo Dados

def adicionar_series(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    serie = Serie(nome=nome, ano=ano, nota=nota)
    session.add(serie)
    session.commit()
    session.close()

# adicionar_series("The Oficce", 2005, 8.7)
# adicionar_series("Brooklyn 99", 2013, 9.7)
# adicionar_series("Loki", 2020, 8.7)

# Atualizar Dados das series

def atualizar_series(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    serie = session.query(Serie).filter_by(id=id).first()
    if serie:
        if nome is not None:
            serie.nome = nome
        if ano is not None:
            serie.ano = nota
        if nota is not None:
            serie.nota = nota

        session.commit()
        session.close()

# atualizar_series(1, "The Oficce", 2006, 9.7)

def deletar_serie(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    serie = session.query(Serie).filter_by(id=id).first()

    if serie:
        session.delete(serie)
    session.commit()
    session.close()

deletar_serie(4)
