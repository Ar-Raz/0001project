from rest_framework import  response, status

import six

from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib.auth.views import redirect_to_login


class GroupRequiredMixin(AccessMixin):

    login_url = 'users:tfentry'
    raise_exception = True
    group_required = None
    permission_denied_message = "برای دسترسی به این صفحه باید {0} خودرا فعال کنید"

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            self.request.session['message'] = 'شما به این صفخه دسترسی ندارید'
            return response.Response({'message' : 'شما به این صفحه دسترسی ندارید'},
                                     status=status.HTTP_401_UNAUTHORIZED)
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def get_group_required(self):
        if self.group_required is None or (
                not isinstance(self.group_required,
                               (list, tuple) + six.string_types)
        ):

            raise ImproperlyConfigured(
                '{0} requires the "group_required" attribute to be set and be '
                'one of the following types: string, unicode, list or '
                'tuple'.format(self.__class__.__name__))
        if not isinstance(self.group_required, (list, tuple)):
            self.group_required = (self.group_required,)
        return self.group_required

    def check_membership(self, groups):
        """ Check required group(s) """
        if self.request.user.is_superuser:
            return True
        user_groups = self.request.user.groups.values_list("name", flat=True)
        return set(groups).intersection(set(user_groups))

    def dispatch(self, request, *args, **kwargs):
        in_group = False
        if request.user.is_authenticated:
            in_group = self.check_membership(self.group_required())

        if not in_group:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)