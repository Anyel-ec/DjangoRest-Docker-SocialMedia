from microservice_app.repositories.GenderRepository import GenderRepository

class GenderService:

    @staticmethod
    def create_gender(gender_data):
        new_gender = GenderRepository.add_gender(gender_data)
        return new_gender

    @staticmethod
    def get_gender(gender_id):
        return GenderRepository.get_gender_by_id(gender_id)

    @staticmethod
    def get_all_genders():
        return GenderRepository.get_all_genders()

    @staticmethod
    def update_gender(gender_id, gender_data):
        updated_gender = GenderRepository.update_gender(gender_id, gender_data)
        return updated_gender

    @staticmethod
    def delete_gender(gender_id):
        return GenderRepository.delete_gender(gender_id)