from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    orders = relationship("Orders", back_populates="client")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    cost = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", back_populates="orders")

    def __init__(self, name, cost, client_id):
        self.name = name
        self.cost = cost
        self.client_id = client_id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


connection_string = "sqlite:///doc.sqlite"
engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# petya = Clients("Petya")
# katya = Clients("Katya")
# vasya = Clients("Vasya")
# frosya = Clients("Frosya")
# or_1 = Orders("key", 10, 1)
# or_2 = Orders("wine", 7, 2)
# or_3 = Orders("laptop", 560, 2)
# or_4 = Orders("handy", 350, 3)
# or_5 = Orders("flower", 25, 4)
# or_6 = Orders("laces", 2, 1)
# or_7 = Orders("boots", 35, 1)
# or_8 = Orders("battaries", 4, 3)
# or_9 = Orders("watch", 90, 3)
# or_10 = Orders("lock", 10, 1)
# or_11 = Orders("dirt", 20, 4)
# session.add_all(
#     [
#         petya,
#         katya,
#         vasya,
#         frosya,
#         or_1,
#         or_2,
#         or_3,
#         or_4,
#         or_5,
#         or_6,
#         or_7,
#         or_8,
#         or_9,
#         or_10,
#         or_11,
#     ]
# )
# session.commit()

#########
# clients = session.query(Clients).all()
# for client in clients:
#     print(f"client(№{client.id}) {client.name}:")
#     for order in client.orders:
#         print(f"    order for client №{order.client_id} {(order.name).ljust(11)}{order.cost}$")
# session.close()
########

##########
# connection = engine.connect()
# query = connection.execute(
#     text(
#         "select clients.name as client_name, orders.name as order_name, orders.cost from clients JOIN orders on clients.id = orders.client_id"
#     )
# )
# for row in query.mappings():
#     print(
#         f"клиент {row['client_name']}: {row['order_name']}, стоимость: {row['cost']}$"
#     )
# connection.close()
# ########
