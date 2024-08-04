from ..models import Gender, Province, Status


class GenderRepository:

    @staticmethod
    def add_gender(gender_data):
        gender = Gender(**gender_data)
        gender.save()
        return gender

    @staticmethod
    def get_gender_by_id(gender_id):
        try:
            return Gender.objects.get(id=gender_id)
        except Gender.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_genders():
        return Gender.objects.all()

    @staticmethod
    def update_gender(gender_id, gender_data):
        gender = GenderRepository.get_gender_by_id(gender_id)
        if gender:
            for key, value in gender_data.items():
                setattr(gender, key, value)
            gender.save()
            return gender
        return None

    @staticmethod
    def delete_gender(gender_id):
        gender = GenderRepository.get_gender_by_id(gender_id)
        if gender:
            gender.delete()
            return True
        return False