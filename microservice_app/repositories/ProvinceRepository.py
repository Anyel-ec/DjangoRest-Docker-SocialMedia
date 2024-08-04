from microservice_app.models.Province import Province
class ProvinceRepository:

    @staticmethod
    def add_province(province_data):
        province = Province(**province_data)
        province.save()
        return province

    @staticmethod
    def get_province_by_id(province_id):
        try:
            return Province.objects.get(id=province_id)
        except Province.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_provinces():
        return Province.objects.all()

    @staticmethod
    def update_province(province_id, province_data):
        province = ProvinceRepository.get_province_by_id(province_id)
        if province:
            for key, value in province_data.items():
                setattr(province, key, value)
            province.save()
            return province
        return None

    @staticmethod
    def delete_province(province_id):
        province = ProvinceRepository.get_province_by_id(province_id)
        if province:
            province.delete()
            return True
        return False