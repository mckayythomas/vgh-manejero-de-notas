from rest_framework.test import APITestCase
from rest_framework import status
from models.models import NotasDeEstudiante

# Create your tests here.
class NotasDeEstudianteUpdateTest(APITestCase):
    def setUp(self):
        # Create a sample NotasDeEstudiante object for testing
        self.nota = NotasDeEstudiante.objects.create(
            nota_id=8,
            bimestre=1,
            nota="A",
            comentario="Good job",
        )

    def test_update_notas_valid(self):
        url = f'api/profesor-dashboard/nota/{self.nota.nota_id}/update'
        data = {
            'nota': 'B',
            'comentario': 'Keep it up'
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.nota.refresh_from_db()
        self.assertEqual(self.nota.nota, 'B')
        self.assertEqual(self.nota.comentario, 'Keep it up')

    # def test_update_notas_invalid_missing_fields(self):
    #     url = f'/your-api-endpoint-here/update-nota-comentario/{self.nota.nota_id}/'
    #     data = {
    #         'nota': '',  # Missing nota field intentionally
    #         'comentario': 'Keep it up'
    #     }

    #     response = self.client.put(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data['message'], 'Missing either the nota or comentario fields in request body')

    # def test_update_notas_invalid_not_found(self):
    #     url = '/your-api-endpoint-here/update-nota-comentario/999/'  # Non-existent nota_id
    #     data = {
    #         'nota': 'B',
    #         'comentario': 'Keep it up'
    #     }

    #     response = self.client.put(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.data['message'], 'Nota or Estudiante Tiene Nota with the given ID doesn\'t exist')
