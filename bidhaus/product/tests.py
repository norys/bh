from unittest import mock

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product


class ProductListTest(APITestCase):
    def test_gets_list(self):
        product = Product.objects.create(
            name="Cool Watch",
            description="it is shiny!",
            price=1200,
            in_stock=True,
        )

        response = self.client.get(reverse("product:product-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.json(), [{
            "id": product.pk,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "in_stock": product.in_stock,
        }])

    def test_create_product(self):
        data = {
            "name": "Fun Item",
            "description": "something different",
            "price": 1500,
            "in_stock": True,
        }

        response = self.client.post(reverse("product:product-list"), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response.json(), {
            "id": mock.ANY,
            **data,
        })


class ProductDetailTest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Wacky Product",
            description="wack wack wack...",
            price=10000,
            in_stock=True,
        )
        self.url = reverse("product:product-detail", kwargs={"pk": self.product.pk})

    def test_gets_product(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), {
            "id": self.product.pk,
            "name": self.product.name,
            "description": self.product.description,
            "price": self.product.price,
            "in_stock": self.product.in_stock,
        })

    def test_updates_product(self):
        data = {
            "name": "a different product name",
            "description": "a different description",
            "price": 400,
            "in_stock": False,
        }

        response = self.client.patch(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), {
            "id": self.product.pk,
            **data,
        })

    def test_delete_product(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Product.DoesNotExist, Product.objects.get, pk=self.product.pk)
