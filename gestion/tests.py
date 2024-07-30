
from django.test import TestCase
from django.urls import reverse
from .models import Copropriete, Coproprietaire

class CoproprieteModelTest(TestCase):
    def setUp(self):
        Copropriete.objects.create(nom="Test Copropriete", adresse="123 Test St", nombre_lots=10)

    def test_copropriete_creation(self):
        copropriete = Copropriete.objects.get(nom="Test Copropriete")
        self.assertEqual(copropriete.adresse, "123 Test St")
        self.assertEqual(copropriete.nombre_lots, 10)

class CoproprieteViewTest(TestCase):
    def setUp(self):
        Copropriete.objects.create(nom="Test Copropriete", adresse="123 Test St", nombre_lots=10)

    def test_copropriete_list_view(self):
        response = self.client.get(reverse('copropriete_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Copropriete")

# Ajoutez d'autres tests pour les autres modèles et vues