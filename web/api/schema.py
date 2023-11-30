import graphene
from graphql import GraphQLError

from .bitbucket import getDataFromBitbucket
from .outlook import get_mails
from .webex import get_messages


class Query(graphene.ObjectType):
    getPRs = graphene.String(
        username=graphene.String(),
        password=graphene.String(),
        start_date=graphene.String(),
        end_date=graphene.String(),
    )
    getMails = graphene.String(start_date=graphene.String(), end_date=graphene.String())
    getWebex = graphene.String()

    def resolve_getPRs(self, info, username, password, start_date, end_date):
        resp = getDataFromBitbucket(
            start_date=start_date,
            end_date=end_date,
            username=username,
            password=password,
        )
        if resp == None or len(resp) == 0:
            raise GraphQLError("Empty Response")
        return resp

    def resolve_getMails(self, info, start_date, end_date):
        resp = get_mails(start_date=start_date, end_date=end_date)
        if resp == None or len(resp) == 0:
            raise GraphQLError("Empty Response")
        return resp
    
    def resolve_getWebex(self, info):
        resp = get_messages()
        if resp == None or len(resp) == 0:
            raise GraphQLError("Empty Response")
        return resp
