from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Medicine
from .serializers import MedicineSerializer


# GET all medicines + POST create new
@api_view(['GET', 'POST'])
def medicines_list(request):

    if request.method == 'GET':
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET single medicine + UPDATE + DELETE
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def medicine_detail(request, id):

    try:
        medicine = Medicine.objects.get(id=id)
    except Medicine.DoesNotExist:
        return Response({"error": "Medicine not found"}, status=404)

    # GET single record
    if request.method == 'GET':
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    # UPDATE (Full)
    if request.method == 'PUT':
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # UPDATE (Partial)
    if request.method == 'PATCH':
        serializer = MedicineSerializer(medicine, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE
    if request.method == 'DELETE':
        medicine.delete()
        return Response({"message": "Medicine deleted"}, status=200)
