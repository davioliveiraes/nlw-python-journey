import pytest # type: ignore
import uuid
from datetime import datetime
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
activities_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="integracao com banco de dados")
def test_registry_activity():
   conn = db_connection_handler.get_connection()
   activities_repository = ActivitiesRepository(conn)

   activity_infos = {
      "id": activities_id,
      "trip_id": trip_id,
      "title": "Correr na praia",
      "occurs_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   }
   activities_repository.registry_activity(activity_infos)

@pytest.mark.skip(reason="integracao com banco de dados")
def test_find_activities_from_trip():
   conn = db_connection_handler.get_connection()
   activities_repository = ActivitiesRepository(conn)

   activities = activities_repository.find_activities_from_trip(trip_id)
   print(activities)

