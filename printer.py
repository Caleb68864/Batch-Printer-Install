from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class Printer(Base):
    __tablename__ = "printers"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    loc = Column('loc', String, unique=True)
    path = Column('path', String)
    active = Column('active', Integer) # Active=1 Inactive=0

    def __init__(self):
        #engine = create_engine('sqlite:///printers.sqlite', echo=True)
        engine = create_engine('sqlite:///printers.sqlite')
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def addPrinter(self, name, loc, path, active):
        printer = Printer()
        printer.name = name
        printer.loc = loc
        printer.path = path
        printer.active = active
        self.session.add(printer)
        self.session.commit()

    def getPrinters(self):
        printers = self.session.query(Printer).all()
        #print(printers)
        # for printer in printers:
        #      print(printer.id)
        return printers

    def getActivePrinters(self):
        printers = self.session.query(Printer).filter(Printer.active == 1)
        return printers

    def getInactivePrinters(self):
        printers = self.session.query(Printer).filter(Printer.active == 0)
        return printers

    def close(self):
        self.session.close()
        print("Printer Session Closed")

    def __exit__(self):
        self.close()
