from microservice_app.models.Status import  Status
class StatusRepository:

    @staticmethod
    def add_status(status_data):
        status = Status(**status_data)
        status.save()
        return status

    @staticmethod
    def get_status_by_id(status_id):
        try:
            return Status.objects.get(id=status_id)
        except Status.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_statuses():
        return Status.objects.all()

    @staticmethod
    def update_status(status_id, status_data):
        status = StatusRepository.get_status_by_id(status_id)
        if status:
            for key, value in status_data.items():
                setattr(status, key, value)
            status.save()
            return status
        return None

    @staticmethod
    def delete_status(status_id):
        status = StatusRepository.get_status_by_id(status_id)
        if status:
            status.delete()
            return True
        return False