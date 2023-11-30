import api.schema
import graphene
import graphql_jwt


class Query(api.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    # getMails= graphene.List([1,2,3])
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass
    

schema = graphene.Schema(query=Query,mutation=Mutation)