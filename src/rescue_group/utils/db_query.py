from api_projects.schemas import session, Animals


animal = Animals()
session.add(animal)
print(session.query(Animals).filter().all())
