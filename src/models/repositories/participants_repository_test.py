import pytest # type: ignore
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
participant_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())

@pytest.mark.skip(reason="integração com banco de dados")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    cursor = conn.cursor()
    cursor.execute(
      '''
         INSERT INTO emails_to_invite (id, email)
         VALUES (?, ?)
      ''', (emails_to_invite_id, "roberta@exemple.com")
   )
    conn.commit()

    participant_infos = {
      "id": participant_id,
      "trip_id": trip_id,
      "emails_to_invite_id": emails_to_invite_id,
      "name": "Roberta Cavalcante"
   }

    participants_repository.registry_participant(participant_infos)

@pytest.mark.skip(reason="integração com banco de dados")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print(f"Participantes Encontrados: {participants}")

    assert len(participants) > 0, "Nenhum participante encontrado"
    assert participants[0][1] == "Roberta Cavalcante", "Nome do participante não confere"
    print(f"Participante Encontrado: {participants[0]}")

@pytest.mark.skip(reason="integração com banco de dados")
def test_update_participant_status():
   conn = db_connection_handler.get_connection()
   participants_repository = ParticipantsRepository(conn)

   participants = participants_repository.update_participant_status(participant_id)

   cursor = conn.cursor()
   cursor.execute(
      '''
         SELECT is_confirmed FROM participants WHERE id = ?
      ''', (participant_id,)
   )
   result = cursor.fetchone()

   assert result is not None, "Partipante não encontrado"
   print(f"Status atualizado com sucesso: is_confirmed = {result[0]}")
