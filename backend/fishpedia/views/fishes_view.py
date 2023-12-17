from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import generics
from fishpedia.serializers.fishes_serializer import FishSerializer
from fishpedia.models.fishes import Fish


class FishListCreateView(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def get_queryset(self):
        return Fish.objects.all()

    def get(self, request, *args, **kwargs):
        fish_list = self.get_queryset()
        return render(request, 'fish_list.html', {'fish_list': fish_list})

class FishDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def get(self, request, *args, **kwargs):
        try:
            fish = self.get_object()
        except Fish.DoesNotExist:
            return redirect(reverse('fish-list-create'))

        return render(request, 'fish_detail.html', {'fish': fish})
