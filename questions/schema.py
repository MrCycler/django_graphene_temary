# graphene import
import graphene
from graphene_django import DjangoObjectType

# app models auto import
from .models import Question,QuestionOption

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionOptionType(DjangoObjectType):
    class Meta:
        model = QuestionOption
        fields = '__all__'

class Query(graphene.ObjectType):
    # List all question options
    all_questions = graphene.List(QuestionType)
    all_question_options = graphene.List(QuestionOptionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.ID(required=True))

    def resolve_all_questions(root,info):
        return Question.objects.all()

    def resolve_all_question_options(root, info):
        # We can easily optimize query count in the resolve method
        return QuestionOption.objects.select_related("question").all()

    def resolve_question_by_id(root, info, id):
        try:
            return Question.objects.get(pk=id)
        except Question.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)