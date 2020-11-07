from typing import Set
from django.contrib.admin import ModelAdmin, StackedInline, site
from patients.models.patient import Patient
from patients.models.lab_results import LabResult
from patients.models.consent import Consent
from patients.models.authorized_parties import AuthorizedParty

# Unregister the provided model admin
# admin.site.unregister(User)


class LabResultInline(StackedInline):
    model = LabResult
    extra = 0
    raw_id_fields =['patient',]

class ConsentInline(StackedInline):
    model = Consent
    extra = 0
    raw_id_fields =['patient',]

class AuthorizedPartyInline(StackedInline):
    model = AuthorizedParty
    extra = 0
    raw_id_fields =['patient',]

class PatientAdmin(ModelAdmin):
    inlines = [
        LabResultInline,
        ConsentInline,
        AuthorizedPartyInline,
    ]
    raw_id_fields=['edited_by',]

site.register(Patient, PatientAdmin)
# @admin.register(User)
# class ITAdmin(UserAdmin):
#     """
#     This is a superuser account, use discretion when creating.
#     """
#     def has_delete_permission(self, request, obj=None):
#         return False
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs):
#         is_superuser = request.user.is_superuser
#         disabled_fields  = set() #type: Set[str]
#         if not is_superuser:
#             disabled_fields |= {
#                 'is_superuser','user_permissions',
#             }
#         if (not is_superuser and obj is not None and obj == request.user):
#             disabled_fields |= {'is_staff', 'is_superuser', 'groups', 'user_permissions',}
#         for field in disabled_fields:
#             if field in form.base_field:
#                 form.base_fields[field].disabled=True
#         return form
