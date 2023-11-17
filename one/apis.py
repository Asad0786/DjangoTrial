from .models import student
from .serializers import StudentSerializer, CustomStudentSerializer
from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class CustomStudentViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    
    queryset = student.objects.all()
    serializer_class = CustomStudentSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        userResponse = serializer.create(serializer.validated_data )
        return Response(StudentSerializer(userResponse).data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # serializer = self.get_serializer(instance, data=request.data)
        serializer = self.get_serializer(instance, data=request.data)
        
        if not serializer.is_valid():
            return Response("Error", status=400)
        
        updated_student_item = serializer.update(instance, serializer.validated_data)
        return Response(StudentSerializer(updated_student_item).data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        x = instance.delete()
        print(type(x))
        return Response("Deleted", status=201)
    
    def partial_update(self, request,*args, **kwargs):
        instance = self.get_object()
        print(11111)
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial= True)
        serializer.is_valid(raise_exception=True)
        # instance = instance.save()
        print(instance.__dict__)
        patched_update_student = serializer.patch(instance, serializer.validated_data)
        return Response(StudentSerializer(patched_update_student).data, status=201)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer()
        
        return Response(serializer.list(queryset), status=201)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # print()
        return Response(serializer.retrive(instance), status=201)

    



    


