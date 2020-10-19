import json
import warnings

from django import template
from django.apps import apps
from django.utils.html import format_html
from django.conf import settings

from users.models import ProducerProfile, Profile, User
from users.serializers import UserSerializer

register = template.Library()


# class UserNode(template.Node):
#     def __init__(self, request):
#         self.request = request

#     def render(self, context):
#         context['user'] = request

# class ObjectsNode(template.Node):
#     def __init__(self, model, manager_method, limit, var_name):
#         self.model = model
#         self.manager_method = manager_method
#         self.limit = template.Variable(limit) if limit else None
#         self.var_name = var_name
#     def render(self, context):
#         if "." in self.manager_method:
#             manager, method = self.manager_method.split(".")
#         else:
#             manager = "_default_manager"
#             method = self.manager_method
            
#         model_manager = getattr(self.model, manager)
#         fallback_method = self.model._default_manager.none
#         qs = getattr(model_manager, method, fallback_method)()
#         limit = None
#         if self.limit:
#             try:
#                 limit = self.limit.resolve(context)
#             except template.VariableDoesNotExist:
#                 limit = None
#         context[self.var_name] = qs[:limit] if limit else qs
#         return ""

# @register.tag
# def load_user_json(parser, token):
#     limit_count = 1
#     try:
#         (tag_name, manager_method,
#         str_from, app_model,
#         str_limit, limit_count,
#         str_as, var_name) = token.split_contents()
#     except ValueError:
#         try:
#             (tag_name, manager_method,
#             str_from, app_model,
#             str_as, var_name) = token.split_contents()
#         except ValueError:
#             tag_name = token.contents.split()[0]
#             raise template.TemplateSyntaxError(
#                 f"{tag_name} tag requires the following syntax: "
#                 f"{{% {tag_name} [<manager>.]<method> from "
#                 "<app_name>.<model_name> [limit <amount>] "
#                 "as <var_name> %}")
#     try:
#         app_name, model_name = app_model.split(".")
#     except ValueError:
#         raise template.TemplateSyntaxError(
#             "load_objects tag requires application name "
#             "and model name, separated by a dot")
#     model = apps.get_model(app_name, model_name)
#     return ObjectsNode(
#         model, manager_method, limit_count, var_name
#     )

@register.simple_tag
def user_tag(username):
    user = User.objects.get(username=username)
    if user.is_producer:
        profile = ProducerProfile.objects.get(user=user)
    else: 
        profile = Profile.objects.get(user=user)
    picture = profile.profile_picture.url
    user_date = {
        "is_logined" : user.is_authenticated,
        "is_superuser" : user.is_superuser,
        "is_producer" : user.is_producer,
        "is_staff" : user.is_staff,
        "username" : user.username,
        'picture' : picture,
    }
    json_data = json.dumps(user_date)
    return json_data


@register.inclusion_tag('test2.html', takes_context=True)
def csrf_tag(context):
    csrf = context['csrftoken']
    return {"csrf" : csrf}


class CsrfTokenMetaNode(template.Node):
    def render(self, context):
        csrf_token = context.get('csrf_token')
        if csrf_token:
            if csrf_token == 'NOTPROVIDED':
                return format_html("")
            else:
                return format_html('<meta  name="csrf" content="{}">', csrf_token)
        else:
            # It's very probable that the token is missing because of
            # misconfiguration, so we raise a warning
            if settings.DEBUG:
                warnings.warn(
                    "A {% csrf_token %} was used in a template, but the context "
                    "did not provide the value.  This is usually caused by not "
                    "using RequestContext."
                )
            return ''

@register.tag
def csrf_token_tag(parser, token):
    return CsrfTokenMetaNode()