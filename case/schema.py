import graphene
from graphene_django import DjangoObjectType
from case.models import *
from user.models import *

Users = get_user_model()

class CaseType(DjangoObjectType):
    class Meta:
        model = Case
        fields = '__all__'

class UserInfo(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'

class UserDetails(DjangoObjectType):
    class Meta:
        model = UserDetails
        fields = '__all__'


class Query(graphene.ObjectType):
    cases = graphene.List(CaseType)
    pet_det = graphene.List(UserDetails)
    res_det = graphene.List(UserDetails)
    pet_adv_det = graphene.List(UserDetails)
    res_adv_det = graphene.List(UserDetails)
    per_inv_det = graphene.List(UserDetails)


    @graphene.resolve_only_args
    def resolve_pet_det(self):
        if not self: return ""
        else: return self.petitioner.all()

    @graphene.resolve_only_args
    def resolve_res_det(self):
        if not self: return ""
        else: return self.respondent.all()

    @graphene.resolve_only_args
    def resolve_pet_adv_det(self):
        if not self: return ""
        else: return self.petitioner_advocate.all()

    @graphene.resolve_only_args
    def resolve_res_adv_det(self):
        if not self: return ""
        else: return self.respondent_advocate.all()

    @graphene.resolve_only_args
    def resolve_per_inv_det(self):
        if not self: return ""
        else: return self.person_involved.all()

schema = graphene.Schema(query = Query)