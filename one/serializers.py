from rest_framework import serializers
from .models import student, models

class CustomStudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    key = serializers.ReadOnlyField()

    class Meta:
        model = student
        fields = ["first_name", "last_name","age","contact", "parentAge", "key"]

    def create(self, validated_data):
        student_db_item = student(
            name=f'{validated_data["first_name"]} {validated_data["last_name"]}',
            age=validated_data["age"],
            parentAge=validated_data["parentAge"],
            contact=validated_data["contact"]
        )
        #student_db_item.is_valid(raise_exception=True)
        student_db_item.save()
        return student_db_item
    
    def update(self, instance, validated_data):
        instance.name = f'{validated_data["first_name"]} {validated_data["last_name"]}'
        instance.age = validated_data['age']
        instance.contact = validated_data['contact']
        instance.parentAge = validated_data['parentAge']
        instance.save()
        return instance
    
    def patch(self, instance, validated_data):
        print(instance.name.split(" "))
        instance.name = f'{validated_data.get("first_name", instance.name.split(" ")[0])} {validated_data.get("last_name", instance.name.split(" ")[1])}'
        instance.age = validated_data.get('age', instance.age)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.parentAge = validated_data.get('parentAge', instance.parentAge)
        instance.save()
        return instance

    def list(self,queryset):
        data =[]
        for x in queryset:
            print( "Mr."+ x.__dict__['name'].split(" ")[1])
            data.append("Mr."+ x.__dict__['name'].split(" ")[1])
        print (data)
        return data
    
    def retrive(self,instance):
        print(instance.__dict__['name'])
        return instance.__dict__['name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"
