from rest_framework import serializers
from .models import Aluno, Professor

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
      model = Aluno
      fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
      model = Professor
      fields = '__all__'
    