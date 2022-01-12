from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from .views import FizzViewSet
from .models import FizzModel

class FizzBuzzTests(APITestCase):

    def test_get_fizz(self):
        """
        Ensure we can create a new fizzbuzz objects and retrieve them.
        """

        request = APIRequestFactory().get("")
        fizz_details = FizzViewSet.as_view({'get': 'retrieve'})
        fizz_1 = FizzModel.objects.create(message="object 1")
        fizz_2 = FizzModel.objects.create(message="object 2")
        response = fizz_details(request, pk=fizz_1.fizzbuzz_id)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FizzModel.objects.count(), 2)
        self.assertEqual(FizzModel.objects.get(fizzbuzz_id = fizz_1.fizzbuzz_id).message, 'object 1')
        self.assertEqual(FizzModel.objects.get(fizzbuzz_id = fizz_2.fizzbuzz_id).message, 'object 2')