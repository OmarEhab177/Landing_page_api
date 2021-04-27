from .serializers import MessageSerializer
# from .permissions import IsOwner
from .models import Message

# from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.



class MessageListView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (IsAuthenticated,)

class MessageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (IsOwner,)




























# @api_view(['GET'])
# def messageList(request):
#     messages = Message.objects.all()
#     serializer = MessageSerializer(messages, many=True) 
#     return Response(serializer.data)

# @api_view(['GET'])
# def messageDetail(request, pk):
#     message = Message.objects.get(id=pk)
#     serializer = MessageSerializer(message, many=False) 
#     return Response(serializer.data)

# @api_view(['POST'])
# def messageCreate(request):
#     serializer = MessageSerializer(data=request.data) 
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def messageUpdate(request, pk):
#     message = Message.objects.get(id=pk)
#     serializer = MessageSerializer(instance=message, data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def messageDelete(request, pk):
#     message = Message.objects.get(id=pk)
#     message.delete()

#     return Response("Deleted Successfully")
