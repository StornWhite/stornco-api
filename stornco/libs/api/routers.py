from rest_framework.routers import DefaultRouter


class NoPutRouter(DefaultRouter):
    """
    Router class that does not pass the PUT method.

    PATCH method can perform full or partial updates, while PUT can perform
    partial updates only.  Because PATCH's functionality entirely encompasses
    PUT's, a best practice is to eliminate PUT entirely.
    """
    def get_method_map(self, viewset, method_map):
        """
        Removes PUT method.
        """
        bound_methods = super().get_method_map(viewset, method_map)

        if 'put' in bound_methods.keys():
            del bound_methods['put']

        return bound_methods
