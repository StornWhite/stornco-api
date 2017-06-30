from stornco.libs.exceptions import DRFValidationError


class NewTaskMarkedCompleteError(DRFValidationError):
    default_detail = 'New tasks may not be marked as complete when created.'
    default_code = 'tasklist_new_task_marked_complete'


class ChangeUserError(DRFValidationError):
    default_detail = 'Cannot change user for existing task.'
    default_code = 'tasklist_change_user'
