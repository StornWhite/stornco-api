from rest_framework.exceptions import ValidationError


class DRFValidationError(ValidationError):
    """
    Wrapper for Django Rest Framework ValidationError which uses
    default_detail rather than requiring detail for instantiation.
    """
    def __init__(self, detail=None):
        """
        Makes detail an optional argument.
        """
        if not detail:
            detail = self.default_detail

        # Fixes DRF bug, where code is never set.
        self.code = self.default_code

        super().__init__(detail=detail, code=self.default_code)

    @property
    def default_detail(self):
        """
        Requires default_detail property for subclasses.
        """
        raise NotImplementedError

    @property
    def default_code(self):
        """
        Requires default_code property for subclasses.
        """
        raise NotImplementedError
