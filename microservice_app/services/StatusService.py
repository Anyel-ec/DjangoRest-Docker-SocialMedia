from ..repositories import GenderRepository, ProvinceRepository, StatusRepository


class StatusService:

    @staticmethod
    def create_status(status_data):
        new_status = StatusRepository.add_status(status_data)
        return new_status

    @staticmethod
    def get_status(status_id):
        return StatusRepository.get_status_by_id(status_id)

    @staticmethod
    def get_all_statuses():
        return StatusRepository.get_all_statuses()

    @staticmethod
    def update_status(status_id, status_data):
        updated_status = StatusRepository.update_status(status_id, status_data)
        return updated_status

    @staticmethod
    def delete_status(status_id):
        return StatusRepository.delete_status(status_id)