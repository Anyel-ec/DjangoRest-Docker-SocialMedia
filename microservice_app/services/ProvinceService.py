from ..repositories import GenderRepository, ProvinceRepository, StatusRepository


class ProvinceService:

    @staticmethod
    def create_province(province_data):
        new_province = ProvinceRepository.add_province(province_data)
        return new_province

    @staticmethod
    def get_province(province_id):
        return ProvinceRepository.get_province_by_id(province_id)

    @staticmethod
    def get_all_provinces():
        return ProvinceRepository.get_all_provinces()

    @staticmethod
    def update_province(province_id, province_data):
        updated_province = ProvinceRepository.update_province(province_id, province_data)
        return updated_province

    @staticmethod
    def delete_province(province_id):
        return ProvinceRepository.delete_province(province_id)
